# /usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Génération fichier csv from listing
    SIRIUS
    Auteur : CHC
    Date : 2018-10-24
"""


import sys
import csv


def erreur(fichier):
    faute = "Fichier " + fichier + " inexistant."
    usage()
    exit(faute)


def parse_file(entree, sortie):
    try:
        with open(sortie, 'w', newline='') as result:
            try:
                with open(entree, 'r') as source:
                    for line in source:
                        enreg = csv.writer(result, dialect='excel')
                        contenu = (";".join(line.split('/')).lstrip(';')).split(';')
                        enreg.writerow(contenu)
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
