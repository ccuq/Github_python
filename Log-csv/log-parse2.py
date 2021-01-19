# /usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Génération fichier csv from listing
    SIRIUS
    Auteur : CHC
    Date : 2018-10-24
"""

import sys


def erreur(fichier):
    faute = "Fichier " + fichier + " inexistant."
    usage()
    exit(faute)


def parse_file(entree, sortie):
    try:
        with open(sortie, 'w') as result:
            try:
                with open(entree, 'r') as source:
                    for line in source:
                        result.write(";".join(line.split('/')).lstrip(';'))
            except FileNotFoundError:
                erreur(entree)
    except FileNotFoundError:
        erreur(sortie)


def usage():
    print("Usage : " + sys.argv[0] + " NomfichierEntree NomFichierSortie")


if __name__ == '__main__':
    if len(sys.argv) > 2:
        parse_file(sys.argv[1], sys.argv[2])
    else:
        usage()
        exit()
