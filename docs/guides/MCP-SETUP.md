# 🔧 MCP Server Setup Instructions

This guide walks you through setting up all MCP servers for the Agentic SDLC project.

## Prerequisites

1. **Install UV (Python Package Manager)**
   ```bash
   # Windows (PowerShell)
   powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
   
   # Or via pip
   pip install uv
   ```

2. **Verify Installation**
   ```bash
   uvx --version
   ```

## 📋 Configuration Steps

### 1. Copy Environment Variables
```bash
copy .env.template .env
```

### 2. Configure API Keys

Edit `.env` and add your credentials:

#### GitHub (Required for @PM, @PO, @REPORTER)
- Get token: https://github.com/settings/tokens
- Permissions needed: `repo`, `read:org`, `read:project`
```
GITHUB_TOKEN=ghp_your_token_here
GITHUB_REPO=your-org/your-repo
```

#### Brave Search (Required for @PM, @PO)
- Get API key: https://brave.com/search/api/
```
BRAVE_API_KEY=your_brave_api_key
```

#### Firecrawl (Required for @SECA, @DEVOPS)
- Get API key: https://firecrawl.dev/
```
FIRECRAWL_API_KEY=your_firecrawl_key
```

#### PostgreSQL/Supabase (Required for @SA, @DEV)
```
POSTGRES_CONNECTION_STRING=postgresql://user:password@host:5432/database
# OR for Supabase
SUPABASE_URL=https://your-project.supabase.co
SUPABASE_KEY=your_supabase_key
```

#### Vercel (Optional for @DEVOPS)
- Get token: https://vercel.com/account/tokens
```
VERCEL_TOKEN=your_vercel_token
```

### 3. Test MCP Servers

After configuration, restart Kiro and test each server:

1. Open Command Palette (Ctrl+Shift+P)
2. Search for "MCP: Reconnect All Servers"
3. Check the MCP Server view in Kiro panel

## 🛠️ Configured Servers

| Server | Status | Tools Available |
|--------|--------|-----------------|
| GitHub | ✅ Configured | Issues, PRs, Milestones |
| Brave Search | ✅ Configured | Web search, research |
| Playwright | ✅ Configured | Browser automation, E2E testing |
| Sequential Thinking | ✅ Configured | Logic reasoning |
| PostgreSQL | ✅ Configured | Database operations |
| Docker | ✅ Configured | Container management |
| Firecrawl | ✅ Configured | Web scraping |

## 📝 Servers Requiring Manual Setup

Some servers from the MCP-GUIDE.md require additional setup or are not available via uvx:

### Vercel
- Install: `npm install -g @modelcontextprotocol/server-vercel`
- Add to mcp.json manually with node command

### GitIngest
- Custom implementation needed
- Alternative: Use GitHub MCP + file reading

### Apidog
- Check if API available or use Postman/Insomnia alternatives

### Context7
- Custom architecture analysis tool
- May need custom MCP server implementation

### DesktopCommander
- Windows-specific automation
- Consider PowerShell scripts as alternative

## 🔍 Troubleshooting

### Server Not Connecting
1. Check `.env` file has correct values
2. Verify uvx is installed: `uvx --version`
3. Check logs in Kiro MCP Server view
4. Try manual reconnect from Command Palette

### Missing Dependencies
```bash
# Reinstall UV
pip install --upgrade uv

# Clear UV cache
uvx cache clear
```

### Permission Issues
- Ensure GitHub token has correct scopes
- Check API key quotas and limits
- Verify network/firewall settings

## 🚀 Next Steps

1. Test each MCP server with a simple query
2. Configure auto-approve for trusted tools (optional)
3. Review role-specific MCP usage in MCP-GUIDE.md
4. Set up additional advanced MCPs as needed

---
*Last Updated: 2026-01-01*
