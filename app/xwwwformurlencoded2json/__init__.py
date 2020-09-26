from flask import Blueprint

bp = Blueprint("xwwwformurlencoded2json", __name__)
from app.xwwwformurlencoded2json import routes  # noqa: E402, F401
