class Joueur:

<<<<<<< HEAD
    def __init__(self, num_joueur: int, actif: bool, couleur: int):
=======
    def __init__(self, num_joueur: int, joueur_actif: bool, couleur: int):

        self.nom_joueur = nom_joueur

        self.a_joue_au_dernier_tour = a_joue_au_dernier_tour

        self.joueur_actif = joueur_actif
>>>>>>> fe4e0bc (pull)

        self.nom_joueur = input("Quel est le nom du joueur ? ")
        self.num_joueur = num_joueur
        self.a_joue_au_dernier_tour = True
        self.actif = actif
        self.couleur = couleur

    def input_joueur (self) :
        input_ok=False
        liste_position=[]
        lettres = ["A", "B", "C", "D", "E", "F", "G", "H"] 
        for x in range(1, 9):
            for y in range(1, 9):
                liste_position = [lettres[x-1] + str(y)]
                
        while input_ok!=True:
            input_joueur=input(f'{self.nom_joueur} place ton pion: ')
            input_joueur_MAJU=input_joueur.upper()
            if input_joueur_MAJU == "Q":
                exit()
            else:
                if len(input_joueur_MAJU)==2:
                    if input_joueur_MAJU in liste_position:
                        input_ok=True
                    else:
                        print('Tu es en dehors de la grille, recommence: ')
                else:
                    print("mauvaise entrer, tu n'as le droit qu'a 2 caracteres, recommence: ")
        return input_joueur_MAJU