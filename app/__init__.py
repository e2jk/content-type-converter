from flask import Flask

app = Flask(__name__)
from app import routes  # noqa

__version__ = "0.1.0"
