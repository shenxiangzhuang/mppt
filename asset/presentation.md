---
title: 现代Python应用构建
sub_title: MPPT实践篇
author: Mathew Shen
theme:
  name: dark
  defaults:
    terminal_font_size: 16
---

What
===

## MPPT: A `M`odern `P`ython `P`ackage `T`emplate.
- Check the website for more details: [MPPT](https://datahonor.com/mppt/)

<!-- end_slide -->


Why
===

<!-- pause -->

## 技术债务

"**Technical debt** is the implied cost of future reworking required when choosing
  an **_easy but limited solution_** instead of a better approach that could take more time." -- Wikipedia

- 与金融债务类似，技术债务如果不偿还，会积累“利息”，使得实现变更变得更加困难。
- 未偿还的技术债务会增加软件熵和进一步重做的成本。
- 与金融债务类似，技术债务不一定是坏事，有时（如概念验证（POC））是推动项目前进所必需的。


## Goals


- 提高代码质量
- 降低技术债务积累
- 优化开发体验: 通过类型检查，减少`Runtime Error`, ...
- 提高团队协作效率: Documentation, Code Review, ...
- 降低维护成本: Test, CI/CD, ...

<!-- end_slide -->


How
===

Just do it!
---

<!-- end_slide -->


Environment Setting: Uv & Poetry & Python
---

- Install `uv`: [https://github.com/astral-sh/uv](https://github.com/astral-sh/uv)
  - 这里用`uv`主要是为了利用其cache功能，加速依赖安装
    - 另外其用来创建虚拟环境的功能也很方便
    - 最后是因为其**Cargo for Python**的愿景, 未来可能成为Python依赖管理的事实标准！
- Install `poetry`: [https://python-poetry.org/docs/#installation](https://python-poetry.org/docs/#installation)
- Install Python3.9 in your system: `brew install python@3.9`(for macOS)

检查安装是否成功:
```bash +exec
uv -V
poetry -V
```

```bash +exec
which python3.9
```

<!-- end_slide -->


Project Setting: Project Directory & Venv
---

- Create Project Directory
  - **All** the project files will be under this directory
```bash +exec
mkdir toylib-repo
```


- Create a virtual environment with Python 3.9( [EOL](https://devguide.python.org/versions/)):
```bash +exec
cd toylib-repo
uv venv -p python3.9
```

- Activate the virtual environment
```bash +exec
cd toylib-repo
source .venv/bin/activate
which python
```
<!-- end_slide -->



Project Setting: Poetry init project
---

### Project init
- Run `git init` to create a new git repository(if the project is not under version control)
  - Add `.gitignore` file: [Python.gitignore](https://github.com/github/gitignore/blob/main/Python.gitignore)
- Run `poetry init` to create a new project
  - fill in the project name, description, author, ...
- Change PyPI source to China mirrors


### Project setting
- Add `README.md`
- Add root package directory: `toylib-repo/toylib`, `toylib-repo/toylib/__init__.py`

### Installation
- Run `poetry install` to install all dependencies
- The project itself is installed as editable package

```bash
Installing the current project: toylib (0.1.0)
```

<!-- end_slide -->

Add some code...
---

- Add some demo code in `toylib-repo/toylib/inference.py`

```python
class ModelInference:
    @staticmethod
    def inference(stream_data: list[float]) -> float:
        result = max(stream_data)
        return result


if __name__ == "__main__":
    stream_data = [1.0, 2.0, 3.0, 4.0, 5.0]
    result = ModelInference.inference(stream_data)
    print(result)
```

<!-- pause -->
- Is there any problem with the code?
<!-- pause -->
  - Maybe...


<!-- end_slide -->



Then? Add some unit tests!
---
- Install `pytest` for testing
```bash
poetry add -G test pytest
```

- Add simple tests in `toylib-repo/tests/test_inference_simple.py`
```python
from toylib.inference import ModelInference


def test_model_inference():
    cases = [
        ([1, 2], 2),
        ([3, 1, 2], 3),
        ([2], 2),
    ]
    for case in cases:
        result = ModelInference().inference(case[0])
        assert result == case[1]
```
<!-- end_slide -->


Better unit tests
---

Add test in `toylib-repo/tests/test_inference_better.py`

```python
import pytest
from toylib.inference import ModelInference

EPS = 1e-8


def is_close(x, y):
    return abs(x - y) < EPS


# tip1: use pytest.mark to mark the test case,
# and run the test case with `pytest -m inference tests`
@pytest.mark.inference
# tip2: use pytest.mark.parametrize to parametrize the test case,
# influence the number of test cases
@pytest.mark.parametrize(
    "stream_data,expect_result",
    [([1.0, 2.0], 2.0), ([3.0, 1.0, 2.0], 3.0), ([2.0], 2.0)],
)
def test_model_inference(stream_data, expect_result):
    result = ModelInference().inference(stream_data)
    # tip3: use is_close to compare the float number
    assert is_close(result, expect_result)

```

<!-- end_slide -->


More Better unit tests
---
- Problem: The test cases are not enough, there is a bug in the code, how to find it?
<!-- pause -->
- Solution: Use `Hypothesis`!

<!-- pause -->

- Add library `hypothesis`: `poetry add -G test hypothesis`
- Add test in `toylib-repo/tests/test_inference_property.py`

```python
from toylib.inference import ModelInference
from hypothesis import given
from hypothesis import strategies as st

EPS = 1e-8

def is_close(x, y):
    return abs(x - y) < EPS

# given input is a list of float numbers
@given(st.lists(st.floats()))
def test_inference(stream_data):
    # check the return value is a float number
    assert isinstance(ModelInference().inference(stream_data), float)
```

<!-- pause -->
```bash
E       ValueError: max() arg is an empty sequence
E       Falsifying example: test_inference(
E           stream_data=[],
E       )
```

<!-- end_slide -->


Then? Add linters!
---

- Add `pre-commit` with `ruff`, `black`, `isort`, `mypy` and so on...
  - Install `pre-commit`: `poetry add -G test pre-commit`
  - Add `.pre-commit-config.yaml` file(copy from `crowdlib`)
  - Run `pre-commit install` to install the pre-commit hooks
  - Run `pre-commit run --all-files` to check the code style

- Fix the issues and commit the changes!


<!-- end_slide -->


And Then? Add some docs!
---

## First? Add `mkdocs`!

- Install `mkdocs` with `material` theme
  - `poetry add -G docs mkdocs mkdocs-material`
- MkDocs init: `mkdocs new .`
- Change the `mkdocs.yml` file to use `material` theme
```yaml
site_name: My site
site_url: https://mydomain.org/mysite
theme:
  name: material
```
- Run `mkdocs serve` to preview the docs

<!-- end_slide -->

Some Engineering Practices
===
- Test Coverage
  - `crowdlib`: `make test`

- CHANGELOG & Semantic Versioning
  - [](https://keepachangelog.com/en/1.1.0/)
  - [](https://semver.org/)

- Conventional Commits
  - [](https://www.conventionalcommits.org/en/v1.0.0/)

- Code Review
  - `Viewed`, `Suggestions`, ...
  - [](https://gitlab.leihuo.netease.com/crowdsourcing-algorithm-group/algorithms/crowdlib/-/merge_requests/9)


<!-- end_slide -->

Showcase: `crowdlib`
===
- [](https://crowdlib.apps-sl.danlu.netease.com/)


<!-- end_slide -->

Tools used in this presentation
===
- Presenterm: [](https://github.com/mfontanini/presenterm)
- Wrap: [](https://www.warp.dev/)
- Zed: [](https://zed.dev/)

<!-- end_slide -->


QA
===
