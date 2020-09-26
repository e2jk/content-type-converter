from app.xwwwformurlencoded2json import bp


@bp.route("/")
def index():
    return "Please indicate a profile"


@bp.route("/<profile>", methods=["GET", "POST"])
def profile(profile):
    return "Hello, World 2!\nProfile: %s" % profile
