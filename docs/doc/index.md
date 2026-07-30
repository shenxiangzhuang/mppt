# Documentation

## Zensical (Recommended)

[Zensical](https://zensical.org/) is a modern static site generator for project
documentation. Documentation is written in Markdown and configured in a native
`zensical.toml` file.

This template intentionally keeps the configuration minimal:

```toml
[project]
site_name = "MPPT"
site_url = "https://shenxiangzhuang.github.io/mppt/"
```

Preview the documentation locally:

```bash
uv run --group docs zensical serve
```

Build the same strict output used by CI:

```bash
uv run --group docs zensical build --clean --strict
```

## GitHub Pages

The documentation workflow builds on pull requests and uploads/deploys the
generated `site/` artifact after changes reach `master`. Configure GitHub Pages
to use **GitHub Actions** as its source before the first deployment.

## Alternatives

### Sphinx

[Sphinx](https://www.sphinx-doc.org/) remains a common choice for projects that
prefer reStructuredText or need its extension ecosystem.
