# System Design Specification - Version 1.0

## Document Info
| Field | Value |
|-------|----------|
| Version | 1.0 |
| Date | 2026-01-01 |
| Author | @SA |
| Project Type | Web (Static Site - Landing Page) |
| Status | Draft → Auto-Review |
| Sprint | Sprint 1 |

---

## 1. Architecture Overview

```
┌──────────────────────────────────────────────────────────────────┐
│                    ASTRO STATIC SITE ARCHITECTURE                │
└──────────────────────────────────────────────────────────────────┘

┌─────────────────┐     ┌──────────────────┐     ┌─────────────────┐
│   Build Time    │────▶│   Static HTML    │────▶│   CDN (Vercel)  │
│   (Astro SSG)   │     │   + Assets       │     │   Edge Network  │
└─────────────────┘     └──────────────────┘     └─────────────────┘
        │                                                  │
        │                                                  ▼
        ▼                                         ┌─────────────────┐
┌─────────────────┐                              │   End Users     │
│  Components:    │                              │   (Browsers)    │
│  - Hero         │                              └─────────────────┘
│  - Features     │
│  - Demo         │
│  - CTA          │
└─────────────────┘

ISLAND ARCHITECTURE (Astro):
┌────────────────────────────────────────────────────────────┐
│  Static HTML (Default - Zero JS)                           │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐    │
│  │   Island 1   │  │   Island 2   │  │   Island 3   │    │
│  │  (Terminal   │  │  (Role       │  │  (Code       │    │
│  │   Demo)      │  │   Explorer)  │  │   Tabs)      │    │
│  │  [Hydrated]  │  │  [Hydrated]  │  │  [Hydrated]  │    │
│  └──────────────┘  └──────────────┘  └──────────────┘    │
└────────────────────────────────────────────────────────────┘
```

**Architecture Pattern:** Jamstack (JavaScript, APIs, Markup)
- **Build Time:** Astro compiles all pages to static HTML
- **Runtime:** Zero JavaScript by default, selective hydration for interactive components
- **Deployment:** Static files served from Vercel Edge Network (CDN)
- **No Backend:** Pure static site, no server-side logic

---

## 2. Technology Stack

| Layer | Technology | Justification |
|-------|------------|---------------|
| **Framework** | Astro 4.x | Best-in-class SSG for SEO, zero JS by default, island architecture |
| **Build Tool** | Vite (built-in) | Fast HMR, optimized builds, modern ESM support |
| **Styling** | Vanilla CSS + CSS Modules | Scoped styles, no runtime overhead, maximum control |
| **Animations** | View Transitions API + CSS | Native browser animations, smooth transitions, no library needed |
| **Interactive Islands** | Vanilla JS (minimal) | Only for terminal demo, role explorer, code tabs |
| **Syntax Highlighting** | Shiki (Astro built-in) | Server-side highlighting, zero runtime JS, 100+ themes |
| **Icons** | Lucide Icons (SVG) | Tree-shakeable, lightweight, consistent design |
| **SEO** | @astrojs/seo | Automatic meta tags, Open Graph, Twitter Cards, JSON-LD |
| **Sitemap** | @astrojs/sitemap | Auto-generated XML sitemap |
| **Image Optimization** | Astro Image | WebP/AVIF conversion, lazy loading, responsive images |
| **Deployment** | Vercel | Edge network, automatic HTTPS, perfect Lighthouse scores |
| **Analytics** | Vercel Analytics | Privacy-friendly, Core Web Vitals tracking |

---

## 3. Component Architecture

### 3.1 Page Structure
```
src/
├── pages/
│   └── index.astro          # Main landing page (single page)
├── components/
│   ├── layout/
│   │   ├── Header.astro     # Navigation, logo
│   │   ├── Footer.astro     # Links, social, license
│   │   └── SEO.astro        # Meta tags, OG, schema
│   ├── sections/
│   │   ├── Hero.astro       # Hero section with CTA
│   │   ├── Features.astro   # 12 roles showcase
│   │   ├── HowItWorks.astro # SDLC workflow diagram
│   │   ├── TechStack.astro  # Supported IDEs/platforms
│   │   ├── QuickStart.astro # Installation commands
│   │   ├── LiveDemo.astro   # Terminal simulation (island)
│   │   ├── Stats.astro      # Metrics (12 roles, 16 templates)
│   │   └── CTA.astro        # Final call-to-action
│   ├── interactive/
│   │   ├── TerminalDemo.astro    # Interactive terminal (client:load)
│   │   ├── RoleExplorer.astro    # Role cards (client:visible)
│   │   └── CodeTabs.astro        # Code examples (client:visible)
│   └── ui/
│       ├── Button.astro     # Reusable button
│       ├── Card.astro       # Feature card
│       ├── Badge.astro      # Role badge
│       └── CodeBlock.astro  # Syntax highlighted code
├── styles/
│   ├── global.css           # CSS variables, resets, utilities
│   ├── animations.css       # Keyframes, transitions
│   └── themes.css           # Dark mode support
└── assets/
    ├── images/              # Generated images (hero, OG)
    └── icons/               # SVG icons
```

### 3.2 Component Hydration Strategy
| Component | Hydration | Rationale |
|-----------|-----------|-----------|
| Header, Footer | None (static) | No interactivity needed |
| Hero, Features, Stats | None (static) | Pure content, CSS animations |
| TerminalDemo | `client:load` | Interactive from start, critical UX |
| RoleExplorer | `client:visible` | Hydrate when scrolled into view |
| CodeTabs | `client:visible` | Hydrate when scrolled into view |

**Hydration Directives:**
- `client:load` - Hydrate immediately on page load
- `client:visible` - Hydrate when component enters viewport
- `client:idle` - Hydrate when browser is idle
- Default (no directive) - Never hydrate, pure HTML

---

## 4. Data Model

### 4.1 Static Data (No Database)
All content is defined in Astro components or TypeScript constants:

```typescript
// src/data/roles.ts
export const roles = [
  {
    id: 'pm',
    name: 'Project Manager',
    icon: 'briefcase',
    description: 'Leads project from start to finish',
    command: '/pm',
    color: '#8B5CF6' // purple
  },
  {
    id: 'sa',
    name: 'System Analyst',
    icon: 'cpu',
    description: 'Designs system architecture',
    command: '/sa',
    color: '#3B82F6' // blue
  },
  // ... 10 more roles
];

// src/data/features.ts
export const features = [
  {
    title: '12 AI Roles',
    description: 'Complete SDLC team simulation',
    icon: 'users',
    stats: '12 specialized agents'
  },
  {
    title: 'Slash Commands',
    description: 'Instant role activation',
    icon: 'terminal',
    stats: '10+ commands'
  },
  // ... more features
];

// src/data/techStack.ts
export const supportedIDEs = [
  { name: 'Cursor', logo: '/icons/cursor.svg', url: 'https://cursor.sh' },
  { name: 'GitHub Copilot', logo: '/icons/copilot.svg', url: '...' },
  // ... more IDEs
];
```

### 4.2 SEO Metadata
```typescript
// src/data/seo.ts
export const seoConfig = {
  title: 'Agentic SDLC - AI-Powered Software Development Lifecycle',
  description: 'Transform your IDE into a full SDLC team with 12 specialized AI roles, automated workflows, and knowledge management. Build faster, smarter.',
  keywords: ['SDLC', 'AI agents', 'automation', 'Cursor', 'GitHub Copilot', 'workflow'],
  ogImage: '/og-image.png',
  twitterCard: 'summary_large_image',
  canonicalUrl: 'https://agentic-sdlc.vercel.app',
  author: 'truongnat',
  schema: {
    '@context': 'https://schema.org',
    '@type': 'SoftwareApplication',
    name: 'Agentic SDLC',
    applicationCategory: 'DeveloperApplication',
    operatingSystem: 'Windows, macOS, Linux',
    // ... more schema
  }
};
```

---

## 5. Routing & Navigation

### 5.1 Single Page Application (SPA)
- **Single Route:** `/` (index.astro)
- **Navigation:** Smooth scroll to sections with anchor links
- **Sections:** 
  - `#hero`
  - `#features`
  - `#how-it-works`
  - `#tech-stack`
  - `#quick-start`
  - `#demo`
  - `#get-started`

### 5.2 Navigation Implementation
```astro
<!-- Header.astro -->
<nav>
  <a href="#features">Features</a>
  <a href="#how-it-works">How It Works</a>
  <a href="#quick-start">Quick Start</a>
  <a href="#demo">Demo</a>
</nav>

<script>
  // Smooth scroll behavior (native CSS)
  // html { scroll-behavior: smooth; }
</script>
```

---

## 6. Performance Optimization

### 6.1 Build-Time Optimizations
| Optimization | Implementation | Impact |
|--------------|----------------|--------|
| **HTML Pre-rendering** | Astro SSG | 100% crawlable, instant FCP |
| **CSS Inlining** | Critical CSS inline | Eliminate render-blocking |
| **Image Optimization** | Astro Image (WebP/AVIF) | 60-80% size reduction |
| **Code Splitting** | Per-island bundles | Only load what's needed |
| **Minification** | Vite production build | Smaller bundle sizes |
| **Tree Shaking** | ES modules | Remove unused code |

### 6.2 Runtime Optimizations
| Optimization | Implementation | Impact |
|--------------|----------------|--------|
| **Lazy Loading** | `loading="lazy"` on images | Faster initial load |
| **Intersection Observer** | `client:visible` islands | Defer non-critical JS |
| **CSS Animations** | GPU-accelerated transforms | 60fps animations |
| **Font Loading** | `font-display: swap` | Prevent FOIT |
| **Resource Hints** | `<link rel="preconnect">` | Faster external resources |

### 6.3 Performance Targets
```
Lighthouse Scores (Target: 100/100/100/100)
├── Performance: 100
│   ├── FCP: < 0.8s
│   ├── LCP: < 1.2s
│   ├── TBT: < 100ms
│   └── CLS: < 0.1
├── Accessibility: 100
│   ├── ARIA labels
│   ├── Keyboard navigation
│   └── Color contrast > 4.5:1
├── Best Practices: 100
│   ├── HTTPS
│   ├── No console errors
│   └── Modern image formats
└── SEO: 100
    ├── Meta tags
    ├── Semantic HTML
    └── Mobile-friendly
```

---

## 7. SEO Implementation

### 7.1 On-Page SEO
```astro
<!-- SEO.astro Component -->
<head>
  <!-- Primary Meta Tags -->
  <title>{title}</title>
  <meta name="title" content={title} />
  <meta name="description" content={description} />
  <meta name="keywords" content={keywords.join(', ')} />
  
  <!-- Open Graph / Facebook -->
  <meta property="og:type" content="website" />
  <meta property="og:url" content={canonicalUrl} />
  <meta property="og:title" content={title} />
  <meta property="og:description" content={description} />
  <meta property="og:image" content={ogImage} />
  
  <!-- Twitter -->
  <meta property="twitter:card" content="summary_large_image" />
  <meta property="twitter:url" content={canonicalUrl} />
  <meta property="twitter:title" content={title} />
  <meta property="twitter:description" content={description} />
  <meta property="twitter:image" content={ogImage} />
  
  <!-- Canonical -->
  <link rel="canonical" href={canonicalUrl} />
  
  <!-- JSON-LD Structured Data -->
  <script type="application/ld+json" set:html={JSON.stringify(schema)} />
</head>
```

### 7.2 Technical SEO
- **Sitemap:** Auto-generated at `/sitemap.xml`
- **Robots.txt:** Allow all crawlers
- **Semantic HTML:** `<header>`, `<nav>`, `<main>`, `<section>`, `<article>`, `<footer>`
- **Heading Hierarchy:** Single `<h1>`, logical `<h2>`-`<h6>`
- **Alt Text:** All images have descriptive alt attributes
- **Mobile-First:** Responsive design, viewport meta tag

---

## 8. Accessibility (WCAG 2.1 AA)

| Requirement | Implementation |
|-------------|----------------|
| **Keyboard Navigation** | All interactive elements focusable, visible focus states |
| **Screen Readers** | ARIA labels, semantic HTML, skip links |
| **Color Contrast** | Minimum 4.5:1 for text, 3:1 for UI components |
| **Focus Management** | Logical tab order, focus trapping in modals |
| **Alternative Text** | Descriptive alt text for all images |
| **Responsive Text** | Readable at 200% zoom |

---

## 9. Interactive Components (Islands)

### 9.1 Terminal Demo Component
```typescript
// TerminalDemo.astro (client:load)
interface Command {
  input: string;
  output: string;
  delay: number;
}

const demoCommands: Command[] = [
  { input: '$ npm install -g agentic-sdlc', output: '✓ Installed successfully', delay: 1000 },
  { input: '$ agentic-sdlc create my-app', output: '✓ Project created', delay: 1500 },
  { input: '$ cd my-app && /pm Build a todo app', output: '🤖 PM: Creating project plan...', delay: 2000 },
];

// Auto-play animation on mount
```

### 9.2 Role Explorer Component
```typescript
// RoleExplorer.astro (client:visible)
// Interactive cards that expand on click to show role details
// Smooth animations, accessible keyboard navigation
```

---

## 10. Deployment Architecture

```
┌─────────────────┐
│   GitHub Repo   │
│   (main branch) │
└────────┬────────┘
         │
         │ git push
         ▼
┌─────────────────┐
│  Vercel Build   │
│  (Astro build)  │
└────────┬────────┘
         │
         │ Deploy
         ▼
┌─────────────────────────────────────┐
│      Vercel Edge Network (CDN)      │
│  ┌─────────┐  ┌─────────┐  ┌──────┐│
│  │ US-East │  │ EU-West │  │ Asia ││
│  └─────────┘  └─────────┘  └──────┘│
└─────────────────────────────────────┘
         │
         ▼
┌─────────────────┐
│   End Users     │
│  (< 100ms RTT)  │
└─────────────────┘
```

**Deployment Flow:**
1. Push to `main` branch
2. Vercel auto-builds with `astro build`
3. Static files deployed to Edge Network
4. Automatic HTTPS, caching, compression

---

## 11. Open Questions

- [x] @UIUX: Color palette and typography confirmed?
- [x] @PO: All must-have features prioritized in backlog?
- [ ] @DEVOPS: Vercel project created and configured?
- [ ] @DEV: Any concerns about Astro island hydration?

---

### Next Step:
- **@QA** - Review design for testability and accessibility ✅ AUTO-TRIGGERED
- **@SECA** - Security review of architecture and dependencies ✅ AUTO-TRIGGERED
- **@UIUX** - Create UI/UX Design Specification (in parallel) 🔄 IN PROGRESS
- **@PO** - Create Product Backlog (in parallel) 🔄 IN PROGRESS

#designing #sprint-1 #sa
