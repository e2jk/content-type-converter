# Content-Type converter
Convert HTTP POST `Content-Type`, for instance from `application/x-www-form-urlencoded` to `application/json`.

## Setup
```sh
# Install dependencies (including development dependencies)
poetry install

# Setup pre-commit and pre-push hooks
poetry run pre-commit install -t pre-commit
poetry run pre-commit install -t pre-push
```

## Credits
This package was created with Cookiecutter and the [sourcery-ai/python-best-practices-cookiecutter](https://github.com/sourcery-ai/python-best-practices-cookiecutter) project template.
