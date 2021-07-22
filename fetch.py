import requests as r
import regex as re
from bs4 import BeautifulSoup as S

def list_registered(contest_id):
    result = r.get(f"https://codeforces.com/group/6VlO0zus3c/contestRegistrants/{contest_id}")

    soup = S(result.text, features="lxml")
    links =  soup.find_all("a", href=re.compile(r"^/profile"))
    return [l.text for l in links]


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

if __name__ == '__main__':
    for contest in list_contests("6VlO0zus3c", "MaratonUFFS"):
        print(list_registered(contest))





