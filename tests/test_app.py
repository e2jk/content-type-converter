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
    assert (
        b'Available convertors:<ul><li><a href="xwwwformurlencoded2json">'
        b"xwwwformurlencoded2json</a></li></ul>" in rv.data
    )


def test_xwwwformurlencoded2json_root(client):
    rv = client.get("/xwwwformurlencoded2json/")
    assert (
        b'Please indicate a profile:<br><ul><li><a href="test_profile">'
        b'test_profile</a></li><li><a href="second_profile">second_profile</a>'
        b"</li></ul>" in rv.data
    )


def test_xwwwformurlencoded2json_dummy(client):
    rv = client.get("/xwwwformurlencoded2json/dummy")
    assert b"Current profile: dummy" in rv.data
