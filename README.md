# Horo Coach Website

Static, bilingual marketing website for **Horo Coach** (GitHub Pages compatible, Jekyll markdown pages + shared layout/components).

## Structure

- `_layouts/default.html`: global page shell
- `_includes/site-header.html`: primary navigation + language switcher
- `_includes/site-footer.html`: footer links
- `assets/css/site.css`: design system + responsive UI
- `assets/js/site.js`: mobile nav, fade-in animation, screenshot carousel controls
- `index.md`, `index-fr.md`: landing pages (conversion-focused)
- `press-kit.md`, `press-kit-fr.md`: media resources
- `support*.md`, `privacy-policy*.md`, `privacy-choices*.md`: legal/support pages

## Navigation

Primary menu on all pages:

1. Home
2. Press Kit
3. Support
4. Privacy
5. Privacy Choices

Language switcher is always visible in the header and uses `lang_alt` per page front matter.

## Design System

Defined in `assets/css/site.css`:

- **Typography**: `Manrope` (headings), `DM Sans` (body)
- **Spacing scale**: `--space-1` to `--space-9`
- **Palette**: neutral base + blue/teal/indigo accent gradient
- **Components**: buttons, cards, panels, quick links, prose blocks
- **Effects**: subtle glass nav, soft shadows, lightweight transitions

## Microinteractions

Implemented in `assets/js/site.js`:

- Mobile navigation toggle
- Scroll reveal (`.fade-in` -> `.visible`)
- Horizontal screenshot carousel controls

## Content Maintenance

- Update App Store links (`href="#"`) on landing + CTA sections.
- Replace founder bio placeholder in both press kit pages.
- Replace asset links in press kit pages with real hosted files.
- Keep legal date fields synchronized (`privacy-policy*.md`, `privacy-choices*.md`).

## GitHub Pages Notes

- No backend required.
- Works as static Jekyll pages.
- Keep files at repo root to preserve existing URL structure (`support.html`, `privacy-policy.html`, etc.).
