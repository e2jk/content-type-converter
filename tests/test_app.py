import pytest

from app import create_app
from config import Config


class TestConfig(Config):
    TESTING = True


@pytest.fixture
def client():
    app = create_app(TestConfig)
    return app.test_client()


def test_root(client):
    rv = client.get("/")
    assert b"Hello, World!" in rv.data


def test_xwwwformurlencoded2json_root(client):
    rv = client.get("/xwwwformurlencoded2json/")
    assert b"Please indicate a profile" in rv.data


def test_xwwwformurlencoded2json_dummy(client):
    rv = client.get("/xwwwformurlencoded2json/dummy")
    assert b"Hello, World 2!\nProfile: dummy" in rv.data
