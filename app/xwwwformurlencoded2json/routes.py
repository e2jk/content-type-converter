from flask import current_app, render_template

from app.xwwwformurlencoded2json import bp


@bp.route("/")
def index():
    available_profiles = ""
    for p in current_app.config["PROFILES"]:
        available_profiles += '<li><a href="%s">%s</a></li>' % (p, p)
    return "Please indicate a profile:<br><ul>%s</ul>" % available_profiles


@bp.route("/<profile>", methods=["GET", "POST"])
def profile(profile):
    if profile not in current_app.config["PROFILES"]:
        # Invalid profile
        return (
            render_template(
                "xwwwformurlencoded2json/invalid.html",
                title="Invalid profile '%s'" % profile,
            ),
            404,
        )
