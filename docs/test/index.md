# Testing


## Pytest
[Pytest](https://docs.pytest.org/en/stable/) is a testing framework for Python.
It is a mature full-featured Python testing tool.


## Hypothesis
[Hypothesis](https://hypothesis.readthedocs.io/en/latest/) is a library for **property based testing**.


### Testing Statistics
RUN: `pytest --hypothesis-show-statistics tests/test_sort.py`

??? "Testing statistics"

    ```python
    ======================== Hypothesis Statistics =========================
    tests/test_sort.py::TestQuickSort::test_integer:

      - during reuse phase (0.00 seconds):
        - Typical runtimes: < 1ms, of which < 1ms in data generation
        - 2 passing examples, 0 failing examples, 0 invalid examples

      - during generate phase (0.08 seconds):
        - Typical runtimes: < 1ms, of which < 1ms in data generation
        - 98 passing examples, 0 failing examples, 2 invalid examples

      - Stopped because settings.max_examples=100


    tests/test_sort.py::TestQuickSort::test_float:

      - during reuse phase (0.00 seconds):
        - Typical runtimes: < 1ms, of which < 1ms in data generation
        - 2 passing examples, 0 failing examples, 0 invalid examples

      - during generate phase (0.05 seconds):
        - Typical runtimes: < 1ms, of which < 1ms in data generation
        - 98 passing examples, 0 failing examples, 11 invalid examples

      - Stopped because settings.max_examples=100


    tests/test_sort.py::TestQuickSort::test_string:

      - during reuse phase (0.00 seconds):
        - Typical runtimes: < 1ms, of which < 1ms in data generation
        - 3 passing examples, 0 failing examples, 0 invalid examples

      - during generate phase (0.40 seconds):
        - Typical runtimes: ~ 0-2 ms, of which ~ 0-2 ms in data generation
        - 297 passing examples, 0 failing examples, 4 invalid examples

      - Stopped because settings.max_examples=300
    ```


## Codecov

[Codecov](https://about.codecov.io/) is a code coverage tool.

Some configurations are needed to use Codecov to generate test coverage report.

!!! tip "Set the codecov token `CODECOV_TOKEN`"

    - Login your codecov account with GitHub: [https://about.codecov.io/](https://about.codecov.io/)
    - In codecov account, select the repository and you'll see a page named `Let's get your repo covered`. Just **COPY** the token here.
    - In the GitHub repository: `Setting` -> `Secrets and variables`: Add a `Repository secrets` named `CODECOV_TOKEN` and set the value with the token
