from flask import (
    Blueprint, render_template, request
)

from flask import Flask
app = Flask(__name__)

bp = Blueprint('app', __name__)

@bp.route('/', methods=('GET', 'POST'))
def index():
    return render_template('index.html')


app.register_blueprint(bp)
