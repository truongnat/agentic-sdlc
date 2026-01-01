import fs from 'fs-extra';
import path from 'path';
import { colors, log } from '../utils/colors.js';

/**
 * Create new project with instructions
 */
export async function createProject(templatePath, projectName, options = {}) {
  const startTime = Date.now();
  const targetPath = path.join(process.cwd(), projectName);

  try {
    if (!options.quiet) log.header(`🚀 Creating Project: ${projectName}`);

    // Check if project exists
    if (await fs.pathExists(targetPath)) {
      if (!options.force) {
        log.error(`Directory '${projectName}' already exists`);
        log.info('Use --force to overwrite');
        process.exit(1);
      } else {
        log.warning('Overwriting existing project...');
        await fs.remove(targetPath);
      }
    }

    // Create project directory
    if (!options.quiet) log.step('Creating project directory...');
    await fs.ensureDir(targetPath);

    // Copy instructions
    if (!options.quiet) log.step('Installing instructions...');
    await fs.copy(templatePath, path.join(targetPath, '.agent'));

    // Create basic project structure
    if (!options.quiet) log.step('Setting up project structure...');

    // Create docs structure
    await fs.ensureDir(path.join(targetPath, 'docs', 'sprints', 'sprint-1', 'plans'));
    await fs.ensureDir(path.join(targetPath, 'docs', 'sprints', 'sprint-1', 'designs'));
    await fs.ensureDir(path.join(targetPath, 'docs', 'sprints', 'sprint-1', 'reviews'));
    await fs.ensureDir(path.join(targetPath, 'docs', 'sprints', 'sprint-1', 'logs'));
    await fs.ensureDir(path.join(targetPath, 'docs', 'sprints', 'sprint-1', 'tests'));
    await fs.ensureDir(path.join(targetPath, 'docs', 'sprints', 'sprint-1', 'reports'));
    await fs.ensureDir(path.join(targetPath, 'docs', 'global', 'reports'));

    // Create package.json
    await fs.writeJson(
      path.join(targetPath, 'package.json'),
      {
        name: projectName,
        version: '1.0.0',
        description: 'Project created with agentic-sdlc',
        main: 'index.js',
        scripts: {
          test: 'echo "Error: no test specified" && exit 1',
        },
      },
      { spaces: 2 }
    );

    // Create README
    await fs.writeFile(
      path.join(targetPath, 'README.md'),
      `# ${projectName}\n\nProject created with agentic-sdlc.\n\n## Getting Started\n\n1. Review instructions: \`.agent/usage.md\`\n2. Setup IDE: \`agentic-sdlc ide cursor\`\n3. Start planning: \`/pm Build your project\`\n\n## Documentation\n\nAll project documentation is in \`docs/\` folder organized by sprints.\n`
    );

    // Create .gitignore
    await fs.writeFile(
      path.join(targetPath, '.gitignore'),
      `node_modules/\n.DS_Store\n*.log\n.env\n.env.local\n.agent/\n`
    );

    // Success
    if (!options.quiet) {
      log.success('Project created successfully!');
      console.log(`Location: ${targetPath}`);
      console.log(`\nNext Steps:`);
      console.log(`  ${colors.cyan}cd ${projectName}${colors.reset}`);
      console.log('  agentic-sdlc ide cursor');
      console.log('  • Review .agent/usage.md');
      console.log('  • Initialize git repository');
      console.log('  • Start: /pm Build your project\n');

      const duration = ((Date.now() - startTime) / 1000).toFixed(2);
      log.info(`Completed in ${duration}s`);
    }

    process.exit(0);
  } catch (err) {
    log.error('Project creation failed');
    log.error(err.message);
    if (options.verbose) console.error('\nStack trace:', err.stack);
    process.exit(1);
  }
}
