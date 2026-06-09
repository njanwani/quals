# quarto-theme (clean-nav)

A Quarto RevealJS theme for the **Dynamic Mobility Lab**. Derived from
Grant McDermott's [`clean`](https://github.com/grantmcdermott/quarto-revealjs-clean)
theme, extended with a persistent **section sidebar** that shows where you
are in the presentation and highlights the current section.

> **This repo is the extension itself.** Its root contains `_extension.yml`
> and the theme assets — drop it into your project's `_extensions/` tree and
> Quarto will pick it up.

## Install (recommended: git submodule)

From the root of your Quarto presentation:

```bash
git submodule add \
  https://github.com/dynamicmobility/quarto-theme.git \
  _extensions/dynamicmobility/clean-nav
git submodule update --init --recursive
```

That puts the extension at `_extensions/dynamicmobility/clean-nav/` — the
exact path Quarto's `quarto add` would produce. Your presentation pins a
specific commit; to upgrade later:

```bash
git submodule update --remote _extensions/dynamicmobility/clean-nav
```

When a teammate clones your presentation, they pull the theme with:

```bash
git clone --recurse-submodules <your-presentation-url>
# or, if already cloned:
git submodule update --init --recursive
```

## Install (alternative: plain clone)

If you don't want a submodule:

```bash
git clone https://github.com/dynamicmobility/quarto-theme.git \
  _extensions/dynamicmobility/clean-nav
```

## Use

In your `.qmd` frontmatter:

```yaml
---
title: "My Talk"
author: "Your Name"
format:
  clean-nav-revealjs:
    slide-number: "c/t"
    # Optional: point at a project-root nav-sections.js to override sections
    include-in-header:
      - text: |
          <script src="nav-sections.js"></script>
---
```

See [`template.qmd`](template.qmd) for a minimal working example.

## Customizing the nav sidebar

1. Create `nav-sections.js` at your project root:

   ```javascript
   var NAV_SECTIONS = [
     { key: "intro",    label: "Introduction" },
     { key: "methods",  label: "Methods" },
     { key: "results",  label: "Results" },
     { key: "future",   label: "Future Work" },
   ];
   ```

   The `include-in-header` block in your frontmatter loads this *before* the
   extension's sidebar script, so your `NAV_SECTIONS` wins. If you omit the
   file, a generic default is used.

2. Tag each slide heading with `{.nav-<key>}`:

   ```markdown
   ## Background {.nav-intro}
   ## Algorithm {.nav-methods}
   ```

3. To hide the sidebar on a slide (e.g., backup slides), use `{.nav-none}`:

   ```markdown
   ## Backup figures {.nav-none}
   ```

The sidebar auto-hides on the title slide and on `#`-level transition
slides. Slides after a `# Backup` transition are automatically marked
`data-visibility="uncounted"` so they don't affect the slide counter.

## Customizing colors

Edit [`clean-nav.scss`](clean-nav.scss) or override via a project-local
`custom.scss`:

```yaml
format:
  clean-nav-revealjs:
    theme: [default, custom.scss]
```

```scss
/*-- scss:defaults --*/
$accent: #b04a00;
```

Theme variables:
- `$jet`     — base text color (default `#131516`)
- `$accent`  — primary accent (default `#107895`)
- `$accent2` — secondary accent (default `#9a2515`)

## Attribution

- Base theme: [grantmcdermott/quarto-revealjs-clean](https://github.com/grantmcdermott/quarto-revealjs-clean) (MIT)
- Fonts: [Roboto](https://fonts.google.com/specimen/Roboto)
- Math: [MathJax 4](https://www.mathjax.org/)

## License

MIT — see [LICENSE](LICENSE).
