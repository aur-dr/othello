# Engine

from pion import Pion
from plateau import Plateau
from joueur import Joueur

class Engine : 
    def __init__(self) :
        self.plateau1 = Plateau()
        self.joueur1= Joueur(1, True, 1)
        self.joueur2= Joueur(2, False, 2)

            

    def trouver_pion_a_retourner(self, plateau: list, input_joueur: tuple, joueur_actif:Joueur): #Règle 
        # Output: list_de_pion_a_retourner 
        couleur_a_chercher = joueur_actif.couleur
        adversaire = 1 if couleur_a_chercher == 2 else 2
        list_de_pion_a_retourner = []

        def dans_grille(ligne, col):
            return 0 <= col < len(plateau) and 0 <= ligne < len(plateau[0])

        def parcours_direction(ligne, col, direction):
            dy, dx = direction
            positions_adversaire = []
            ligne += dx
            col += dy
            while dans_grille(ligne, col):
                if plateau[ligne][col] == 0:
                    return []
                elif plateau[ligne][col] == adversaire:
                    positions_adversaire.append((ligne, col))
                elif plateau[ligne][col] == couleur_a_chercher:
                    if positions_adversaire:
                        return positions_adversaire
                    else:
                        return []
                ligne += dx
                col += dy
            return []

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1),  # haut, bas, gauche, droite
                      (-1, -1), (-1, 1), (1, -1), (1, 1)]  # diagonales

        col,ligne  = input_joueur
        if plateau[ligne][col] == 0:  # Position vide pour le nouveau pion
            for direction in directions:
                pions_a_retourner = parcours_direction(ligne, col, direction)
                list_de_pion_a_retourner.extend(pions_a_retourner)
        return list_de_pion_a_retourner


    def lister_coup_possible (self, plateau: list, joueur_actif:Joueur) :
        list_coup_possible=[]
        for x in range(0,8):
            for y in range (0,8):
                pion_test=(x,y)
                if self.trouver_pion_a_retourner(plateau=plateau,input_joueur=pion_test,joueur_actif=joueur_actif) :
                    list_coup_possible.append(pion_test)
        print("Coup possible: ",list_coup_possible)
        return list_coup_possible
    
    def verif_coup_joueur (self,input_joueur:tuple,list_coup_possible:list):
        if input_joueur in list_coup_possible:
            return True
        else:
            print("Coup impossible, rejoue")
            return False
        
    
    def placer_pion (self, plateau: list, input_joueur: tuple, joueur_actif:Joueur) : 
        input_index0=input_joueur[0]
        input_index1=input_joueur[1]
        plateau[input_index1][input_index0]=joueur_actif.couleur


    def retourner_pion(self, plateau: list, list_de_pion_a_retourner: list, joueur_actif:Joueur) :
        for pion in list_de_pion_a_retourner:
            self.placer_pion(plateau=plateau,input_joueur=pion,joueur_actif=joueur_actif)
    
    def switch_joueur(self,joueur1:Joueur,joueur2:Joueur) : 
        if joueur1.actif== True:
            joueur1.actif=False
            joueur2.actif=True
        else:
            joueur1.actif=True
            joueur2.actif=False
    
    

if __name__ == '__main__':
    engine1= Engine()
    #print(list_pion)
    #for pion in list_pion:
        #print(pion.couleur,pion.coordonnes,pion.position)
    engine1.initialisation_plateau_1_er_tour()

