# Linter

## Black

[Black](https://github.com/psf/black)

## Isort
[Isort](https://github.com/PyCQA/isort)

## Flake8
[Flake8](https://github.com/PyCQA/flake8)

## Mypy
[Mypy](https://github.com/python/mypy)

## Pre-commit
[Pre-commit](https://pre-commit.com/)

??? note "Pre-commit as a linter manager"

    Pre-commit can be treated as a linter manager, it can manage the linters in the project and run them in a batch.

    ```yaml
    repos:
      - repo: https://github.com/pre-commit/pre-commit-hooks
        rev: v4.5.0
        hooks:
          - id: check-toml
          - id: check-yaml
          - id: end-of-file-fixer
          - id: trailing-whitespace
            exclude: .+\.csv
          - id: mixed-line-ending
            args: [--fix=lf]
      - repo: https://github.com/psf/black
        rev: 23.11.0
        hooks:
          - id: black
      - repo: https://github.com/pycqa/isort
        rev: 5.12.0
        hooks:
          - id: isort
            args: ["--profile", "black"]
      - repo: https://github.com/pycqa/flake8
        rev: 6.1.0
        hooks:
          - id: flake8
      - repo: https://github.com/pre-commit/mirrors-mypy
        rev: v1.7.1  # Use the sha / tag you want to point at
        hooks:
          - id: mypy
            args: [--strict, --ignore-missing-imports]
    ```

???+ tip "Pre-commit quick start (with Poetry)"

    - Fellow the `Quick start` in [https://pre-commit.com/](https://pre-commit.com/#quick-start)
    - Run `poetry add pre-commit` to install `pre-commit` into the project
    - Run `pre-commit install` to install the hooks
    - Run `poetry shell` into the created python venv environment
    - Run `pre-commit run -a` to check all the files in the project



## SonarLint
[SonarLint](https://www.sonarsource.com/products/sonarlint/)

## Ruff
[Ruff](https://github.com/astral-sh/ruff)
