# Engine

from pion import Pion

class Engine : 
    def initialisation_plateau_1_er_tour (self) : 
        ligne ='+---+----+----+----+----+----+----+----+----+\n|   | A  | B  | C  | D  | E  | F  | G  | H  |\n+---+----+----+----+----+----+----+----+----+\n| 1 | A1 | A2 | A3 | A4 | A5 | A6 | A7 | A8 |\n+---+----+----+----+----+----+----+----+----+\n| 2 | B1 | B2 | B3 | B4 | B5 | B6 | B7 | B8 |\n+---+----+----+----+----+----+----+----+----+\n| 3 | C1 | C2 | C3 | C4 | C5 | C6 | C7 | C8 |\n+---+----+----+----+----+----+----+----+----+\n| 4 | D1 | D2 | D3 | D4 | D5 | D6 | D7 | D8 |\n+---+----+----+----+----+----+----+----+----+\n| 5 | E1 | E2 | E3 | E4 | E5 | E6 | E7 | E8 |\n+---+----+----+----+----+----+----+----+----+\n| 6 | F1 | F2 | F3 | F4 | F5 | F6 | F7 | F8 |\n+---+----+----+----+----+----+----+----+----+\n| 7 | G1 | G2 | G3 | G4 | G5 | G6 | G7 | G8 |\n+---+----+----+----+----+----+----+----+----+\n| 8 | H1 | H2 | H3 | H4 | H5 | H6 | H7 | H8 |\n+---+----+----+----+----+----+----+----+----+'

        updated_ligne = ligne.replace("A1", "O ")
        ligne.replace("A1", "O ")
        print(updated_ligne)
    
        list_pion=[]

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

        return list_pion

if __name__ == '__main__':
    engine1= Engine()
    engine1.initialisation_plateau_1_er_tour()
    #print(list_pion)
    #for pion in list_pion:
        #print(pion.couleur,pion.coordonnes,pion.position)
    print(engine1.initialisation_plateau_1_er_tour())


    
    




