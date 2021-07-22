from flask import Flask
import json

from fetch import list_contests

app = Flask(__name__)

@app.route("/")
def hello_world():
    contests = list_contests("6VlO0zus3c")
    return json.dumps(contests)