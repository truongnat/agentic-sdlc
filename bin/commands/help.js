import { colors } from '../utils/colors.js';

/**
 * Display help information
 */
export function showHelp(packageJson) {
  console.log(`
${colors.bright}${colors.cyan}agentic-sdlc${colors.reset} ${colors.dim}v${packageJson.version}${colors.reset}

${colors.bright}USAGE${colors.reset}
  ${colors.cyan}agentic-sdlc${colors.reset} ${colors.yellow}<command>${colors.reset} ${colors.dim}[options]${colors.reset}

${colors.bright}COMMANDS${colors.reset}
  ${colors.yellow}install${colors.reset}              Install instructions into current directory
  ${colors.yellow}create${colors.reset} ${colors.dim}<name>${colors.reset}       Create new project with instructions
  ${colors.yellow}list${colors.reset}                List available templates and roles
  ${colors.yellow}ide${colors.reset} ${colors.dim}<ide-name>${colors.reset}     Setup IDE integration (cursor, copilot, windsurf, cline, aider, all)
  ${colors.yellow}init-kb${colors.reset}             Initialize knowledge base structure
  ${colors.yellow}version${colors.reset}             Show version information
  ${colors.yellow}help${colors.reset}                Show this help message

${colors.bright}OPTIONS${colors.reset}
  ${colors.dim}-h, --help${colors.reset}          Show help
  ${colors.dim}-v, --version${colors.reset}       Show version
  ${colors.dim}-f, --force${colors.reset}         Force overwrite existing files
  ${colors.dim}-q, --quiet${colors.reset}         Suppress output
  ${colors.dim}--verbose${colors.reset}           Show detailed output
  ${colors.dim}--no-color${colors.reset}          Disable colored output

${colors.bright}EXAMPLES${colors.reset}
  ${colors.dim}# Install in current directory${colors.reset}
  ${colors.cyan}agentic-sdlc${colors.reset} install

  ${colors.dim}# Create new project${colors.reset}
  ${colors.cyan}agentic-sdlc${colors.reset} create my-project

  ${colors.dim}# Setup Cursor IDE integration${colors.reset}
  ${colors.cyan}agentic-sdlc${colors.reset} ide cursor

  ${colors.dim}# Setup all IDE integrations${colors.reset}
  ${colors.cyan}agentic-sdlc${colors.reset} ide all

  ${colors.dim}# Initialize knowledge base${colors.reset}
  ${colors.cyan}agentic-sdlc${colors.reset} init-kb

  ${colors.dim}# List available templates${colors.reset}
  ${colors.cyan}agentic-sdlc${colors.reset} list

${colors.bright}IDE INTEGRATIONS${colors.reset}
  ${colors.dim}cursor${colors.reset}      - Cursor IDE (.cursorrules)
  ${colors.dim}copilot${colors.reset}     - GitHub Copilot (.github/copilot-instructions.md)
  ${colors.dim}windsurf${colors.reset}    - Windsurf Cascade (.windsurfrules)
  ${colors.dim}cline${colors.reset}       - Cline VS Code Extension
  ${colors.dim}aider${colors.reset}       - Aider CLI (.aider.conf.yml)
  ${colors.dim}all${colors.reset}         - Setup all IDE integrations

${colors.bright}DOCUMENTATION${colors.reset}
  ${colors.dim}Repository:${colors.reset} https://github.com/yourusername/template-instructions
  ${colors.dim}Issues:${colors.reset}     https://github.com/yourusername/template-instructions/issues
`);
}

/**
 * Display version information
 */
export function showVersion(packageJson) {
  console.log(`${colors.cyan}agentic-sdlc${colors.reset} ${colors.bright}v${packageJson.version}${colors.reset}`);
  console.log(`${colors.dim}${packageJson.description}${colors.reset}`);
}
