from collections import defaultdict, Counter
import requests as r
import regex as re
import json
import sys
import pdfkit
import csv
import pickle
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

def load_csv(file):
    with open(file) as csvfile:
        reader = csv.reader(csvfile)
        return list(reader)

def write_csv(data, file):
    with open(file, 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)


def generate_certificate(nome, matricula, horas, template, folder="outputs"):
    x = template.replace("$NOME_ESTUDANTE", nome)
    x = x.replace("$HORAS", str(2*horas))
    x = x.replace("$MATRICULA", str(matricula))

    options = {"enable-local-file-access": ""}

    pdfkit.from_string(x, "{}/{}.pdf".format(folder, nome), options=options)


import typer

app = typer.Typer()


@app.command()
def fetch(pattern: str, dump_horas: str): #
    # pattern = "MaratonUFFS #"

    all_registered = Counter()
    for contest in list_contests("6VlO0zus3c", pattern):
        contest_registered = list_registered(contest)
        lower = [st.lower() for st in contest_registered]
        all_registered.update(lower)

    with open(dump_horas, 'wb') as f :
        counts = dict(all_registered)
        pickle.dump(counts, f)

@app.command()
def show(dump_horas: str): #
    with open(dump_horas, 'rb') as file:
        data_horas = pickle.load(file)
    print(data_horas)

@app.command()
def certificates(dump_horas: str, dados: str, output_folder:str):
    with open("template.html", "r") as f:
        template = f.read()
    data_dados = load_csv(dados)

    with open(dump_horas, 'rb') as file:
        data_horas = pickle.load(file)

    for row in data_dados[1:]:
        [_,matricula,nome,login,horas] = row
        horas = data_horas.get(login)
        if horas:
            generate_certificate(nome, matricula, horas, template, output_folder)


if __name__ == '__main__':
    app()
    # print("tourist", count_official("tourist"))


    



        # generate_certificate(k, v, template)

    #for row in data:
    #    row.append(counts.get(row[3].lower()))

    #write_csv(data, sys.argv[1])




