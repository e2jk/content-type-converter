from flask import Flask

from config import Config

app = Flask(__name__)
app.config.from_object(Config)

from app import routes  # noqa

__version__ = "0.1.0"
