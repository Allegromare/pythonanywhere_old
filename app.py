from flask import Flask, render_template
from git import Repo  # GitPython library (to install: pip install GitPython)
from downloadDataCovid import download_nuovi_positivi_ita_csv, download_nuovi_positivi_ita_json, download_nuovi_positivi_lazio_json

app = Flask(__name__)

# Route for the GitHub webhook

@app.route('/git_update', methods=['POST'])
def git_update():
    repo = Repo('./pythonanywhere')
    origin = repo.remotes.origin
    repo.create_head('main', origin.refs.main).set_tracking_branch(origin.refs.main).checkout()
    origin.pull()
    return '', 200

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/covid19ItaCsv/', methods=["GET"])
def covid19ItaCsv():
    nuovi_positivi = download_nuovi_positivi_ita_csv()
    return render_template("covid19ItaCsv.html", nuovi_positivi=nuovi_positivi)

@app.route('/covid19ItaJson/', methods=["GET"])
def covid19ItaJson():
    nuovi_positivi = download_nuovi_positivi_ita_json()
    return render_template("covid19ItaJson.html", nuovi_positivi=nuovi_positivi)

@app.route('/covid19LazioJson/', methods=["GET"])
def covid19LazioJson():
    nuovi_positivi = download_nuovi_positivi_lazio_json()
    return render_template("covid19LazioJson.html", nuovi_positivi=nuovi_positivi)

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404