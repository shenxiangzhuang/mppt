# Changelog

## [Unreleased]

## [0.7.0] - 2025-04-25

### Added

* add(test): add mutmut pkg by @shenxiangzhuang in [#164](https://github.com/shenxiangzhuang/mppt/pull/164)
* add(doc): sphinx-immaterial theme by @shenxiangzhuang in [#165](https://github.com/shenxiangzhuang/mppt/pull/165)

### Changed

* chore(linting): update Ruff lint configuration by @shenxiangzhuang in [#157](https://github.com/shenxiangzhuang/mppt/pull/157)
* pkg: remove lock file by @shenxiangzhuang in [#158](https://github.com/shenxiangzhuang/mppt/pull/158)
* chore: remove dev container by @shenxiangzhuang in [#161](https://github.com/shenxiangzhuang/mppt/pull/161)

### CI/CD

* ci: uv cache prune by @shenxiangzhuang in [#150](https://github.com/shenxiangzhuang/mppt/pull/150)
* ci(publish): use pypi trusted publisher by @shenxiangzhuang in [#162](https://github.com/shenxiangzhuang/mppt/pull/162)

## [0.6.0] - 2025-03-06

### Added

- CI: add mypy and ruff in test workflow

### Changed

- Linter & formatter: use ruff only, remove isort, black, flake8

## [0.5.0] - 2025-01-03

### Changed

- Use uv to manage the package rather than poetry (#106)
- Drop the support for Python 3.8 (#110)

## [0.4.0] - 2024-06-11

### Added

- Poetry: Add commitizen, a conventional commit tool (#71)
- Add `py.typed` file to support type hinting (#70)
- Add sql linter: SQLFluff (#58)
- Add task runner just (#50)
- Add package management tool uv (#49)
- Add Locust as a load testing tool (#39)

## [0.3.0] - 2023-12-14

### Added

- Add ruff as extra linter and formatter: both in dependency and pre-commit (#31)
- Add more details about the linters and formatters with the resource from Google SRE book
- Add doctest (#34)

## [0.2.0] - 2023-12-01

### Added

- Documentations for all the features (#20)
- Quick sort implementation for hypothesis testing (#22)

### Changed

- Change package management from Rye to Poetry (#15, #19)

### Removed

- Sweep AI App

## [0.1.1] - 2023-08-15

### Changed

- reorg this package template

## [0.1.0] - 2023-08-15

### Added

- add this package template
