# Horo Coach website

Bilingual static Jekyll website, hosted at https://paraita-io.github.io/horo-website/.

## Local preview

With Ruby 3.3 and Bundler installed:

```sh
bundle install
bundle exec jekyll serve --strict_front_matter
```

Open http://localhost:4000/horo-website/. For a production build and link checks:

```sh
bundle exec jekyll build --strict_front_matter
python3 scripts/check_site.py _site
node --check assets/js/site.js
```

## Content and configuration

- `index.md` / `index-fr.md`: value proposition, explicitly illustrative example, sports, coaches, FAQ, download and feedback.
- `get-started.md` / `get-started-fr.md`: first analysis, troubleshooting and post-workout routine.
- `plans*.md`: free and Premium comparison. The daily quota is configured remotely; avoid publishing an unverified fixed number.
- `support*.md`, `privacy-*.md`, `press-kit*.md`: existing support, privacy and press URLs preserved.
- `_config.yml`: canonical host, base path and verified App Store ID/link (6756943315).
- `_layouts/default.html`: canonical, reciprocal language alternates, social metadata, Smart App Banner and application structured data.
- `sitemap.xml`: generated from localized pages. If the domain changes, update `url` and `baseurl` together.
- The project-level `robots.txt` cannot control crawling of github.io's domain root; the sitemap remains usable directly.
- Keep English and French versions in sync, including `lang_alt`. Illustrations must never be labelled as screenshots or actual user feedback.

## Measuring whether this helps

This change adds no analytics service, cookies or collection of health data.
It does not claim to measure installs or retention from a website click.

Before publishing, note the date and baseline App Store Connect figures. After publishing,
compare equivalent periods: product page views, first-time downloads and web referrers.
App engagement/retention must be checked in App Store Connect or in separately designed app
instrumentation; website visits alone cannot establish retention.

Use the getting-started page in conversations with early users. Ask whether they reached
their first analysis and whether they returned after the next workout. The feedback links
open an email draft only; nothing is sent automatically.

For channel attribution, create campaign links in App Store Connect and use the exact
Apple-generated URLs in the corresponding campaign. Do not invent provider tokens or
assume arbitrary UTM parameters measure App Store installs.

## Verification sources

Public App Store listing: https://apps.apple.com/us/app/horo-coach/id6756943315
Developer website linked from that listing: https://paraita-io.github.io/horo-website/
Local iOS code confirms that opening a workout triggers its analysis.
