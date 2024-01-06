# Packaging a python project.

## 1. Set up virtual environment to work in

```sh
python3 -m venv .venv
source .venv/bin/activate
deactivate # to exit
```

## 2. set up folder structure
```sh
fib
├── fib # main meat code
│   ├── __init__.py 
│   ├── fib.py 
└── tests # test code 
    ├── __init__.py
    └── test_fib.py
```

## 3. add paperwork
```sh
touch README.md # docs here
touch LICENSE # license here
touch pyproject.toml\
touch requirements_dev.txt # dev requirements here
```

## 4. Install dev requirements

```sh
pip install -r requirements_dev.txt
```

## 5. Add tests with pytest
```py

import pytest
from fib.fib import fib

def test_fib_0():
    assert fib(0) == 0
...


```

### Run the tests

```sh
# in root of project
pytest

```

## 6. Configure pyproject.toml file

```toml
[build-system]
requires = ["setuptools"]
build-backend = "setuptools.build_meta"

[project]
name = "fib"
version = "0.1"
dependencies = []

[project.scripts]
fib = "fib:main" # to set up the entry point
```

To make the entry point work, modify init.py

```py
# fib/__init__.py

from .fib import main

```

## 7. Install your package in edit mode

```sh
# in project root
pip install --editable .
```

Test out that it worked
```sh
$ fib 10
55
```

## 8. Code quality and uniformity (linting): flake8, black, isort
```sh

touch .flake8

```

```toml
# .flake8

exclude = ...
per_file_ignores= ...

# to work with black
max-line-length = 88
extend-ignore = E203
```

### Enforce formatting with black and isort

```sh
black fib/
isort fib/

black tests/
isort testst/

# check if linting errors still remain
flake8
```

