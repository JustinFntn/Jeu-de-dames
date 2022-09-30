#####################
#    JEU DE DAME    #
#####################

import numpy as np
import string

# création du damier
# le jeu se passe sur les lignes 1 à 10 et colonnes 1 à 10
# les lignes 0 et 11 et les colonnes 0 et 11 utilisées pour l'affichage
n = 12


def init_damier():
    # mise en forme du damier avec les pions et les indications sur les bordures
    dim = [[" "]*n for i in range(n)]
    tableau = np.array(dim)  # tableau de dimension 12 avec des " "
    for i in range(1, n-1):
        tableau[i][0] = i-1
        tableau[i][n-1] = i-1
        tableau[0][i] = chr(96+i)
        tableau[n-1][i] = chr(96+i)
    for i in range(1, 5):
        tableau[i][range(1+(i % 2), n-1, 2)] = "n"
    for i in range(7, n-1):
        tableau[i][range(1+(i % 2), n-1, 2)] = "b"
    return tableau

# def avancer_pion(lettre, numer):
#     return lettre+numero


if __name__ == "__main__":
    damier = init_damier()
    print(damier)

# print(avancer_pion(3.2, 3.2))
