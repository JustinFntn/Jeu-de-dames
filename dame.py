#####################
#    JEU DE DAME    #
#####################
# le jeu se passe sur les lignes 1 à 10 et colonnes 1 à 10
# les lignes 0 et 11 et les colonnes 0 et 11 utilisées pour l'affichage

import numpy as np
n = 12  # dimension du tableau

############### sous-programme ######################


def menu():
    # =======menu simple avec question pour jouer ou non=======
    select = input("voulez-vous jouer une partie? (oui/non): ")
    while (select != "oui" and select != "non"):
        select = input('veuillez saisir "oui" ou "non": ')
    return select == 'oui'
#####################################


def init_damier():
    # ======mise en forme du damier avec les pions et les indices sur les bordures=======
    dim = [["-"]*n for i in range(n)]
    tableau = np.array(dim)  # tableau de dimension 12 avec des "-"
    tableau[0][0] = "#"
    tableau[0][11] = "#"
    tableau[11][0] = "#"
    tableau[11][11] = "#"
    for i in range(1, n-1):
        tableau[i][0] = chr(96+i)
        tableau[i][n-1] = chr(96+i)
        tableau[0][i] = i-1
        tableau[n-1][i] = i-1
    for i in range(1, 5):
        tableau[i][range(1+(i % 2), n-1, 2)] = "N"
    for i in range(7, n-1):
        tableau[i][range(1+(i % 2), n-1, 2)] = "B"
    return tableau
#####################################


def pion_valide_joueur(damier, pion, joueur):
    # =======Vérifie si le pion pointé est correcte selon le joueur=======
    if (pion[0] < 1 or pion[0] > 10 or pion[1] < 1 or pion[1] > 10):
        return False
    elif ((joueur == 0 and damier[pion[0]][pion[1]] == "B") or (joueur == 1 and damier[pion[0]][pion[1]] == "N")):
        return True
    else:
        return False
#####################################


def deplacement_pion(damier, joueur):
    # =======déplacer un pion selon le joueur=======
    # demande emplacement de départ (vérifie la couleur en fonction du joueur)
    depart = input("saisir les coordonnées du pion à déplacer (exemple a6):")
    depart = [int(ord(depart[0]))-96, int(depart[1])+1]
    while (pion_valide_joueur(damier, depart, joueur) == False):
        depart = input(
            "veuillez saisir un pion correspondant à votre couleur (exemple a6):")
        depart = [int(ord(depart[0]))-96, int(depart[1])+1]

    # demande emplacement de destination (verifie case vide + verifie diag) (prévision de modification pour les pions "dame")
    arrive = input("saisir les coordonnées de destination (exemple a6):")
    arrive = [int(ord(arrive[0]))-96, int(arrive[1])+1]
    case_correcte = False
    while (case_correcte == False):
        if (arrive[0] < 1 or arrive[0] > 10 or arrive[1] < 1 or arrive[1] > 10):
            arrive = input(
                "coordonnées en dehors du damier, veuillez saisir de nouvelles coordonnées (exemple a6):")
            arrive = [int(ord(arrive[0]))-96, int(arrive[1])+1]
        elif (damier[arrive[0]][arrive[1]] != "-"):
            arrive = input(
                "cette case n'est pas vide, veuillez saisir de nouvelles coordonnées (exemple a6):")
            arrive = [int(ord(arrive[0]))-96, int(arrive[1])+1]
        elif ((joueur == 0 and arrive[0] != depart[0]-1 or (arrive[1] != depart[1]+1 and arrive[1] != depart[1]-1)) or (joueur == 1 and arrive[0] != depart[0]+1 or (arrive[1] != depart[1]+1 and arrive[1] != depart[1]-1))):
            arrive = input(
                "soit cette case n'est pas en diagonale, soit vous ne pouvez pas reculer , veuillez saisir de nouvelles coordonnées (exemple a6):")
            arrive = [int(ord(arrive[0]))-96, int(arrive[1])+1]
        else:
            case_correcte = True

    # échange des cases pour le déplacement
    damier[depart[0]][depart[1]] = "-"
    if (joueur == 0):
        damier[arrive[0]][arrive[1]] = "B"
    else:
        damier[arrive[0]][arrive[1]] = "N"
#####################################


def prise_pion(damier, joueur):
    # =======prise de pion======= (prevoir le rajout de prise multiple)
    prise_possible = False
    while (prise_possible == False):
        # entrer des coordonnées de prise et verifier si la prise et possible
        depart = [0, 0]
        while (pion_valide_joueur(damier, depart, joueur) == False):
            depart = input(
                "saisir les coordonnées du pion de prise (exemple a6):")
            depart = [int(ord(depart[0]))-96, int(depart[1])+1]
            if (pion_valide_joueur(damier, depart, joueur) == False):
                print("veuillez saisir un pion de votre couleur")

        pion_elimine = [0, 0]
        while (pion_valide_joueur(damier, pion_elimine, 1-joueur) == False):
            pion_elimine = input(
                "saisir les coordonnées du pion à prendre (exemple a6):")
            pion_elimine = [int(ord(pion_elimine[0]))-96,
                            int(pion_elimine[1])+1]
            if (pion_valide_joueur(damier, pion_elimine, 1-joueur) == False):
                print("veuillez saisir un pion de couleur adverse")

        # verifier que l'arrive pour le piont de prise est correcte
        arrive = [2*pion_elimine[0]-depart[0], 2*pion_elimine[1]-depart[1]]
        print(arrive)
        if ((pion_elimine[0] == depart[0]+1 or pion_elimine[0] == depart[0]-1) and (pion_elimine[1] == depart[1]-1 or pion_elimine[1] == depart[1]+1) and (arrive[0] > 0 and arrive[0] < 11 and arrive[1] > 0 and arrive[1] < 11)):
            if (damier[arrive[0]][arrive[1]] == "-"):
                prise_possible = True
        else:
            print("cette prise n'est pas possible")

    # effectuer les changements sur le damier
    damier[depart[0]][depart[1]] = "-"
    damier[pion_elimine[0]][pion_elimine[1]] = "-"
    if (joueur == 0):
        damier[arrive[0]][arrive[1]] = "B"
    else:
        damier[arrive[0]][arrive[1]] = "N"
#####################################


def prise_possible(damier, joueur):
    # =======verifier si une prise est possible selon le joueur=======
    compteur_prise = 0
    for i in range(1, 11):
        for j in range(1, 11):
            if (joueur == 0 and damier[i][j] == "B"):
                if ((damier[i+1][j+1] == "N" and damier[i+2][j+2] == "-") or (damier[i+1][j-1] == "N" and damier[i+2][j-2] == "-") or (damier[i-1][j+1] == "N" and damier[i-2][j+2] == "-") or (damier[i-1][j-1] == "N" and damier[i-2][j-2] == "-")):
                    print("Une prise possible pour le pion en position", chr(i+96), j-1)
                    compteur_prise += 1
            elif (joueur == 1 and damier[i][j] == "N"):
                if ((damier[i+1][j+1] == "B" and damier[i+2][j+2] == "-") or (damier[i+1][j-1] == "B" and damier[i+2][j-2] == "-") or (damier[i-1][j+1] == "B" and damier[i-2][j+2] == "-") or (damier[i-1][j-1] == "B" and damier[i-2][j-2] == "-")):
                    print("Une prise possible pour le pion en position", chr(i+96), j-1)
                    compteur_prise += 1
    if (compteur_prise != 0):
        print("la prise est obligatoire")
        return True
    else:
        return False
#####################################


def est_finie(damier):
    # =======verifier si la partie est finie======= (return True si un joueur n'a plus de pions mais aussi si il n'y a plus aucun coup possible)
    # verifier si un joueur n'a plus de pion
    # verifier qu'une prise est possible
    if (prise_possible(damier, 0) or prise_possible(damier, 1)):
        return True
    # verifier si un mouvement est encore possible pour l'un des joueurs
####################################


############### programme ######################
if __name__ == "__main__":
    joueur = 0
    tour = 0
    if (menu()):
        damier = init_damier()
        a = True
        damier[5][4]="B"
        damier[5][6]="B"
        while (a != False):
            joueur = tour % 2
            print(damier)
            if (joueur == 0):
                print("tour du joueur blanc")
            else:
                print("tour joueur noir")
            if (prise_possible(damier, joueur)):
                prise_pion(damier, joueur)
            else:
                deplacement_pion(damier, joueur)
            tour += 1
    print("partie terminée")
