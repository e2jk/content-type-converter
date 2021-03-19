import os


class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or "you-will-never-guess"
    PROFILES = {
        "test_profile": {"base_url": "http://myhttpheader.com/", "aa": 1, "bb": 2},
        "second_profile": {
            "base_url": "https://www.whatismybrowser.com/detect/what-http-headers-is-my-browser-sending",
            "aa": 1,
            "bb": 2,
        },
        "third_profile": {
            "base_url": "http://localhost:5555",
            "header_authorization": "key TestingABC",
            "bb": 2,
        },
        "invalid_profile": {"base_url": "http://nonexistent.invalid/"},
    }
