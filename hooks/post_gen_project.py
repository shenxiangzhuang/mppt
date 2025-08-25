#!/usr/bin/env python3
"""Post-generation hook for cookiecutter template."""

import os
import shutil
import re


def remove_file_or_dir(file_path):
    """Remove file or directory if it exists."""
    if os.path.exists(file_path):
        if os.path.isdir(file_path):
            shutil.rmtree(file_path)
        else:
            os.remove(file_path)


def generate_python_versions(min_version, max_version):
    """Generate list of Python versions between min and max (inclusive)."""
    # Extract major and minor versions
    min_parts = min_version.split(".")
    max_parts = max_version.split(".")

    min_major, min_minor = int(min_parts[0]), int(min_parts[1])
    max_major, max_minor = int(max_parts[0]), int(max_parts[1])

    versions = []

    # For now, assume all versions are 3.x
    if min_major == 3 and max_major == 3:
        for minor in range(min_minor, max_minor + 1):
            versions.append(f"3.{minor}")

    return versions


def update_pyproject_toml():
    """Update pyproject.toml with correct Python version configuration."""
    min_version = "{{ cookiecutter.python_min_version }}"
    max_version = "{{ cookiecutter.python_max_version }}"

    # Generate the list of supported Python versions
    python_versions = generate_python_versions(min_version, max_version)

    # Read the current pyproject.toml
    with open("pyproject.toml", "r") as f:
        content = f.read()

    # Generate classifiers
    classifiers = []
    for version in python_versions:
        classifiers.append(f'    "Programming Language :: Python :: {version}",')

    # Replace the Python version classifiers placeholder
    replacement = "\n".join(classifiers)
    content = content.replace("    # PYTHON_VERSION_CLASSIFIERS_PLACEHOLDER", replacement)

    # Write back the updated content
    with open("pyproject.toml", "w") as f:
        f.write(content)


def main():
    """Remove files/directories based on configuration and fix Python versions."""

    # Update Python version configuration
    update_pyproject_toml()

    # Remove docs if not included
    if "{{ cookiecutter.include_docs }}" == "n":
        remove_file_or_dir("docs")
        remove_file_or_dir("mkdocs.yml")

    # Remove pre-commit config if not included
    if "{{ cookiecutter.include_pre_commit }}" == "n":
        remove_file_or_dir(".pre-commit-config.yaml")

    # Remove GitHub Actions if not included
    if "{{ cookiecutter.include_github_actions }}" == "n":
        remove_file_or_dir(".github")


if __name__ == "__main__":
    main()
