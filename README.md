# Content-Type converter
Convert HTTP POST `Content-Type`, for instance from `application/x-www-form-urlencoded` to `application/json`.


[![Test](https://github.com/e2jk/content-type-converter/workflows/Test/badge.svg)](https://github.com/e2jk/content-type-converter/actions?query=workflow%3ATest)
[![GitHub last commit](https://img.shields.io/github/last-commit/e2jk/content-type-converter.svg)](https://github.com/e2jk/content-type-converter/commits/master)
[![License](https://img.shields.io/github/license/e2jk/content-type-converter)](../../tree/master/LICENSE)

## Setup
```sh
# Install dependencies (including development dependencies)
poetry install

# Setup pre-commit and pre-push hooks
poetry run pre-commit install -t pre-commit
poetry run pre-commit install -t pre-push
```
