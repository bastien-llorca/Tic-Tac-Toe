
grille=["-","-","-",
        "-","-","-",
        "-","-","-",]
joueur_actuel=""
fin_jeu=False 
gagnant=""

def jouer():
    choix_joueur()
    affichage_grille()
    while fin_jeu==False:
        tour(joueur_actuel)
        verifier_fin_jeu()
        verifier_match_nul()
        joueur_suivant()
        affichage_grille()
    resultat()

def choix_joueur():
    global joueur_actuel
    joueur_actuel= input("Veuillez choisir soit (X), soit (O) :")
    while True :
        joueur_actuel=joueur_actuel.upper()
        if joueur_actuel =="X"  :
            print("Vous avez choisi X. Le joueur 2 aura le 0")
            break
        elif joueur_actuel=="O" :
            print("Vous avez choisi O. Le joueur 2 aura le X")
            break
        else:
            joueur_actuel= input("Veuillez choisir soit (X), soit (O) :")

def affichage_grille():
    print("\n")
    print("-------------")
    print("|", grille[0], "|", grille[1], "|", grille[2], "|     1 | 2 | 3 ")
    print("-------------")
    print("|", grille[3], "|", grille[4], "|", grille[5], "|     4 | 5 | 6")
    print("-------------")
    print("|", grille[6], "|", grille[7], "|", grille[8], "|     7 | 8 | 9 ")
    print("-------------")
    print("\n")

def tour(joueur):
    print("C'est le tour du joueur : ", joueur)
    pos = input("Veullier sélectionner un espace vide sur la grille entre 1 et 9 :")

    valide= False
    while valide==False:
        while pos not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            pos=input("Veuiller sélectionner un espace vide sur la grille entre 1 et 9 :")
        
        pos = int(pos) - 1

        if grille [pos]=="-":
            valide=True
        else:
            print("La position n'est pas entre 1 et 9 :" )
    grille[pos]=joueur
affichage_grille()         

def verifier_fin_jeu():
    global fin_jeu
    global gagnant
    if grille[0]==grille[1]==grille[2] and grille[2]!="-":
        fin_jeu=True
        gagnant=grille[1]
    if grille[3]==grille[4]==grille[5] and grille[4]!="-":
        fin_jeu=True
        gagnant=grille[4]
    if grille[6]==grille[7]==grille[8] and grille[7]!="-":
        fin_jeu=True
        gagnant=grille[7]
    if grille[0]==grille[4]==grille[8] and grille[4]!="-":
        fin_jeu=True
        gagnant=grille[4]
    if grille[2]==grille[4]==grille[6] and grille[4]!="-":
        fin_jeu=True
        gagnant=grille[4]
    if grille[0]==grille[3]==grille[6] and grille[3]!="-":
        fin_jeu=True
        gagnant=grille[3]
    if grille[1]==grille[4]==grille[7] and grille[4]!="-":
        fin_jeu=True
        gagnant=grille[4]
    if grille[2]==grille[5]==grille[8] and grille[5]!="-":
        fin_jeu=True
        gagnant=grille[5]

def verifier_match_nul():
    global fin_jeu
    if "-" not in grille :
        fin_jeu=True

def joueur_suivant ():
    global joueur_actuel
    if joueur_actuel == "X" :
        joueur_actuel = "O" 
    else:
        joueur_actuel = "X"

def resultat():
    if gagnant == "X" or gagnant =="O":
        print("Le joueur :", gagnant,"a gagné")
    else:
        print("Le match est nul")
jouer()
