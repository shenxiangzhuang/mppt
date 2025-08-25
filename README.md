# MPPT: A Modern Python Package Template

[![Python](https://img.shields.io/pypi/pyversions/mppt.svg?color=%2334D058)](https://pypi.org/project/mppt/)
[![PyPI](https://img.shields.io/pypi/v/mppt?color=%2334D058&label=pypi%20package)](https://pypi.org/project/mppt/)
[![PyPI Downloads](https://static.pepy.tech/badge/mppt)](https://pepy.tech/projects/mppt)
[![GitHub License](https://img.shields.io/github/license/shenxiangzhuang/mppt)](https://github.com/shenxiangzhuang/mppt/blob/master/LICENSE)

[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Checked with mypy](https://www.mypy-lang.org/static/mypy_badge.svg)](https://mypy-lang.org/)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit)
[![Build Docs](https://github.com/shenxiangzhuang/mppt/actions/workflows/build_docs.yaml/badge.svg)](https://github.com/shenxiangzhuang/mppt/actions/workflows/build_docs.yaml)
[![Test](https://github.com/shenxiangzhuang/mppt/actions/workflows/test.yaml/badge.svg)](https://github.com/shenxiangzhuang/mppt/actions/workflows/test.yaml)
[![Codecov](https://codecov.io/gh/shenxiangzhuang/mppt/branch/master/graph/badge.svg)](https://codecov.io/gh/shenxiangzhuang/mppt)

## About

[MPPT](https://github.com/shenxiangzhuang/mppt): A **M**odern **P**ython **P**ackage **T**emplate.

## Get Started

### Option 1: Using Cookiecutter (Recommended)

The easiest way to use this template is with cookiecutter, which will interactively prompt you for all the necessary information:

1. Install cookiecutter:
   ```bash
   pip install cookiecutter
   # or
   uv tool install cookiecutter
   ```

2. Generate your project:
   ```bash
   cookiecutter https://github.com/shenxiangzhuang/mppt.git
   ```

3. Answer the prompts to customize your project:
   - Project name
   - Author information
   - GitHub username
   - Package description
   - Python versions to support
   - Optional features (docs, pre-commit, GitHub Actions, etc.)

4. Navigate to your new project and set up the development environment:
   ```bash
   cd your-project-name
   uv venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   uv sync --all-extras --dev
   ```

### Option 2: Using GitHub Template

Alternatively, you can use this as a GitHub template:

1. Click the "Use this template" button on GitHub or visit [MPPT](https://github.com/shenxiangzhuang/mppt).

2. Replace all instances of MPPT, shenxiangzhuang, and other template-specific details with your own information:
   - Project name, author, and GitHub username in all files
   - GitHub repository links in README.md badges and documentation
   - Package name in pyproject.toml and code files
   - Update LICENSE file with your name and year

3. Set up your development environment:

   ```bash
   # Clone your repository
   git clone https://github.com/your-username/your-project.git
   cd your-project

   # Set up environment using uv
   uv venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate

   # Install development dependencies with uv
   uv sync --all-extras --dev

   # Initialize pre-commit hooks
   uv run pre-commit install
   ```

4. Start developing your package by modifying the code structure as needed.

5. Run tests to ensure everything is working correctly:

   ```bash
   uv run pytest
   ```

6. Preview documentation locally:

   ```bash
   uv run mkdocs serve
   ```

   Then visit [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser.

For more details on customization options, refer to the documentation.
