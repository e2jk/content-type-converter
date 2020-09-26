import os


class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or "you-will-never-guess"
    PROFILES = {
        "test_profile": {"aa": 1, "bb": 2},
        "second_profile": {"aa": 1, "bb": 2},
    }
