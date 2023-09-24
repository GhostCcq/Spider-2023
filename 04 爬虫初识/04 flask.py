from flask import Flask
from flask import request
from flask import jsonify
app = Flask(__name__)


@app.route('/index', methods=["GET", "POST"])
def index():
    # user = request.values.get('user')
    # pwd = request.values.get('pwd')
    # province = request.values.get('province')
    # hobby = request.values.get('hobby')
    # gender = request.values.get('gender')
    all = {}
    for v,k in request.values.items():
        all[v] = k
    return jsonify(all)


@app.route('/login')
def login():
    return 'hello login'

app.run(port=8889)