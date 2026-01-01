# UI/UX Design Specification - Version 1.0

## Document Info
| Field | Value |
|-------|----------|
| Version | 1.0 |
| Date | 2026-01-01 |
| Author | @UIUX |
| Platform | Web (Desktop + Mobile Responsive) |
| Status | Draft → Auto-Review |
| Sprint | Sprint 1 |
| Design Style | Premium, Modern, Glassmorphism, Dark Mode |

---

## 1. Design Overview

**Target Users:** Developers, Tech Leads, Solo Developers, Development Teams  
**Platform:** Web (Responsive - Mobile First)  
**Design Goals:**
- 🎨 **WOW Factor:** Stunning first impression with premium aesthetics
- 🚀 **Conversion:** Clear CTAs, easy installation path
- 📱 **Responsive:** Flawless experience on all devices
- ♿ **Accessible:** WCAG 2.1 AA compliant
- ⚡ **Performance:** Smooth 60fps animations, fast load times

**Design Philosophy:**
> "Premium, not MVP. Dynamic, not static. Accessible, not exclusive."

---

## 2. User Personas

### Persona 1: Solo Developer (Primary)
| Attribute | Details |
|-----------|---------|
| **Role** | Full-stack Developer, Indie Hacker |
| **Age Range** | 25-35 |
| **Goals** | Build projects faster, automate repetitive tasks, improve code quality |
| **Pain Points** | Wearing too many hats, context switching, forgetting best practices |
| **Tech Savviness** | High (uses Cursor, GitHub Copilot, modern tools) |
| **Platform Usage** | Desktop (primary), Mobile (docs) |

### Persona 2: Tech Lead (Secondary)
| Attribute | Details |
|-----------|---------|
| **Role** | Engineering Manager, Team Lead |
| **Age Range** | 30-45 |
| **Goals** | Standardize team workflows, ensure quality, reduce onboarding time |
| **Pain Points** | Inconsistent processes, knowledge silos, manual reviews |
| **Tech Savviness** | High |
| **Platform Usage** | Desktop |

---

## 3. User Flows

### Flow 1: First-Time Visitor → Installation
```
┌──────────────┐    ┌──────────────┐    ┌──────────────┐    ┌──────────────┐
│ Land on Hero │───▶│ Scroll to    │───▶│ See Demo     │───▶│ Click "Get   │
│ (Impressed)  │    │ Features     │    │ (Convinced)  │    │ Started" CTA │
└──────────────┘    └──────────────┘    └──────────────┘    └──────┬───────┘
                                                                    │
                                                                    ▼
┌──────────────┐    ┌──────────────┐    ┌──────────────┐    ┌──────────────┐
│ Success!     │◀───│ Follow       │◀───│ Copy Install │◀───│ Jump to      │
│ (Using it)   │    │ Instructions │    │ Command      │    │ Quick Start  │
└──────────────┘    └──────────────┘    └──────────────┘    └──────────────┘
```

### Flow 2: Returning Visitor → Documentation
```
┌──────────────┐    ┌──────────────┐    ┌──────────────┐
│ Direct Link  │───▶│ Quick Scan   │───▶│ Find Info    │
│ from GitHub  │    │ Sections     │    │ (Docs Link)  │
└──────────────┘    └──────────────┘    └──────────────┘
```

---

## 4. Screen/Interface Specifications

### 4.1 Hero Section (Above the Fold)

**Layout:**
```
┌────────────────────────────────────────────────────────────────┐
│                        [Gradient Background]                    │
│                                                                 │
│                    ┌─────────────────────┐                     │
│                    │   Agentic SDLC      │ (Logo + Title)      │
│                    └─────────────────────┘                     │
│                                                                 │
│              Transform Your IDE Into a Full                     │
│                    SDLC Team with AI                           │
│                                                                 │
│        12 Specialized Roles • Automated Workflows •            │
│                  Knowledge Management                           │
│                                                                 │
│         ┌──────────────┐      ┌──────────────┐                │
│         │ Get Started  │      │  View Demo   │                │
│         │  (Primary)   │      │ (Secondary)  │                │
│         └──────────────┘      └──────────────┘                │
│                                                                 │
│              $ npm install -g agentic-sdlc                     │
│              [Copy button with animation]                       │
│                                                                 │
└────────────────────────────────────────────────────────────────┘
```

**Specifications:**
| Element | Specification |
|---------|---------------|
| **Container** | Max-width: 1200px, Padding: 80px 24px, Min-height: 100vh |
| **Title (H1)** | Font: Space Grotesk 700, Size: 64px (mobile: 40px), Color: White |
| **Subtitle** | Font: Inter 400, Size: 24px (mobile: 18px), Color: rgba(255,255,255,0.9) |
| **Background** | Gradient: Purple (#8B5CF6) → Blue (#3B82F6) → Pink (#EC4899), Animated mesh |
| **CTA Buttons** | Height: 56px, Padding: 16px 32px, Border-radius: 12px |
| **Code Block** | Font: Fira Code, Size: 16px, Background: rgba(0,0,0,0.3), Glassmorphism |

**States:**
- **CTA Primary (Get Started):**
  - Default: Solid white bg, purple text, shadow
  - Hover: Scale 1.05, glow effect
  - Active: Scale 0.98
- **CTA Secondary (View Demo):**
  - Default: Glass border, white text
  - Hover: Glass fill, glow
- **Copy Button:**
  - Default: Icon only, subtle
  - Hover: Tooltip "Copy"
  - Clicked: Checkmark, "Copied!"

**Animations:**
- Hero title: Fade up + blur (500ms, ease-out)
- Subtitle: Fade up + blur (600ms, ease-out, delay 100ms)
- CTAs: Fade up + blur (700ms, ease-out, delay 200ms)
- Background: Slow gradient animation (10s loop)

---

### 4.2 Features Section

**Layout:**
```
┌────────────────────────────────────────────────────────────────┐
│                       Why Agentic SDLC?                         │
│                                                                 │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐      │
│  │  [Icon]  │  │  [Icon]  │  │  [Icon]  │  │  [Icon]  │      │
│  │ 12 Roles │  │  Slash   │  │   Auto   │  │ Knowledge│      │
│  │          │  │ Commands │  │ Workflow │  │   Base   │      │
│  │  [Desc]  │  │  [Desc]  │  │  [Desc]  │  │  [Desc]  │      │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘      │
│                                                                 │
│  [4 more cards in second row]                                  │
│                                                                 │
└────────────────────────────────────────────────────────────────┘
```

**Feature Card Specifications:**
| Element | Specification |
|---------|---------------|
| **Card** | Width: 280px, Padding: 32px, Border-radius: 16px |
| **Background** | Glassmorphism: rgba(255,255,255,0.05), backdrop-blur(10px) |
| **Border** | 1px solid rgba(255,255,255,0.1), gradient on hover |
| **Icon** | Size: 48px, Color: Gradient (purple → blue) |
| **Title** | Font: Space Grotesk 600, Size: 20px, Color: White |
| **Description** | Font: Inter 400, Size: 14px, Color: rgba(255,255,255,0.7) |
| **Shadow** | 0 8px 32px rgba(0,0,0,0.2), glow on hover |

**States:**
- Default: Subtle glass effect
- Hover: Border gradient animation, lift (translateY: -8px), glow
- Focus: Visible focus ring

**Grid:**
- Desktop: 4 columns
- Tablet: 2 columns
- Mobile: 1 column

---

### 4.3 How It Works Section

**Layout:**
```
┌────────────────────────────────────────────────────────────────┐
│                      How It Works                               │
│                                                                 │
│  ┌────────────────────────────────────────────────────────┐   │
│  │                                                         │   │
│  │         [SDLC Workflow Diagram - Animated]             │   │
│  │                                                         │   │
│  │   Planning → Design → Dev → Test → Deploy              │   │
│  │      ↓         ↓       ↓      ↓       ↓                │   │
│  │     @PM      @SA     @DEV   @TESTER @DEVOPS            │   │
│  │                                                         │   │
│  └────────────────────────────────────────────────────────┘   │
│                                                                 │
│  ┌──────────────────────────────────────────────────────────┐ │
│  │ Step 1: Install                                          │ │
│  │ Step 2: Initialize                                       │ │
│  │ Step 3: Use Slash Commands                              │ │
│  └──────────────────────────────────────────────────────────┘ │
└────────────────────────────────────────────────────────────────┘
```

**Workflow Diagram:**
- Animated flow with glowing connections
- Each phase highlights on scroll
- Role icons appear with stagger animation

---

### 4.4 Live Demo Section (Interactive Island)

**Layout:**
```
┌────────────────────────────────────────────────────────────────┐
│                      See It In Action                           │
│                                                                 │
│  ┌────────────────────────────────────────────────────────┐   │
│  │  $ npm install -g agentic-sdlc                         │   │
│  │  ✓ Installed successfully                              │   │
│  │                                                         │   │
│  │  $ agentic-sdlc create my-app                          │   │
│  │  ✓ Project created                                     │   │
│  │                                                         │   │
│  │  $ cd my-app && /pm Build a todo app                   │   │
│  │  🤖 PM: Creating project plan...                       │   │
│  │  ✓ Plan created: docs/sprints/sprint-1/plans/...      │   │
│  │  [Typing animation continues...]                       │   │
│  └────────────────────────────────────────────────────────┘   │
│                                                                 │
└────────────────────────────────────────────────────────────────┘
```

**Terminal Specifications:**
| Element | Specification |
|---------|---------------|
| **Container** | Background: #1E1E1E (VS Code dark), Border-radius: 12px |
| **Font** | Fira Code, Size: 14px, Line-height: 1.6 |
| **Colors** | Prompt: #4EC9B0, Success: #4EC9B0, Error: #F48771, Command: #DCDCAA |
| **Cursor** | Blinking white block, 500ms interval |
| **Animation** | Typing effect: 50ms per character, realistic pauses |

---

### 4.5 Quick Start Section

**Layout:**
```
┌────────────────────────────────────────────────────────────────┐
│                       Quick Start                               │
│                                                                 │
│  ┌──────────────────────────────────────────────────────────┐ │
│  │  # Install                                               │ │
│  │  npm install -g agentic-sdlc              [Copy]        │ │
│  └──────────────────────────────────────────────────────────┘ │
│                                                                 │
│  ┌──────────────────────────────────────────────────────────┐ │
│  │  # Create project                                        │ │
│  │  agentic-sdlc create my-project           [Copy]        │ │
│  └──────────────────────────────────────────────────────────┘ │
│                                                                 │
│  ┌──────────────────────────────────────────────────────────┐ │
│  │  # Setup IDE                                             │ │
│  │  agentic-sdlc ide cursor                  [Copy]        │ │
│  └──────────────────────────────────────────────────────────┘ │
│                                                                 │
└────────────────────────────────────────────────────────────────┘
```

**Code Block Specifications:**
- Syntax highlighting with Shiki (server-side)
- Copy button on hover
- Success feedback on copy

---

### 4.6 Tech Stack Section

**Layout:**
```
┌────────────────────────────────────────────────────────────────┐
│                    Supported IDEs & Platforms                   │
│                                                                 │
│  ┌────────┐  ┌────────┐  ┌────────┐  ┌────────┐  ┌────────┐  │
│  │[Cursor]│  │[Copilot│  │[Windsurf│  │[Cline] │  │[Aider] │  │
│  │  Logo  │  │  Logo] │  │  Logo] │  │  Logo] │  │  Logo] │  │
│  └────────┘  └────────┘  └────────┘  └────────┘  └────────┘  │
│                                                                 │
│  ┌────────┐  ┌────────┐  ┌────────┐  ┌────────┐              │
│  │  Web   │  │ Mobile │  │Desktop │  │  CLI   │              │
│  └────────┘  └────────┘  └────────┘  └────────┘              │
│                                                                 │
└────────────────────────────────────────────────────────────────┘
```

**Logo Card:**
- Grayscale by default
- Color + glow on hover
- Smooth transition

---

### 4.7 Stats Section

**Layout:**
```
┌────────────────────────────────────────────────────────────────┐
│                                                                 │
│    ┌──────────┐    ┌──────────┐    ┌──────────┐              │
│    │    12    │    │    16    │    │    5+    │              │
│    │  Roles   │    │Templates │    │   IDEs   │              │
│    └──────────┘    └──────────┘    └──────────┘              │
│                                                                 │
└────────────────────────────────────────────────────────────────┘
```

**Number Animation:**
- Count up animation on scroll into view
- Large numbers: Space Grotesk 700, 72px
- Labels: Inter 400, 16px

---

### 4.8 Footer

**Layout:**
```
┌────────────────────────────────────────────────────────────────┐
│  Agentic SDLC                                                  │
│  Simulating a complete SDLC with AI Agents                     │
│                                                                 │
│  [GitHub]  [NPM]  [Docs]  [License]                           │
│                                                                 │
│  © 2026 truongnat • MIT License                                │
└────────────────────────────────────────────────────────────────┘
```

---

## 5. Design System

### 5.1 Color Palette

| Token | Hex | Usage | Contrast |
|-------|-----|-------|----------|
| `--color-primary` | #8B5CF6 | Primary purple, CTAs | - |
| `--color-secondary` | #3B82F6 | Secondary blue, accents | - |
| `--color-accent` | #EC4899 | Pink accent, highlights | - |
| `--color-success` | #10B981 | Success states, checkmarks | WCAG AA ✓ |
| `--color-warning` | #F59E0B | Warnings | WCAG AA ✓ |
| `--color-error` | #EF4444 | Errors | WCAG AA ✓ |
| `--color-bg-dark` | #0F172A | Background (dark mode) | - |
| `--color-bg-darker` | #020617 | Deeper background | - |
| `--color-text-primary` | #FFFFFF | Primary text (on dark) | WCAG AAA ✓ |
| `--color-text-secondary` | rgba(255,255,255,0.7) | Secondary text | WCAG AA ✓ |
| `--color-text-tertiary` | rgba(255,255,255,0.5) | Tertiary text | - |
| `--color-glass` | rgba(255,255,255,0.05) | Glassmorphism bg | - |
| `--color-glass-border` | rgba(255,255,255,0.1) | Glass borders | - |

**Gradients:**
```css
--gradient-primary: linear-gradient(135deg, #8B5CF6 0%, #3B82F6 50%, #EC4899 100%);
--gradient-hero: radial-gradient(ellipse at top, #8B5CF6, transparent),
                 radial-gradient(ellipse at bottom, #3B82F6, transparent);
--gradient-card-border: linear-gradient(135deg, #8B5CF6, #3B82F6);
```

### 5.2 Typography

| Token | Font | Size (Desktop) | Size (Mobile) | Weight | Line Height | Usage |
|-------|------|----------------|---------------|--------|-------------|-------|
| `--font-display` | Space Grotesk | 64px | 40px | 700 | 1.1 | Hero title |
| `--font-h1` | Space Grotesk | 48px | 32px | 700 | 1.2 | Section titles |
| `--font-h2` | Space Grotesk | 32px | 24px | 600 | 1.3 | Subsections |
| `--font-h3` | Space Grotesk | 24px | 20px | 600 | 1.4 | Card titles |
| `--font-body-lg` | Inter | 20px | 18px | 400 | 1.6 | Hero subtitle |
| `--font-body` | Inter | 16px | 16px | 400 | 1.6 | Body text |
| `--font-body-sm` | Inter | 14px | 14px | 400 | 1.5 | Captions |
| `--font-mono` | Fira Code | 14px | 13px | 400 | 1.6 | Code, terminal |

**Font Loading:**
```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@600;700&family=Inter:wght@400;500;600&family=Fira+Code:wght@400;500&display=swap" rel="stylesheet">
```

### 5.3 Spacing System (8px base)

| Token | Value | Usage |
|-------|-------|-------|
| `--space-1` | 4px | Tight spacing, icon gaps |
| `--space-2` | 8px | Small gaps |
| `--space-3` | 12px | Component padding (small) |
| `--space-4` | 16px | Component padding (medium) |
| `--space-6` | 24px | Component padding (large) |
| `--space-8` | 32px | Section gaps (small) |
| `--space-12` | 48px | Section gaps (medium) |
| `--space-16` | 64px | Section gaps (large) |
| `--space-20` | 80px | Section padding (vertical) |
| `--space-24` | 96px | Large section padding |

### 5.4 Border Radius

| Token | Value | Usage |
|-------|-------|-------|
| `--radius-sm` | 8px | Small elements, badges |
| `--radius-md` | 12px | Buttons, inputs, cards |
| `--radius-lg` | 16px | Large cards, modals |
| `--radius-xl` | 24px | Hero sections |
| `--radius-full` | 9999px | Pills, avatars |

### 5.5 Shadows & Effects

```css
--shadow-sm: 0 2px 8px rgba(0, 0, 0, 0.1);
--shadow-md: 0 4px 16px rgba(0, 0, 0, 0.15);
--shadow-lg: 0 8px 32px rgba(0, 0, 0, 0.2);
--shadow-xl: 0 16px 64px rgba(0, 0, 0, 0.3);

--glow-primary: 0 0 20px rgba(139, 92, 246, 0.5);
--glow-secondary: 0 0 20px rgba(59, 130, 246, 0.5);
--glow-accent: 0 0 20px rgba(236, 72, 153, 0.5);

--blur-sm: blur(4px);
--blur-md: blur(8px);
--blur-lg: blur(16px);
```

### 5.6 Component Library

| Component | Variants | File |
|-----------|----------|------|
| **Button** | Primary, Secondary, Ghost, Icon | `Button.astro` |
| **Card** | Feature, Glass, Elevated | `Card.astro` |
| **Badge** | Role, Status | `Badge.astro` |
| **CodeBlock** | Inline, Block | `CodeBlock.astro` |
| **Icon** | Lucide set | `Icon.astro` |
| **Input** | Text, Search | `Input.astro` |

**Button Specifications:**
```css
/* Primary Button */
.btn-primary {
  background: white;
  color: var(--color-primary);
  padding: 16px 32px;
  border-radius: var(--radius-md);
  font-weight: 600;
  box-shadow: var(--shadow-lg);
  transition: all 200ms ease;
}

.btn-primary:hover {
  transform: scale(1.05);
  box-shadow: var(--shadow-xl), var(--glow-primary);
}

/* Secondary Button (Glass) */
.btn-secondary {
  background: var(--color-glass);
  backdrop-filter: var(--blur-md);
  border: 1px solid var(--color-glass-border);
  color: white;
  /* ... same padding, radius */
}

.btn-secondary:hover {
  background: rgba(255, 255, 255, 0.1);
  border-image: var(--gradient-card-border) 1;
  box-shadow: var(--glow-secondary);
}
```

---

## 6. Responsive/Adaptive Design

### 6.1 Breakpoints

| Breakpoint | Width | Layout Changes |
|------------|-------|----------------|
| **Mobile** | < 640px | Single column, stacked nav, larger touch targets |
| **Tablet** | 640px - 1024px | 2 columns for features, side-by-side CTAs |
| **Desktop** | > 1024px | 4 columns for features, full layout |
| **Wide** | > 1440px | Max-width container, centered |

### 6.2 Mobile Optimizations
- Touch targets: Minimum 44x44px
- Font sizes: Slightly smaller but still readable
- Spacing: Reduced vertical padding
- Navigation: Sticky header with hamburger menu (if needed)
- Hero: Full viewport height on mobile
- Cards: Full width with proper spacing

---

## 7. Interactions & Animations

### 7.1 Page Load Animations
```javascript
// Stagger animation for hero elements
Hero Title:    fade-up + blur-out, 500ms, delay 0ms
Hero Subtitle: fade-up + blur-out, 600ms, delay 100ms
Hero CTAs:     fade-up + blur-out, 700ms, delay 200ms
Hero Code:     fade-up + blur-out, 800ms, delay 300ms
```

### 7.2 Scroll Animations
| Element | Animation | Trigger |
|---------|-----------|---------|
| Section titles | Fade up + blur | Intersection Observer (threshold: 0.2) |
| Feature cards | Stagger fade up | Intersection Observer (stagger: 100ms) |
| Stats numbers | Count up | Intersection Observer (once) |
| Workflow diagram | Progressive reveal | Scroll position |

### 7.3 Micro-interactions
| Interaction | Animation | Duration |
|-------------|-----------|----------|
| Button hover | Scale 1.05 + glow | 200ms |
| Button press | Scale 0.98 | 100ms |
| Card hover | Lift (translateY: -8px) + glow | 300ms |
| Copy button | Icon change + tooltip | 150ms |
| Link hover | Underline slide | 200ms |

### 7.4 View Transitions API
```css
@view-transition {
  navigation: auto;
}

::view-transition-old(root),
::view-transition-new(root) {
  animation-duration: 300ms;
  animation-timing-function: ease-in-out;
}
```

### 7.5 Animation Principles
- **Respect user preferences:**
  ```css
  @media (prefers-reduced-motion: reduce) {
    * {
      animation-duration: 0.01ms !important;
      transition-duration: 0.01ms !important;
    }
  }
  ```
- **60fps target:** Use `transform` and `opacity` only
- **Easing:** `cubic-bezier(0.4, 0, 0.2, 1)` for smooth feel
- **Stagger delays:** 50-100ms for sequential elements

---

## 8. Accessibility Checklist

### Visual Accessibility
- [x] Color contrast ≥ 4.5:1 for text (WCAG AA)
- [x] Color contrast ≥ 3:1 for UI components
- [x] Text resizable up to 200% without loss of content
- [x] No information conveyed by color alone
- [x] Focus indicators visible (2px solid ring, offset 2px)

### Keyboard & Navigation
- [x] All interactive elements keyboard accessible
- [x] Logical tab order (top to bottom, left to right)
- [x] Skip to main content link
- [x] Escape key closes modals/overlays
- [x] Arrow keys for terminal demo navigation

### Screen Reader Support
- [x] All images have descriptive alt text
- [x] ARIA labels for icon-only buttons
- [x] Semantic HTML (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`)
- [x] Heading hierarchy (single `<h1>`, logical `<h2>`-`<h6>`)
- [x] Live regions for dynamic content (terminal demo)

### Forms & Inputs
- [x] Labels properly associated with inputs
- [x] Error messages announced to screen readers
- [x] Required fields indicated

---

## 9. Platform Guidelines Compliance

### Web Best Practices
- [x] Progressive enhancement (works without JS for static content)
- [x] Cross-browser compatibility (Chrome, Firefox, Safari, Edge)
- [x] Responsive design (mobile-first)
- [x] SEO optimized (semantic HTML, meta tags)
- [x] Performance optimized (lazy loading, code splitting)

---

## 10. Assets & Resources

### Required Assets
| Asset | Format | Size | Notes |
|-------|--------|------|-------|
| **Logo** | SVG | Scalable | Light version (white) |
| **Favicon** | ICO + SVG | 16x16, 32x32, 192x192 | Multiple sizes |
| **OG Image** | PNG | 1200x630 | For social sharing |
| **Hero Background** | WebP + fallback | 1920x1080 | Gradient mesh |
| **Role Icons** | SVG (Lucide) | 24x24 | Consistent set |
| **IDE Logos** | SVG | Various | Official logos |

### Design Files
- **Wireframes:** Created in this spec (ASCII art)
- **Component Library:** Defined in Design System section
- **Style Guide:** This document serves as style guide

---

## 11. Open Questions

- [x] @SA: Component architecture supports island hydration? ✅ YES
- [x] @PO: All must-have features covered in design? ✅ YES
- [ ] @DEV: Any concerns about View Transitions API browser support?
- [ ] @QA: Additional accessibility requirements?

---

## 12. Conclusion & Next Step

Design specification complete with:
✅ Premium glassmorphism aesthetic  
✅ Responsive mobile-first design  
✅ WCAG 2.1 AA accessibility  
✅ Performance-optimized animations  
✅ Complete design system  

### Next Step:
- **@QA** - Review for usability and testability ✅ AUTO-TRIGGERED
- **@SECA** - Security review of user flows ✅ AUTO-TRIGGERED
- **@PO** - Validate against acceptance criteria 🔄 IN PROGRESS
- **@SA** - Confirm system design alignment ✅ COMPLETE

#uiux-design #designing #sprint-1
