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
<!--/delete-->

This is where your description should go. Limit it to a paragraph or two. Consider adding a small example.

## Installation

You can install the package via poetry (or another tool of your choosing that is capable to use pyproject.toml):

```bash
poetry add :package_name
```

## Usage

```php
import :package_slug
```

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

## Changelog

Please see [CHANGELOG](CHANGELOG.md) for more information on what has changed recently.

## License

The MIT License (MIT). Please see [License File](LICENSE.md) for more information.