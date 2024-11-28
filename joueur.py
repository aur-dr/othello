
class Joueur:
    def __init__(self, nom_joueur: str, a_joué_au_dernier_tour : bool, joueur_actif: bool, couleur: str):
        self.nom_joueur = nom_joueur
        self.a_joué_au_dernier_tour = a_joué_au_dernier_tour
        self.joueur_actif = joueur_actif
        self.couleur = couleur
    
