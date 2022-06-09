from flask import Flask, render_template
from git import Repo  # GitPython library (to install: pip install GitPython)

app = Flask(__name__)


# Route for the GitHub webhook

@app.route('/git_update', methods=['POST'])
def git_update():
    repo = Repo('./orbe')
    origin = repo.remotes.origin
    repo.create_head('main',
                     origin.refs.main).set_tracking_branch(origin.refs.main).checkout()
    origin.pull()
    return '', 200

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/primo/')
def index():
    return render_template("primo.html")

@app.route('/secondo/')
def index():
    return render_template("secondo.html")