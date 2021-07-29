from flask import Flask
from collections import defaultdict

from fetch import count_group, count_official

MARATONUFFS = "6VlO0zus3c"

app = Flask(__name__)

print(" * Loading user counts...")
# usercount = count_group(MARATONUFFS)
usercount = defaultdict(int)

async def do_count_groups():
    global usercount

@app.route("/")
def hello_world():
    return "Hello!"

@app.route("/accs/<user>")
def accs(user):
    global usercount

    official = count_official(user)
    count = official + usercount[user]

    return {'result': {'user':user, 'count': count }, 'status': 'OK'}

@app.route("/accs/")
def accs_():
    return {'result': "NOT_FOUND"}
