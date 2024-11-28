# Engine

from pion import Pion
from plateau import Plateau
class Engine : 
    def __init__(self) :
       list_pion=[]
       
    def initialisation_plateau_1_er_tour (self) : 
        structure_plateau_str ='+---+----+----+----+----+----+----+----+----+\n|   | A  | B  | C  | D  | E  | F  | G  | H  |\n+---+----+----+----+----+----+----+----+----+\n| 1 | A1 | A2 | A3 | A4 | A5 | A6 | A7 | A8 |\n+---+----+----+----+----+----+----+----+----+\n| 2 | B1 | B2 | B3 | B4 | B5 | B6 | B7 | B8 |\n+---+----+----+----+----+----+----+----+----+\n| 3 | C1 | C2 | C3 | C4 | C5 | C6 | C7 | C8 |\n+---+----+----+----+----+----+----+----+----+\n| 4 | D1 | D2 | D3 | D4 | D5 | D6 | D7 | D8 |\n+---+----+----+----+----+----+----+----+----+\n| 5 | E1 | E2 | E3 | E4 | E5 | E6 | E7 | E8 |\n+---+----+----+----+----+----+----+----+----+\n| 6 | F1 | F2 | F3 | F4 | F5 | F6 | F7 | F8 |\n+---+----+----+----+----+----+----+----+----+\n| 7 | G1 | G2 | G3 | G4 | G5 | G6 | G7 | G8 |\n+---+----+----+----+----+----+----+----+----+\n| 8 | H1 | H2 | H3 | H4 | H5 | H6 | H7 | H8 |\n+---+----+----+----+----+----+----+----+----+'
  
        

        for X in range(1, 9):
            for Y in range(1, 9):
                if X==1:
                    Lettre="A"
                elif X == 2:
                    Lettre="B"
                elif X == 3:
                    Lettre = "C"
                elif X == 4:
                    Lettre = "D"
                elif X == 5:
                    Lettre = "E"
                elif X == 6:
                    Lettre = "F"
                elif X == 7:
                    Lettre = "G"
                elif X == 8:
                    Lettre = "H" 
                list_pion.append(Pion(couleur=" ",coordonnes=(X,Y),position=Lettre+str(Y)))
        
        for pion in list_pion : #initialisation des 4 pions de départ
            if pion.position == "D4" or pion.position == "E5" : 
                pion.couleur = "X"
            
            elif pion.position == "D5" or pion.position == "E4" : 
                pion.couleur = "O"

        plateau_init=Plateau(list_pion,structure_plateau_str)        
        plateau_init.transformation_du_tableau_a_afficher()
        plateau_init.affichage()

    def trouver_pion_a_retourner (self, list_pion, pion_pose) :
        #input : list_pion 
        #output : list_de_pion_a_retourner 
        
        if pion_pose.couleur == "X" : 
            couleur_a_chercher = "O"
        else :
            couleur_a_chercher = "X"

        list_coordonnes_relatives = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]
        list_coordonnes_absolues = list_coordonnes_relatives.copy 

        list_case_potentielle = []
        for pion in self.list_pion : 
            #if pion.couleur == couleur_a_chercher and pion.coordonnes in list_coordonnes_relative : 
            for coordonne in list_coordonnes_relatives : 
                if coordonne == pion.coordonnes : 
                    list_case_potentielle.append(pion.coordonnes)
        for case_potentielle in list_case_potentielle :      
            if len(list_coordonnes_relatives) == len(list_coordonnes_absolues):
                list_test = [(x_rel - x_abs, y_rel - y_abs) for (x_rel, y_rel), (x_abs, y_abs) in zip(list_coordonnes_relatives, list_coordonnes_absolues)]
            #print(list_test)
            
            else:
                print("Le calcul des coordonnées a un problème.")




            

            

if __name__ == '__main__':
    engine1= Engine()
    #print(list_pion)
    #for pion in list_pion:
        #print(pion.couleur,pion.coordonnes,pion.position)
    engine1.initialisation_plateau_1_er_tour()



    
    




