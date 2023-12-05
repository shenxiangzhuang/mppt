# Package Management

<center>
![](https://imgs.xkcd.com/comics/python_environment.png)
</center>


## Poetry(Recommended)

[Poetry](https://python-poetry.org/) is a tool for dependency management and packaging in Python.
It allows you to declare the libraries your project depends on, and it will manage (install/update) them for you.

!!! note "Poetry"

    Poetry is a tool for **dependency management** and **packaging** in Python.
    It allows you to declare the libraries your project depends on and it will manage (install/update) them for you.
    Poetry offers a **lockfile** to ensure repeatable installs, and can build your project for distribution.

### Publish to pypi

Some configuration is needed in package publishing

!!! tip "Set the pypi token `PYPI_API_TOKEN`"

    - Login your pypi account: [https://pypi.org/manage/account/](https://pypi.org/manage/account/)
    - In pypi account `Acount Setting` -> `API tokens`: Select `Add API token` to generate the api token and **COPY** it!
    - In the GitHub repository: `Setting` -> `Environments`: Select `New environments` and create an environment named `publish`
    - In the `publish` environment add a secrets named with `PYPI_API_TOKEN` and set the value with the token


## Why Poetry?

### More popular

- Poetry: 27.6k🌟
- Rye: 7.6k🌟
- PDM: 5.6k🌟

!!! note "Date"

    Statistic data collect until 2023-12-01

### Faster

- From the benchmark
  ([Python Package Manager Shootout](https://lincolnloop.github.io/python-package-manager-shootout/)),
  we can see that Poetry is (almost)the fastest package manager.


## Alternatives

### PDM
[PDM](https://pdm.fming.dev/) is a modern Python package manager with PEP 582 support.

!!! note "PDM"

    PDM, as described, is a modern Python package and dependency manager supporting the latest PEP standards.
    But it is more than a package manager. It boosts your development workflow in various aspects.
    The most significant benefit is it installs and **manages packages in a similar way to npm** that doesn't need to
    create a virtualenv at all!

### Rye
[Rye](https://rye-up.com/): An Experimental Package Management Solution for Python.

!!! note "Rye"

    Rye is Armin's personal one-stop-shop for all his Python needs.
    It installs and manages Python installations, helps working with pyproject.toml files,
    installs and uninstalls dependencies, creates and updates virtualenvs behind the scenes.
    It supports monorepos and global tool installations.

    Rye is an experimental endeavour to build a new type of packaging experience to Python **inspired by rustup and cargo
    from Rust**. It's not yet production ready but feedback and suggestions are greatly appreciated.
