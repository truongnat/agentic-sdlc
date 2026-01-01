import fs from 'fs-extra';
import path from 'path';
import { log } from '../utils/colors.js';

/**
 * Install instructions in current directory
 */
export async function install(templatePath, options = {}) {
  const startTime = Date.now();
  const targetPath = path.join(process.cwd(), '.agent');

  try {
    if (!options.quiet) log.header('🚀 Installing Template Instructions');

    // Validate environment
    if (options.verbose) log.step('Validating environment...');
    if (!await fs.pathExists(templatePath)) {
      throw new Error(`Template source not found at: ${templatePath}`);
    }

    // Check existing installation
    if (!options.quiet) log.step('Checking for existing installation...');
    if (await fs.pathExists(targetPath)) {
      if (!options.force) {
        log.warning('.agent directory already exists');
        log.info('Use --force to overwrite existing files');
        process.exit(0);
      } else {
        log.warning('Overwriting existing installation...');
        await fs.remove(targetPath);
      }
    }

    // Copy files
    if (!options.quiet) log.step('Copying template files...');
    await fs.copy(templatePath, targetPath, {
      overwrite: options.force,
      preserveTimestamps: true,
    });

    // Verify installation
    if (options.verbose) {
      log.step('Verifying installation...');
      const files = await fs.readdir(targetPath, { recursive: true });
      log.success(`Verified ${files.length} files installed`);
    }

    // Success message
    if (!options.quiet) {
      log.success('Installation complete!');
      console.log(`Location: ${targetPath}`);
      console.log(`\nNext Steps:`);
      console.log('  • Setup IDE: agentic-sdlc ide cursor');
      console.log('  • Review: .agent/usage.md');
      console.log('  • Start: /pm Build your project\n');

      const duration = ((Date.now() - startTime) / 1000).toFixed(2);
      log.info(`Completed in ${duration}s`);
    }

    process.exit(0);
  } catch (err) {
    log.error('Installation failed');
    log.error(err.message);
    if (options.verbose) console.error('\nStack trace:', err.stack);
    process.exit(1);
  }
}
