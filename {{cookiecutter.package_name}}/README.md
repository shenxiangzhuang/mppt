# {{ cookiecutter.package_name }}

[![Python](https://img.shields.io/pypi/pyversions/{{ cookiecutter.package_name }}.svg?color=%2334D058)](https://pypi.org/project/{{ cookiecutter.package_name }}/)
[![PyPI](https://img.shields.io/pypi/v/{{ cookiecutter.package_name }}?color=%2334D058&label=pypi%20package)](https://pypi.org/project/{{ cookiecutter.package_name }}/)
[![PyPI Downloads](https://static.pepy.tech/badge/{{ cookiecutter.package_name }})](https://pepy.tech/projects/{{ cookiecutter.package_name }})
[![GitHub License](https://img.shields.io/github/license/{{ cookiecutter.github_username }}/{{ cookiecutter.package_name }})](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.package_name }}/blob/master/LICENSE)

[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Checked with mypy](https://www.mypy-lang.org/static/mypy_badge.svg)](https://mypy-lang.org/)
{%- if cookiecutter.include_pre_commit == "y" %}
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit)
{%- endif %}
{%- if cookiecutter.include_github_actions == "y" %}
{%- if cookiecutter.include_docs == "y" %}
[![Build Docs](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.package_name }}/actions/workflows/build_docs.yaml/badge.svg)](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.package_name }}/actions/workflows/build_docs.yaml)
{%- endif %}
[![Test](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.package_name }}/actions/workflows/test.yaml/badge.svg)](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.package_name }}/actions/workflows/test.yaml)
{%- endif %}
{%- if cookiecutter.include_codecov == "y" %}
[![Codecov](https://codecov.io/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.package_name }}/branch/master/graph/badge.svg)](https://codecov.io/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.package_name }})
{%- endif %}

## About

{{ cookiecutter.project_short_description }}

## Get Started

1. Set up your development environment:

   ```bash
   # Clone your repository
   git clone https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.package_name }}.git
   cd {{ cookiecutter.package_name }}

   # Set up environment using uv
   uv venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate

   # Install development dependencies with uv
   uv sync --all-extras --dev
   {%- if cookiecutter.include_pre_commit == "y" %}

   # Initialize pre-commit hooks
   uv run pre-commit install
   {%- endif %}
   ```

2. Start developing your package by modifying the code structure as needed.

3. Run tests to ensure everything is working correctly:

   ```bash
   uv run pytest
   ```
   {%- if cookiecutter.include_docs == "y" %}

4. Preview documentation locally:

   ```bash
   uv run mkdocs serve
   ```

   Then visit [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser.
   {%- endif %}

For more details on customization options, refer to the documentation.
