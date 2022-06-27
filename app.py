from flask import Flask, render_template
from git import Repo  # GitPython library (to install: pip install GitPython)
from covid import download_nuovi_positivi

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

@app.route('/covid19/', methods=["GET"])
def primo():
    
    nuovi_positivi = download_nuovi_positivi()
    #n_positivi = nuovi_positivi['2020-02-24T18:00:00']
    print(nuovi_positivi['2020-02-24T18:00:00'])

    #giorno = nuovi_positivi[0]
    #n_positivi = nuovi_positivi[0]
    n_positivi = nuovi_positivi['2020-02-24T18:00:00']
    
    return render_template("covid19.html", n_positivi=n_positivi)

@app.route('/secondo/', methods=["GET"])
def secondo():
    return render_template("secondo.html")

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404
