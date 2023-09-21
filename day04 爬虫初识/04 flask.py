from flask import Flask

app = Flask(__name__)


@app.route('/index')
def index():
    return 'hello index'


@app.route('/login')
def login():
    return 'hello login'

app.run()