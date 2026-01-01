# Knowledge Entry - React Hydration Mismatch in Astro Components

## Document Info
| Field | Value |
|-------|-------|
| ID | KB-2026-01-01-001 |
| Date | 2026-01-01 |
| Author | @DEV |
| Category | Bug Pattern |
| Severity | Medium |
| Auto-Generated | Yes |
| Source Task | TASK-123 |
| Sprint | 1 |
| Project | Landing Page |
| Tags | #react, #astro, #hydration, #ssr, #auto-learned |

---

## Problem / Challenge

### Description
React components in Astro were throwing hydration mismatch errors when using client-side state management. The error appeared only in production builds, not during development.

### Context
- **Platform:** Web
- **Technology:** Astro 4.16, React 18, Tailwind CSS
- **Environment:** Production
- **Affected Components:** Features.astro, Hero.astro

### Symptoms
- Console error: "Hydration failed because the initial UI does not match what was rendered on the server"
- Visual flash of unstyled content (FOUC)
- Interactive elements not responding immediately

### Impact
- **Users Affected:** 100% of visitors
- **Business Impact:** Poor first impression, potential bounce rate increase
- **Technical Impact:** Client-side JavaScript re-rendering entire component

---

## Root Cause Analysis

### What Happened
Astro was server-rendering React components with initial state, but client-side hydration was using different initial values, causing a mismatch.

### Why It Happened
The component was using `Date.now()` for generating unique IDs during SSR, which produced different values during client-side hydration.

### Contributing Factors
- Server and client running at different times
- No stable ID generation strategy
- Missing `client:load` directive specification

### Code/Configuration Example
```jsx
// Problematic code
export default function Features() {
  const [id] = useState(() => `feature-${Date.now()}`);
  return <div id={id}>...</div>;
}
```

---

## Solution

### Approach
Use stable, deterministic IDs that are consistent between server and client rendering.

### Implementation
```jsx
// Fixed code
export default function Features() {
  const [id] = useState('feature-static-id');
  // OR use useId hook in React 18+
  const id = useId();
  return <div id={id}>...</div>;
}
```

### Configuration Changes
```astro
---
// In Astro component, specify hydration strategy
import Features from '../components/Features';
---

<Features client:load />
```

### Steps to Resolve
1. Identify components with dynamic ID generation
2. Replace `Date.now()` or `Math.random()` with stable IDs
3. Use React 18's `useId()` hook for unique IDs
4. Add explicit `client:load` directive in Astro
5. Test in production build mode

### Time to Resolve
- **First Attempt:** 2 hours (tried various hydration strategies)
- **Total Attempts:** 3
- **Final Resolution:** 4 hours

---

## Prevention

### How to Avoid in Future
- Always use stable IDs for SSR components
- Use React 18's `useId()` hook for unique identifiers
- Test production builds before deployment
- Avoid time-based or random values in initial render

### Detection Strategy
- Run `npm run build && npm run preview` before deployment
- Check browser console for hydration warnings
- Add automated tests for SSR/hydration consistency

### Code Review Checklist
- [ ] No `Date.now()` or `Math.random()` in component initialization
- [ ] Using `useId()` for dynamic IDs
- [ ] Explicit hydration directive specified
- [ ] Tested in production build mode

---

## Related Issues

### Similar Bugs/Features
- Hydration issues with conditional rendering
- SSR state management problems

### Related Documentation
- [React 18 Hydration](https://react.dev/reference/react-dom/client/hydrateRoot)
- [Astro Client Directives](https://docs.astro.build/en/reference/directives-reference/#client-directives)

### Related Knowledge Entries
- KB-2026-01-01-002: Astro Island Architecture Best Practices

---

## Lessons Learned

### What Worked Well
- React 18's `useId()` hook solved the problem elegantly
- Production build testing caught the issue before deployment
- Astro's explicit hydration directives provide good control

### What Didn't Work
- Trying to synchronize timestamps between server and client
- Using localStorage to persist IDs (not available during SSR)

### Key Takeaways
1. Always test SSR applications in production mode
2. Avoid non-deterministic values in initial render
3. Use framework-provided solutions (useId) over custom implementations
4. Explicit is better than implicit for hydration strategies

---

## Search Keywords
hydration, mismatch, astro, react, ssr, server-side-rendering, useId, Date.now, production-build, FOUC

---

## Verification

### How to Test
```bash
# Build and preview production
npm run build
npm run preview

# Check browser console for errors
# Look for "Hydration failed" messages
```

### Expected Result
- No hydration warnings in console
- Smooth rendering without FOUC
- Interactive elements work immediately

### Regression Test
- [x] Test case added to prevent recurrence
- [x] Automated test created for SSR consistency

---

## References
- Bug Report: TASK-123
- Pull Request: PR-456
- Documentation: https://docs.astro.build/en/guides/framework-components/
- External Resources: https://react.dev/reference/react/useId

---

#knowledge-base #bug-pattern #react #astro #hydration #ssr #auto-learned #sprint-1

