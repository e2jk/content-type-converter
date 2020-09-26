import pytest

from app import app


@pytest.fixture
def client():
    return app.test_client()


def test_root(client):
    """Start with a blank database."""

    rv = client.get("/")
    assert b"Hello, World!" in rv.data
