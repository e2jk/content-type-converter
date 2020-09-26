from app.main import bp


@bp.route("/")
def index():
    return (
        'Available convertors:<ul><li><a href="xwwwformurlencoded2json">'
        "xwwwformurlencoded2json</a></li></ul>"
    )
