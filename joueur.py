class Joueur:

    def __init__(self,num_joueur: int, joueur_actif: bool, couleur: int):

        self.nom_joueur = input("Quel est le nom du joueur ? ")
        self.num_joueur = num_joueur
        self.a_joue_au_dernier_tour = True

        self.joueur_actif = joueur_actif

        self.couleur = couleur
