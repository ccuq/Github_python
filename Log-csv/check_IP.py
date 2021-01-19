#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    Xxxxxx wxxxxxxxx
    SIRIUS
    Auteur : CHC
    Date : 20XX-XX-XX
"""

import ipaddress


def valid_ip(address):
    try:
        print(ipaddress.ip_address(address))
        return True
    except ValueError:
        return False


# print(valid_ip('10.10.20.30'))
# print(valid_ip('2001:DB8::1'))
# print(valid_ip('gibberish'))
# print(valid_ip('257.0.0.0'))


# import re
# pattern = "^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$"
# match = re.match(pattern, to_check)

import socket

def valid_ip2(address):
    try:
        socket.inet_aton(address)
        return True
    except:
        return False

def valid_ipv4(address):
        host_bytes = address.split('.')
        valid = [int(b) for b in host_bytes]
        valid = [b for b in valid if b >= 0 and b<=255]
        return len(host_bytes) == 4 and len(valid) == 4

# nom de host à partir de l'adresse
host = socket.gethostbyaddr('address')

