# Deployment Guide

Quick guide to deploy the Agentic SDLC landing page.

## 🚀 Quick Deploy to Vercel

### Option 1: GitHub Integration (Recommended)

1. **Push to GitHub:**
   ```bash
   git init
   git add .
   git commit -m "feat: Complete landing page implementation"
   git branch -M main
   git remote add origin <your-repo-url>
   git push -u origin main
   ```

2. **Deploy on Vercel:**
   - Go to [vercel.com](https://vercel.com)
   - Click "New Project"
   - Import your GitHub repository
   - Vercel auto-detects Astro settings
   - Click "Deploy"

3. **Done!** Your site is live at `https://your-project.vercel.app`

### Option 2: Vercel CLI

```bash
# Install Vercel CLI
npm install -g vercel

# Login
vercel login

# Deploy
vercel --prod
```

## 🌐 Custom Domain

1. Go to your Vercel project settings
2. Navigate to "Domains"
3. Add your custom domain
4. Update DNS records as instructed
5. Wait for SSL certificate (automatic)

## 📊 Post-Deployment

### Verify Deployment
- [ ] Site loads correctly
- [ ] All links work
- [ ] Mobile responsive
- [ ] Performance is good (< 2s load)

### Monitor
- Enable Vercel Analytics (optional)
- Check Web Vitals
- Monitor error logs

## 🔄 Updates

Every push to `main` branch automatically deploys to production.

For preview deployments, create a pull request.

## 🐛 Troubleshooting

### Build Fails
```bash
# Test build locally
npm run build

# Check for errors
npm run preview
```

### Slow Performance
- Check bundle size
- Optimize images
- Review Lighthouse report

## 📞 Support

- [Vercel Docs](https://vercel.com/docs)
- [Astro Docs](https://docs.astro.build)
- [Project Issues](https://github.com/truongnat/agentic-sdlc/issues)
