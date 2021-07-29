from flask import Flask
import json
import asyncio
from collections import defaultdict

from fetch import count_group, count_official

MARATONUFFS = "6VlO0zus3c"

app = Flask(__name__)

print(" * Loading user counts...")
usercount = count_group(MARATONUFFS)

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

    return json.dumps({'result': {'user':user, 'count': count }, 'status': 'OK'})
