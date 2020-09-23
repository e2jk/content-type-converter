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
