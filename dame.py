#####################
#    JEU DE DAME    #
#####################

import numpy as np

# le jeu se passe sur les lignes 1 à 10 et colonnes 1 à 10
# les lignes 0 et 11 et les colonnes 0 et 11 utilisées pour l'affichage
n = 12

# class pion:
#     def __init__(self,couleur,emplacement):
#         self.couleur=couleur
#         self.emplacement=emplacement

# sous-programme


def menu():
    # menu simple avec question pour jouer ou non
    select = " "
    print("voulez-vous jouer une partie? (oui/non)")
    select = input(select)
    while (select != "oui" and select != "non"):
        print('veuillez saisir "oui" ou "non"')
        select = input(select)
    return select


def init_damier():
    # mise en forme du damier avec les pions et les indications sur les bordures
    dim = [[" "]*n for i in range(n)]
    tableau = np.array(dim)  # tableau de dimension 12 avec des " "
    for i in range(1, n-1):
        tableau[i][0] = chr(96+i)
        tableau[i][n-1] = chr(96+i)
        tableau[0][i] = i-1
        tableau[n-1][i] = i-1
    for i in range(1, 5):
        tableau[i][range(1+(i % 2), n-1, 2)] = "n"
    for i in range(7, n-1):
        tableau[i][range(1+(i % 2), n-1, 2)] = "b"
    return tableau


def pion_valide_joueur(damier, pion, joueur):
    # Vérifie si le pion pointé est correcte selon le joueur
    if (pion[0] < 1 or pion[0] > 10 or pion[1] < 1 or pion[1] > 10):
        return False
    elif (joueur == 0 and damier[pion[0]][pion[1]] == 'b'):
        return True
    elif (joueur == 1 and damier[pion[0]][pion[1]] == 'n'):
        return True
    else:
        return False


def entrer_coordonnee(cas):
    # Afficher une demande de saisie de coordonnées avec des cas différents selon la situation
    if (cas == 1):
        valeur_entree = input(
            "saisir les coordonnées du pion à déplacer (exemple a6):")
        destination = [int(ord(valeur_entree[0]))-96, int(valeur_entree[1])+1]
    elif (cas == 2):
        valeur_entree = input(
            "coordonnées incorrect, veuillez saisir des coordonnées :")
        destination = [int(ord(valeur_entree[0]))-96, int(valeur_entree[1])+1]
    elif (cas == 3):
        valeur_entree = input(
            "saisir les coordonnées de destination :")
        destination = [int(ord(valeur_entree[0]))-96, int(valeur_entree[1])+1]
    return destination


def deplacement_pion(damier, joueur):
    # l'emplacement de départ et arrivé sont dans le damier
    # l'emplacement d'arrivé est en diagonale de l'emplacement de départ
    depart = entrer_coordonnee(1)
    while (pion_valide_joueur(damier, depart, joueur) == False):
        depart = entrer_coordonnee(2)
    arrive = entrer_coordonnee(3)
    while (damier[arrive[0]][arrive[1]] != " "):
        arrive = entrer_coordonnee(2)

    return 0


    # prog principal
if __name__ == "__main__":
    joueurB = 0
    joueurN = 1
    # selection = menu()
    damier = init_damier()
    print(damier)
    a = deplacement_pion(damier, joueurN)
    print(a)
