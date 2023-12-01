# Testing


## Pytest
[Pytest](https://docs.pytest.org/en/stable/) is a testing framework for Python.
It is a mature full-featured Python testing tool.


## Hypothesis
[Hypothesis](https://hypothesis.readthedocs.io/en/latest/) is a library for **property based testing**.


## Codecov

[Codecov](https://about.codecov.io/) is a code coverage tool.

Some configurations are needed to use Codecov to generate test coverage report.

!!! tip "Set the codecov token `CODECOV_TOKEN`"

    - Login your codecov account with GitHub: [https://about.codecov.io/](https://about.codecov.io/)
    - In codecov account, select the repository and you'll see a page named `Let's get your repo covered`. Just **COPY** the token here.
    - In the GitHub repository: `Setting` -> `Secrets and variables`: Add a `Repository secrets` named `CODECOV_TOKEN` and set the value with the token
