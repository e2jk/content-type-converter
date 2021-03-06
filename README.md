# Content-Type converter
Convert HTTP POST `Content-Type`, for instance from `application/x-www-form-urlencoded` to `application/json`.


[![Test](https://github.com/e2jk/content-type-converter/workflows/Test/badge.svg)](https://github.com/e2jk/content-type-converter/actions?query=workflow%3ATest)
[![codecov](https://codecov.io/gh/e2jk/content-type-converter/branch/master/graph/badge.svg)](https://codecov.io/gh/e2jk/content-type-converter)
[![GitHub last commit](https://img.shields.io/github/last-commit/e2jk/content-type-converter.svg)](https://github.com/e2jk/content-type-converter/commits/master)
[![License](https://img.shields.io/github/license/e2jk/content-type-converter)](../../tree/master/LICENSE)

## Setup
```sh
# Install Python on your computer, then install pipx and Poetry
python3 -m pip install --user pipx
python3 -m pipx ensurepath
pipx install poetry

# Install dependencies (including development dependencies)
poetry install

# Setup pre-commit and pre-push hooks
poetry run pre-commit install -t pre-commit
poetry run pre-commit install -t pre-push
```

## Run the app
```sh
# Optionally activate Flask's Debug mode when developing
export FLASK_DEBUG=1

# Run the Flask app
poetry run flask run
```

## Development info
```sh
# Run the test suite
poetry run pytest --cov --cov-report=term --cov-report=html
# The output in HTML form can be found in the `htmlcov` folder

# Update dependencies
poetry update
```
