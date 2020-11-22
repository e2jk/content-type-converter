import requests
from flask import Response, current_app, render_template, request

from app.xwwwformurlencoded2json import bp


@bp.route("/")
def index():
    available_profiles = ""
    for p in current_app.config["PROFILES"]:
        available_profiles += '<li><a href="%s">%s</a></li>' % (p, p)
    return "Please indicate a profile:<br><ul>%s</ul>" % available_profiles


@bp.route("/<profile>", defaults={"path": ""}, methods=["GET", "POST"])
@bp.route("/<profile>/<path:path>", methods=["GET", "POST"])
def profile(profile, path):
    if profile not in current_app.config["PROFILES"]:
        # Invalid profile
        return (
            render_template(
                "xwwwformurlencoded2json/invalid.html",
                title="Invalid profile '%s'" % profile,
            ),
            404,
        )
    base_url = current_app.config["PROFILES"][profile]["base_url"]
    url = f"{base_url}{path}"
    if request.query_string:
        url += "?%s" % request.query_string.decode("utf-8")

    # Perform the request
    if request.method == "GET":
        r = requests.get(url)
    elif request.method == "POST":
        # TODO: handle POST requests' payload
        r = requests.post(url)
    else:
        # TODO: support other HTTP methods
        return (f"Unsupported method {request.method}", 500)

    # Edit the content to make relative links go through our proxy
    base_path = f"/xwwwformurlencoded2json/{profile}/"
    content = r.content.decode("utf-8")  # Bytes to UTF-8 string
    content = content.replace('href="', f'href="{base_path}')
    # Make sure full URL links are not funneled through our proxy
    content = content.replace(f'href="{base_path}http', 'href="http')
    content = content.encode("utf-8")  # Back to bytes

    return Response(content, r.status_code, mimetype=r.headers["Content-Type"])
