from collections import defaultdict
import requests as r
import regex as re
import json
from pprint import pprint
from bs4 import BeautifulSoup as S

def list_registered(contest_id):
    result = r.get(f"https://codeforces.com/group/6VlO0zus3c/contestRegistrants/{contest_id}")

    soup = S(result.text, features="lxml")
    soup = soup.find("table", attrs={'class': 'registrants'})
    links =  soup.find_all("a", href=re.compile(r"^/profile"))
    return [l.text for l in links]


def count_official(user):
    response = r.get(f"https://codeforces.com/api/user.rating?handle={user}")
    data = json.loads(response.text)

    if data['status'] == 'OK':
        payload = data['result']
        return len(payload)
    return 0

def list_contests(group, name=None):
    result = r.get(f"https://codeforces.com/group/{group}/contests")
    soup = S(result.text, features="lxml")

    pattern = re.compile(rf"^/group/{group}/contest/\d+$")

    contests = [c for c in soup.find_all("a", href=pattern)]

    if name:
        contest_name = re.compile(name, re.I)
        contests = [c for c in contests if re.search(contest_name, c.parent.text) ]

    contest_ids = [c['href'].split('/')[-1] for c in contests]

    return contest_ids

def count_group(group, name=None):

    contest_ids = list_contests(group, name)
    usercount = defaultdict(int)

    for contest_id in contest_ids:
        users = list_registered(contest_id)
        for user in users:
            usercount[user] += 1
            
    return usercount



if __name__ == '__main__':
    print("tourist", count_official("tourist"))
    for contest in list_contests("6VlO0zus3c", "MaratonUFFS"):
        print(list_registered(contest))





