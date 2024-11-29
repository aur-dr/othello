class Joueur:

    def __init__(self, num_joueur: int, actif: bool, couleur: int):

        self.nom_joueur = input("Quel est le nom du joueur ? ")
        self.num_joueur = num_joueur
        self.a_joue_au_dernier_tour = True
        self.actif = actif
        self.couleur = couleur
        self.input_joueur_MAJU = ""

    def input_joueur (self) :
        input_ok=False
        liste_position=[]
        lettres = ["A", "B", "C", "D", "E", "F", "G", "H"] 
        for x in range(1, 9):
            for y in range(1, 9):
                liste_position = [lettres[x-1] + str(y)]
                
        while input_ok!=True:
            self.input_joueur_MAJU=input(f'{self.nom_joueur} place ton pion: ')
            self.input_joueur_MAJU=self.input_joueur_MAJU.upper()
            if self.input_joueur_MAJU == "Q":
                exit()
            else:
                if len(self.input_joueur_MAJU)==2:
                    if self.input_joueur_MAJU in liste_position:
                        input_ok=True
                    else:
                        print('Tu es en dehors de la grille, recommence : ')
                else:
                    print("Mauvaise entrée, tu n'as le droit qu'à 2 caractères, recommence : ")
        #return input_joueur_MAJU

        