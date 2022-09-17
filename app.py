from flask import Flask, render_template, request, session, redirect, send_file
from pytube import YouTube
from io import BytesIO

from git import Repo  # GitPython library (to install: pip install GitPython)
from downloadDataCovid import (
    download_nuovi_positivi_ita_csv,
    download_nuovi_positivi_ita_json,
    download_nuovi_positivi_lazio_json,
)


app = Flask(__name__)
app.config[
    "SECRET_KEY"
] = "VoglioAndrare4VolteAlMare@MatteoWoa!!VistoCheSono4VolteCheNonViRiesco"
# Route for the GitHub webhook


@app.route("/git_update", methods=["POST"])
def git_update():
    repo = Repo("./pythonanywhere")
    origin = repo.remotes.origin
    repo.create_head("main", origin.refs.main).set_tracking_branch(
        origin.refs.main
    ).checkout()
    origin.pull()
    return "", 200


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/covid19/", methods=["GET"])
def covid19():
    nuovi_positivi_ita = download_nuovi_positivi_ita_json()
    nuovi_positivi_lazio = download_nuovi_positivi_lazio_json()
    return render_template(
        "/covid19/covid19.html",
        nuovi_positivi_ita=nuovi_positivi_ita,
        nuovi_positivi_lazio=nuovi_positivi_lazio,
    )


@app.route("/ytdown/", methods=["GET", "POST"])
def ytdown():
    yt_url = ""
    if request.method == "POST":
        # print(request.form.get(yt_url))
        return render_template("/ytdown/ytdown_found.html")

    return render_template("/ytdown/ytdown.html")


"""
        try:
            yt_url = YouTube(session["link"])
            yt_url.check_availability()
        except:
            return render_template("/ytdown/ytdown_notfound.html")

        return render_template("/ytdown/ytdown_found.html")
"""


@app.route("/ytdown_found/", methods=["GET", "POST"])
def ytdown_download_video():
    if request.method == "POST":
        buffer = BytesIO()
        yt_url = YouTube(session["link"])
        itag = request.form.get("itag")
        video = yt_url.streams.get_by_itag(itag)
        video.stream_to_buffer(buffer)
        buffer.seek(0)
        return send_file(
            buffer,
            as_attachment=True,
            download_name="Video - YT2Video.mp4",
            mimetype="video/mp4",
        )
    return render_template("/ytdown/ytdown_found.html")


@app.route("/daUtilizzare/", methods=["GET"])
def daUtilizzare():
    return render_template("/daUtilizzare/daUtilizzare.html")


@app.route("/covid19ItaCsv/", methods=["GET"])
def covid19ItaCsv():
    nuovi_positivi = download_nuovi_positivi_ita_csv()
    return render_template("/covid19/covid19ItaCsv.html", nuovi_positivi=nuovi_positivi)


@app.route("/covid19ItaJson/", methods=["GET"])
def covid19ItaJson():
    nuovi_positivi = download_nuovi_positivi_ita_json()
    return render_template(
        "/covid19/covid19ItaJson.html", nuovi_positivi=nuovi_positivi
    )


@app.route("/covid19LazioJson/", methods=["GET"])
def covid19LazioJson():
    nuovi_positivi = download_nuovi_positivi_lazio_json()
    return render_template(
        "/covid19/covid19LazioJson.html", nuovi_positivi=nuovi_positivi
    )


@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
