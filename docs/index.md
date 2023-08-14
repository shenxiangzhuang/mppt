<p align="center" style="font-size:80px; margin:0px 10px 0px 10px">
    <em>MPPT</em>
</p>
<p align="center", style="font-size: 40px">
    <em>A Modern Python Package Template
</em>
</p>

[//]: # (<div align="center">)

[//]: # (  <a href="https://github.com/shenxiangzhuang/pysesd/actions/workflows/test.yaml" target="_blank">)

[//]: # (      <img src="https://github.com/shenxiangzhuang/pysesd/actions/workflows/test.yaml/badge.svg?event=pull_request" alt="Test">)

[//]: # (  </a>)

[//]: # ()
[//]: # (  <a href="https://github.com/shenxiangzhuang/pysesd">)

[//]: # (  <img alt="Documentation" src="https://github.com/shenxiangzhuang/pysesd/actions/workflows/build_docs.yaml/badge.svg"/>)

[//]: # (  </a>)

[//]: # ()
[//]: # (  <a href="#">)

[//]: # (  <img src="https://img.shields.io/badge/Python-3.8, 3.9, 3.10, 3.11-blue">)

[//]: # (  </a>)

[//]: # ()
[//]: # (  <a href="https://pypi.org/project/pysesd" target="_blank">)

[//]: # (      <img src="https://badge.fury.io/py/pysesd.svg" alt="PyPI Package">)

[//]: # (  </a>)

[//]: # (  <a href="https://codecov.io/gh/shenxiangzhuang/pysesd" target="_blank">)

[//]: # (      <img src="https://codecov.io/gh/shenxiangzhuang/pysesd/branch/master/graph/badge.svg" alt="Coverage">)

[//]: # (  </a>)

[//]: # ()
[//]: # (</div>)

# About
A Modern Python Package Template.

# Features
- Rye: Package Management
- MkDocs: Documentation
- Pre-Commit: Linters
- Pytest: Testing
- Codecov: Testing
- Thu pypi source: China pypi source

# Get Started

## Step1: Create a repository by this template
- Create & Clone

## Step2: GitHub Configuration
- Needed in building documentation site: Set the github action can write the repo
  - In the repository: `Setting` -> `Actions` -> `Workflow permissions`: Select `Read and write permissions`
- Needed in package publishing: Set the pypi token `PYPI_API_TOKEN`
  - Login your pypi account: [https://pypi.org/manage/account/](https://pypi.org/manage/account/)
  - In pypi account `Acount Setting` -> `API tokens`: Select `Add API token` to generate the api token and **COPY** it!
  - In the GitHub repository: `Setting` -> `Environments`: Select `New environments` and create an environment named `publish`
  - In the `publish` environment add a secrets named with `PYPI_API_TOKEN` and set the value with the token
- Needed in test coverage report generation: Set the codecov token `CODECOV_TOKEN`
  - Login your codecov account with GitHub: [https://about.codecov.io/](https://about.codecov.io/)
  - In codecov account, select the repository and you'll see a page named `Let's get your repo covered`. Just **COPY** the token here.
  - In the GitHub repository: `Setting` -> `Secrets and variables`: Add a `Repository secrets` named `CODECOV_TOKEN` and set the value with the token

## Step3: Rye installation & Configuration
- Install Rye: [https://rye-up.com/guide/installation/](https://rye-up.com/guide/installation/)
- Run `rye sync --no-lock` to install all the dependencies([without lock](https://rye-up.com/guide/sync/#-no-lock))

## Step4: Pre-Commit Configuration
- Fellow the `Quick start` in [https://pre-commit.com/](https://pre-commit.com/)
  - Because we have already installed the pre-commit by `rye` and have the `.pre-commit-config.yaml` file in our repo,
    so what we ONLY need to do is run `pre-commit install` to install the hooks
- Run `pre-commit run -a` to check all the files in the project
