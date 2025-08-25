# {{ cookiecutter.package_name }}

{{ cookiecutter.project_short_description }}

## Installation

```bash
pip install {{ cookiecutter.package_name }}
```

## Quick Start

```python
from {{ cookiecutter.package_name }} import hello

print(hello())
```

## Development

To set up for development:

```bash
git clone https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.package_name }}.git
cd {{ cookiecutter.package_name }}

# Set up environment using uv
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install development dependencies
uv sync --all-extras --dev

# Run tests
uv run pytest
```
