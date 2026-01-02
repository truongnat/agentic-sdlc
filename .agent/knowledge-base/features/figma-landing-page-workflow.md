---
title: "Figma Landing Page Design & Development Workflow"
category: feature
priority: high
sprint: research
date: 2026-01-02
tags: [figma, landing-page, design-to-code, tailwind, astro, mcp, ai-workflow]
related_files: [landing-page/src/components/, landing-page/tailwind.config.mjs]
time_saved: "8+ hours per landing page"
---

## Overview

Comprehensive guide for designing landing pages in Figma and converting them to production-ready code using AI tools, MCP (Model Context Protocol), and modern frameworks like Astro + Tailwind CSS.

## Key Learnings from Research

### 1. Figma Landing Page Design Best Practices

**Essential Elements:**
- Clear, compelling headline (first thing visitors see)
- Persuasive subheadings and body copy
- Strong call-to-action (CTA) buttons
- Visual hierarchy to guide attention
- Clean layouts preventing distractions
- Responsive design for all devices

**Canvas Sizes:**
- Desktop: 1920 x 1080px or 1440 x 1024px
- iPhone X: 375 x 812px
- Android: 360 x 640px

**Layout Structure:**
- Use 12-column grid system for consistency
- Apply Auto Layout for responsive behavior
- Organize sections: Header → Hero → Features → CTA → Footer

### 2. Figma File Organization for AI Conversion

**Critical for AI Tools:**
```
✅ Consistent naming conventions (HeaderNavigation, ProductCard, PrimaryButton)
✅ Component hierarchy matching React structure
✅ Reusable components for buttons, forms, headers
✅ Auto Layout configured to mimic CSS flexbox/grid
✅ Design tokens for colors, spacing, typography
✅ Variants for component states (hover, active, disabled)
✅ Accessibility annotations (ARIA labels, tab order)
```

**File Structure:**
```
Figma File
├── Design System Page (components library)
├── Desktop (1440px frames)
├── Tablet (768px frames)
└── Mobile (375px frames)
```

### 3. Design-to-Code Workflow

**8-Step Process:**

1. **Plan** - Define goal (leads, product promo, conversions)
2. **Structure** - Create frame hierarchy with clear information flow
3. **Components** - Build reusable elements for consistency
4. **Optimize** - Refine typography, colors, images, CTAs
5. **Integrate Tools** - Connect Figma to code generation tools
6. **Domain** - Link to custom domain
7. **Test** - Verify responsive design across devices
8. **Publish** - Deploy and promote

### 4. Figma to Tailwind CSS Conversion

**AI Tools Available:**
- **Builder.io Visual Copilot** - Supports multiple frameworks, Tailwind/Emotion/Styled Components
- **Dualite Alpha** - Figma to Tailwind automation
- **QuestAI** - Material UI focused
- **DhiWise** - Full app development automation

**MCP Integration Benefits:**
- Dynamic understanding of component relationships
- Maintains consistency across design system
- Generates code matching team standards
- Reduces manual translation effort

### 5. Figma MCP Tools for Landing Pages

**Available MCP Figma Tools:**
```typescript
// Get design context and generate code
mcp_figma_get_design_context({
  fileKey: "extracted-from-url",
  nodeId: "1:2",
  clientLanguages: "typescript,html,css",
  clientFrameworks: "astro,react"
})

// Get screenshot for reference
mcp_figma_get_screenshot({
  fileKey: "file-key",
  nodeId: "1:2"
})

// Get metadata structure
mcp_figma_get_metadata({
  fileKey: "file-key",
  nodeId: "1:2"
})

// Get design variables/tokens
mcp_figma_get_variable_defs({
  fileKey: "file-key",
  nodeId: "1:2"
})

// Map to code components
mcp_figma_get_code_connect_map({
  fileKey: "file-key",
  nodeId: "1:2"
})
```

### 6. Tailwind vs MUI for Landing Pages

**Tailwind CSS (Recommended for Landing Pages):**
- ✅ Utility-first approach
- ✅ Highly customizable
- ✅ Smaller CSS bundles (purges unused styles)
- ✅ Perfect for unique, custom designs
- ✅ Better performance for static sites
- ⚠️ Steeper learning curve initially

**Material UI (MUI):**
- ✅ Pre-built components
- ✅ Faster initial setup
- ✅ Easier for React developers
- ✅ Material Design consistency
- ⚠️ Larger library size
- ⚠️ Less flexible for custom designs

**For Astro Landing Pages: Use Tailwind CSS**

### 7. Component Patterns for Landing Pages

**Common Components:**
```
landing-page/src/components/
├── Hero.astro           # Main headline + CTA
├── Features.astro       # Feature grid/list
├── UseCases.astro       # Use case examples
├── Testimonials.astro   # Social proof
├── FAQ.astro            # Common questions
├── QuickStart.astro     # Getting started
├── TrustBadges.astro    # Credibility indicators
├── GitHubStats.astro    # Open source metrics
├── Footer.astro         # Links + legal
└── StickyHeaderCTA.astro # Persistent CTA
```

### 8. Figma to Astro + Tailwind Workflow

**Step-by-Step:**

1. **Design in Figma**
   - Use 1440px desktop frame
   - Apply 12-column grid
   - Create component variants
   - Add responsive constraints

2. **Extract Design Tokens**
   ```javascript
   // tailwind.config.mjs
   export default {
     theme: {
       extend: {
         colors: {
           primary: '#...',    // From Figma variables
           secondary: '#...',
         },
         spacing: {
           // From Figma spacing tokens
         }
       }
     }
   }
   ```

3. **Generate Component Code**
   - Use MCP Figma tools or Visual Copilot
   - Convert to Astro components
   - Apply Tailwind classes

4. **Optimize for Production**
   - Lazy load images
   - Optimize fonts
   - Minify CSS/JS
   - Add SEO meta tags

### 9. Accessibility Requirements

**Must-Have Features:**
- Color contrast ratios (WCAG 2.1 AA)
- Keyboard navigation
- ARIA labels for interactive elements
- Focus states clearly visible
- Alt text for images
- Semantic HTML structure
- Screen reader compatibility

### 10. Performance Optimization

**Landing Page Specific:**
- Above-the-fold content loads first
- Lazy load images below fold
- Inline critical CSS
- Preload hero images
- Use WebP/AVIF formats
- Minimize JavaScript
- CDN for static assets

## Implementation for Current Project

**For `landing-page/` directory:**

1. **Create Figma Design System**
   - Extract existing component styles
   - Document in Figma with proper naming
   - Create variants for all states

2. **Setup MCP Figma Integration**
   - Add Figma file URL to project docs
   - Configure Code Connect mappings
   - Link components to source files

3. **Automate Design Updates**
   - Use MCP tools to sync design changes
   - Generate updated Tailwind classes
   - Maintain component consistency

4. **Testing Workflow**
   - Preview in Figma (desktop/tablet/mobile)
   - Test in Astro dev server
   - Verify responsive breakpoints
   - Check accessibility with tools

## Tools & Resources

**Design Tools:**
- [Figma](https://figma.com) - Design platform
- [Landify](https://www.bypeople.com/figma-landing-page-template/) - 500+ components, 170+ blocks
- [Figcomponents](https://www.figcomponents.com) - Free component library
- [Untitled UI](https://www.untitledui.com) - Landing page examples

**Conversion Tools:**
- [Builder.io Visual Copilot](https://www.builder.io) - Figma to code
- [Dualite Alpha](https://dualite.dev) - Figma to Tailwind
- [Detachless](https://detachless.com) - Publish from Figma

**Documentation:**
- [Tailwind CSS Docs](https://tailwindcss.com/docs)
- [Astro Docs](https://docs.astro.build)
- [Figma Best Practices](https://www.geeksforgeeks.org/websites-apps/figma-best-practices/)

## ROI & Time Savings

**Manual Process:**
- Design: 4-6 hours
- Code conversion: 8-12 hours
- Responsive testing: 2-4 hours
- **Total: 14-22 hours**

**AI-Assisted Process:**
- Design: 4-6 hours
- AI conversion: 1-2 hours
- Refinement: 2-3 hours
- Testing: 1-2 hours
- **Total: 8-13 hours**

**Time Saved: 6-9 hours per landing page (40-50% reduction)**

## Best Practices Summary

1. ✅ **Design System First** - Create reusable components
2. ✅ **Consistent Naming** - Match Figma to code conventions
3. ✅ **Mobile-First** - Design for smallest screen first
4. ✅ **Accessibility Built-In** - Not an afterthought
5. ✅ **Performance Focused** - Optimize from the start
6. ✅ **Test Early** - Verify responsive behavior in Figma
7. ✅ **Document Everything** - Comments, annotations, guides
8. ✅ **Version Control** - Track design iterations
9. ✅ **Collaborate** - Designers + developers aligned
10. ✅ **Iterate** - Continuous improvement based on metrics

## Next Steps for Implementation

1. Create Figma file for landing page redesign
2. Setup MCP Figma integration in `.kiro/settings/mcp.json`
3. Document component mapping
4. Test conversion workflow with one component
5. Scale to full landing page
6. Automate with CI/CD pipeline

## Related Patterns

- [Design System Documentation](./design-system-setup.md)
- [Component Library Architecture](../architecture/component-library.md)
- [Performance Optimization](../performance/landing-page-optimization.md)
- [Accessibility Guidelines](../architecture/accessibility-standards.md)

#figma #landing-page #design-to-code #tailwind #astro #mcp #ai-workflow
