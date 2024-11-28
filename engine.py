# Engine

from pion import Pion
from plateau import Plateau
from joueur import Joueur

class Engine : 
    def __init__(self) :
        self.plateau = Plateau()
        self.joueur1= Joueur(1, True, 1)
        self.joueur2= Joueur(2, False, 2)
            
   
    def trouver_pion_a_retourner(self, grille: list, input_joueur: tuple, Joueur_actif):
        # output : list_de_pion_a_retourner 
        couleur_du_joueur = Joueur_actif.couleur
        adversaire = 1 if couleur_a_chercher == 2 else 2
        list_de_pion_a_retourner = []

        def dans_grille(ligne, col):
            return 0 <= ligne < len(grille) and 0 <= col < len(grille[0])

        def parcours_direction(ligne, col, direction):
            dx, dy = direction
            positions_adversaire = []
            ligne += dx
            col += dy
            while dans_grille(ligne, col):
                if grille[ligne][col] == 0:
                    return []
                elif grille[ligne][col] == adversaire:
                    positions_adversaire.append((ligne, col))
                elif grille[ligne][col] == couleur_du_joueur:
                    if positions_adversaire:
                        return positions_adversaire
                    else:
                        return []
                ligne += dx
                col += dy
            return []

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1),  # haut, bas, gauche, droite
                      (-1, -1), (-1, 1), (1, -1), (1, 1)]  # diagonales

        ligne, col = input_joueur
        if grille[ligne][col] == 0:
            for direction in directions:
                pions_a_retourner = parcours_direction(ligne, col, direction)
                list_de_pion_a_retourner.extend(pions_a_retourner)

        return list_de_pion_a_retourner

       

if __name__ == '__main__':
    engine1= Engine()
    #print(list_pion)
    #for pion in list_pion:
        #print(pion.couleur,pion.coordonnes,pion.position)
    engine1.initialisation_plateau_1_er_tour()



    
    




