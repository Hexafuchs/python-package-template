# :package_description

[![Latest Version on PyPI](https://img.shields.io/pypi/pyversions/:package_name?style=flat-square)](https://pypi.org/project/:package_name)
[![GitHub Tests Action Status](https://img.shields.io/github/actions/workflow/status/hexafuchs/:package_name/run-tests.yml?branch=main&label=tests&style=flat-square)](https://github.com/hexafuchs/:package_name/actions?query=workflow%3Arun-tests+branch%3Amain)
[![GitHub Code Style Action Status](https://img.shields.io/github/actions/workflow/status/hexafuchs/:package_name/fix-python-code-style-issues.yml?branch=main&label=code%20style&style=flat-square)](https://github.com/hexafuchs/:package_name/actions?query=workflow%3A"Fix+Python+code+style+issues"+branch%3Amain)
[![Total Downloads](https://img.shields.io/pypi/dm/:package_name.svg?style=flat-square)](https://pypi.org/project/:package_name)

<!--delete-->
This repo can be used to scaffold a Python package. Unless you are a member of Hexafuchs, please use the
[Original Template by Microsoft](https://github.com/microsoft/python-package-template).

Follow these steps to get started:

1. Press the "Use this template" button at the top of this repo to create a new repo with the contents of this skeleton.
2. Run "php ./configure.php" to run a script that will replace all placeholders throughout all the files.
3. Have fun creating your package.

Note: Remember to activate discussions and pages in the repository settings. Set pages to workflow.
<!--/delete-->

This is where your description should go. Limit it to a paragraph or two. Consider adding a small example.

## Installation

You can install the package via poetry (or another tool of your choosing):

```bash
poetry add :package_name
```

## Usage

```php
import :package_slug
```

Checkout the docstring or API docs for more usage information.

## Testing

```bash
# All
./venv/bin/pytest -m ""

# Unit
./venv/bin/pytest -m "unit"

# Integration
./venv/bin/pytest -m "integration"

# Unit and Integration
./venv/bin/pytest -m "integration or unit"
```

## Development

### Installing flit and development dependencies

```bash
python3 -m venv venv
./venv/bin/python -m pip install --upgrade pip
./venv/bin/python -m pip install flit
./venv/bin/flit install --only-deps --deps develop
```

### Run linter

```bash
./venv/bin/tox
```

## Create documentation locally

Make sure you have installed the dependencies.
```
cd docs
make clean
make html
```

> You can find the documentation under `docs/_build/html/index.html`

### Installing new dependencies

Either add the dependency to the optional dependencies, or create a new dependency within the `[project]` namespace, e.g.:

```toml
[project]
...
dependencies = [
    "requests==2.32.3"
]
```

Then, install dependencies with flit:

```bash
./venv/bin/flit install --only-deps --deps develop
# or: ./venv/bin/flit install --only-deps --deps all
```

## API Docs

You can find the API Documentation [here](https://hexafuchs.github.io/sharkey-crawler/).

## Changelog

Please see [CHANGELOG](https://github.com/Hexafuchs/:package_name/blob/main/CHANGELOG.md) for more information on what has changed recently.

## License

The MIT License (MIT). Please see [License File](https://github.com/Hexafuchs/:package_name/blob/main/LICENSE.md) for more information.