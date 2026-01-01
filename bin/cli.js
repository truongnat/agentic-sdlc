#!/usr/bin/env node

import fs from 'fs-extra';
import path from 'path';
import { fileURLToPath } from 'url';
import { log } from './utils/colors.js';
import { parseArgs } from './utils/args-parser.js';
import { showHelp, showVersion } from './commands/help.js';
import { listTemplates } from './commands/list.js';
import { install } from './commands/install.js';
import { createProject } from './commands/create.js';
import { setupIDE } from './commands/ide.js';
import { initKnowledgeBase } from './commands/init-kb.js';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const templatePath = path.join(__dirname, '../.agent');

// Package info
const packageJson = JSON.parse(
  await fs.readFile(path.join(__dirname, '../package.json'), 'utf-8')
);

/**
 * Main CLI entry point
 */
async function main() {
  const args = process.argv.slice(2);

  // Handle no arguments
  if (args.length === 0) {
    showHelp(packageJson);
    process.exit(0);
  }

  const { options, args: filteredArgs } = parseArgs(args);
  const command = filteredArgs[0];

  // Handle help flags
  if (command === '-h' || command === '--help' || command === 'help') {
    showHelp(packageJson);
    process.exit(0);
  }

  // Handle version flags
  if (command === '-v' || command === '--version' || command === 'version') {
    showVersion(packageJson);
    process.exit(0);
  }

  // Handle commands
  switch (command) {
    case 'install':
      await install(templatePath, options);
      break;

    case 'create':
      const projectName = filteredArgs[1];
      if (!projectName) {
        log.error('Project name is required');
        console.log('Usage: agentic-sdlc create <project-name>');
        process.exit(1);
      }
      await createProject(templatePath, projectName, options);
      break;

    case 'list':
      await listTemplates(templatePath);
      break;

    case 'ide':
      const ideName = filteredArgs[1];
      if (!ideName) {
        log.error('IDE name is required');
        console.log('Usage: agentic-sdlc ide <cursor|copilot|windsurf|cline|aider|all>');
        process.exit(1);
      }
      await setupIDE(templatePath, ideName, options);
      break;

    case 'init-kb':
      await initKnowledgeBase(templatePath, options);
      break;

    default:
      log.error(`Unknown command: ${command}`);
      console.log('Run agentic-sdlc --help for usage information');
      process.exit(1);
  }
}

// Error handlers
process.on('uncaughtException', (err) => {
  log.error('Unexpected error occurred');
  log.error(err.message);
  process.exit(1);
});

process.on('unhandledRejection', (err) => {
  log.error('Unhandled promise rejection');
  log.error(err.message);
  process.exit(1);
});

main();
