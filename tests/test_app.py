import pytest

import app
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
    assert b"<h1>Invalid profile &#39;dummy&#39;</h1>" in rv.data
    assert b"This profile does not exist" in rv.data


def test_xwwwformurlencoded2json_get(client, mocker):
    mocker.patch("app.xwwwformurlencoded2json.routes.requests.get")
    client.get("/xwwwformurlencoded2json/test_profile?hello=world&test=1")
    app.xwwwformurlencoded2json.routes.requests.get.assert_called_once_with(
        "http://myhttpheader.com/?hello=world&test=1"
    )


def test_xwwwformurlencoded2json_post(client, mocker):
    mocker.patch("app.xwwwformurlencoded2json.routes.requests.post")
    client.post("/xwwwformurlencoded2json/test_profile?hello=world&test=1")
    app.xwwwformurlencoded2json.routes.requests.post.assert_called_once_with(
        "http://myhttpheader.com/?hello=world&test=1"
    )


def test_xwwwformurlencoded2json_invalid_method(client, mocker):
    # Testing HEAD
    # TODO: should actually return GET's headers without body...
    rv = client.head("/xwwwformurlencoded2json/test_profile?hello=world&test=1")
    assert rv.status_code == 501
    assert b"" == rv.data  # HEAD must have no body
    # Testing PUT which is defined as allowed method but is not supported yet
    rv = client.put("/xwwwformurlencoded2json/test_profile?hello=world&test=1")
    assert rv.status_code == 501
    assert b"Unsupported method PUT" in rv.data
    # Test PATCH which is not an allowed method
    rv = client.patch("/xwwwformurlencoded2json/test_profile?hello=world&test=1")
    assert rv.status_code == 405
    assert (
        b"<title>405 Method Not Allowed</title>\n<h1>Method Not Allowed</h1>\n"
        b"<p>The method is not allowed for the requested URL.</p>" in rv.data
    )
