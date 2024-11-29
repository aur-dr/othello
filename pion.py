

class Pion:
    def __init__(self, couleur: str, coordonnes: tuple, position: str):
        self.couleur = couleur
        self.coordonnes = coordonnes
        self.position = position
    def __str__(self):
        return f"{self.couleur}, {self.coordonnes}, {self.position} "




if __name__ == "__main__":
    pion1=Pion(couleur= "X",coordonnes=(1,1), position=("A1"))
    print(pion1)
    # if couleur is not("X","O", " "):
    #     raise ValueError("le couleur doit etre 'X' ou 'O' ou ' '")
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
            
    print(list_pion)
    for pion in list_pion:
        print(pion.couleur,pion.coordonnes,pion.position)
    
