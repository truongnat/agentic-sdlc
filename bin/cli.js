#!/usr/bin/env node
import { spawn } from 'child_process';
import { fileURLToPath } from 'url';
import { dirname, join, resolve } from 'path';
import fs from 'fs';

const __dirname = dirname(fileURLToPath(import.meta.url));
const rootDir = resolve(__dirname, '..');

const commands = {
    'release': 'tools/release/release.py',
    'kb': 'bin/kb_cli.py',
    'agent': 'tools/run.py',
    'validate': 'tools/validation/validate.py',
    'health': 'tools/validation/health-check.py',
    'setup': 'tools/setup/init.py',
    'brain': 'tools/brain/brain_cli.py',
    'research': 'tools/research/research_agent.py'
};

const args = process.argv.slice(2);
const command = args[0];

function printUsage() {
    console.log("Usage: agentic-sdlc <command> [args]");
    console.log("Commands:");
    console.log("  release   Manage releases (args: release, preview, changelog, version)");
    console.log("  workflow  Run workflows (args: cycle, housekeeping, etc.)");
    console.log("  kb        Knowledge Base tools");
    console.log("  agent     Run default agent");
    console.log("  validate  Validate system");
    console.log("  health    Check health");
    console.log("  setup     Initialize project");
    console.log("  brain     Brain system management");
    console.log("  research  Research agent");
}

if (!command || command === '--help' || command === '-h') {
    printUsage();
    process.exit(command ? 0 : 1);
}

let scriptPath = commands[command];
let scriptArgs = args.slice(1);

// Special handling for workflows
if (command === 'workflow') {
    const sub = args[1];
    if (sub) {
        scriptPath = `tools/workflows/${sub}.py`;
        scriptArgs = args.slice(2);
    } else {
        console.error("Please specify a workflow (e.g., cycle, housekeeping)");
        process.exit(1);
    }
}

if (!scriptPath) {
    console.error(`Unknown command: ${command}`);
    printUsage();
    process.exit(1);
}

const fullPath = join(rootDir, scriptPath);

if (!fs.existsSync(fullPath)) {
    console.error(`Script not found: ${scriptPath}`);
    process.exit(1);
}

const pythonProcess = spawn('python', [fullPath, ...scriptArgs], {
    stdio: 'inherit',
    cwd: rootDir // Execute from project root
});

pythonProcess.on('exit', (code) => {
    process.exit(code ?? 0);
});

pythonProcess.on('error', (err) => {
    console.error('Failed to start python process:', err);
    process.exit(1);
});
