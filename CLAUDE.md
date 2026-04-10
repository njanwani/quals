# Quals Presentation

Quarto RevealJS presentation using the `clean-revealjs` theme (Grant McDermott's extension).

## Project Structure

- `main.qmd` — Main file that includes all slides and sets format options
- `slides/*.qmd` — Individual slide files, each starting with `##` heading
- `slides/inconsistency/`, `slides/sample-efficiency/` — Nested includes for multi-part slides
- `images/` — All images (PNG, SVG)
- `scripts/` — Python scripts for generating plots (e.g., `discounting_plot.py`)
- `references.bib` — Bibliography; `custom.csl` — Citation style
- `_extensions/grantmcdermott/clean/` — Theme extension

## Styling

- **Main SCSS**: `_extensions/grantmcdermott/clean/clean.scss`
  - Colors: `$jet` (#131516), `$accent` (#107895), `$accent2` (#9a2515)
  - Font: Roboto (imported from Google Fonts)
  - Nav sidebar styles are at the bottom of this file
- **Extension config**: `_extensions/grantmcdermott/clean/_extension.yml`

## Nav Sidebar (Flowchart Outline)

A persistent left-margin flowchart showing presentation sections. Highlights the active section per slide.

### Files
- `nav-sections.js` — **Edit this to add/remove/rename sections.** Each entry: `{ key: "...", label: "..." }`
- `nav-sidebar.html` — Builds the sidebar dynamically from `nav-sections.js` and handles show/hide logic
- Styles in `clean.scss` under `#nav-sidebar`

### How to assign a slide to a section
Add `{.nav-<key>}` to the slide's `##` heading, where `<key>` matches a key in `nav-sections.js`.

Example: `## My Slide Title {.nav-rewards}`

### How to hide the sidebar on a slide
- Add `{.nav-none}` to the heading: `## Backup Slide {.nav-none}`
- Sidebar auto-hides on title slide, `#`-level transition slides, and `.nav-none` slides

### How to change sidebar appearance
Edit `#nav-sidebar` styles in `clean.scss`:
- `font-size` on `.nav-box` — text size (currently 24px)
- `width` on `.nav-box` — box width (currently 130px)
- `padding` on `.nav-box` — inner spacing
- `left` on `#nav-sidebar` — distance from left edge
- `.nav-box.active` — highlighted state (bold, accent color border)
- `.nav-line` — connecting lines between boxes (height, width, color)

## Common Slide Patterns

### Two-column layout
```html
<div style="display: flex; gap: 1em;">
<div style="flex: 1;">
Left content
</div>
<div style="flex: 1;">
Right content
</div>
</div>
```
Adjust `flex` values for different ratios (e.g., `flex: 2` and `flex: 1` for 2:1).

### Images
```
![](images/filename.png){width="60%"}
```

### Centered image
```html
<div style="text-align: center;">
![](images/filename.png){width="60%"}
</div>
```

### Red-colored LaTeX terms
Wrap in `{\color{red}...}` inside LaTeX blocks: `{\color{red}d}`

### Citations
`[@citekey]{style="font-size: 0.6em;"}.`

### Negative top margin (tighten spacing)
`<div style="margin-top: -1em;">` or `<div style="margin-top: -0.5em; margin-bottom: -0.5em;">`

## Building
- Render: `quarto render main.qmd`
- Preview: `quarto preview main.qmd`
- Python plots use the `reward-exploration` conda environment
