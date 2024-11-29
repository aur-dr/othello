emoji_choice = {
    "1": '🎁',
    "2": '🍪',
    "3": '⭐',
    "4": '🦌',
    "5": '🎅',
    "6": '🎄',
}

choix_joueur_1= ""

class Joueur:
    
    def __init__(self, num_joueur: int, actif: bool):
        
        if num_joueur == 1: 
            self.nom_joueur = input("Quel est le nom du premier joueur ? ") 
        else: 
            self.nom_joueur = input("Quel est le nom du deuxième joueur ? ") 

        print (
            "1 : " '🎁',
            "2 : " '🍪',
            "3 : " '⭐',
            "4 : " '🦌',
            "5 : " '🎅',
            "6 : " '🎄')
        
        if num_joueur == 1: 
            global choix_joueur_1 , emoji_choice             
            self.couleur =emoji_choice[input("Joueur 1 : choisi ton pion ? ")]
            choix_joueur_1 = self.couleur
        else : 
            self.couleur = emoji_choice[input("Joueur 2 : choisi ton pion ? ")]
            while self.couleur == choix_joueur_1 : 
                self.couleur = emoji_choice[input("Joueur 2 : choisi ton pion ? ")]
                if self.couleur == choix_joueur_1 :
                    print("Choisi un autre pion")
                             

    
        self.num_joueur = num_joueur
        self.a_joue_au_dernier_tour = True
        self.actif = actif
        self.input_joueur_MAJU = ""

    def input_joueur (self) :
        input_ok=False
        liste_position=[]
        lettres = ["A", "B", "C", "D", "E", "F", "G", "H"] 
        for x in range(1, 9):
            for y in range(1, 9):
                liste_position.append(lettres[x-1] + str(y))

        while input_ok!=True:
            self.input_joueur_MAJU=input(f'{self.nom_joueur} place ton pion {self.couleur}: ')
            self.input_joueur_MAJU=self.input_joueur_MAJU.upper()
            if self.input_joueur_MAJU == "Q":
                exit()
            else:
                if len(self.input_joueur_MAJU)==2:
                    if self.input_joueur_MAJU in liste_position:
                        input_ok=True
                    else:
                        print('Tu es en dehors de la grille, recommence ')
                else:
                    print("Mauvaise entrée, tu dois écrire 2 caractères, recommence ")
        
        #return input_joueur_MAJU

        #séparer caractère
        for caractere in self.input_joueur_MAJU : 

            if caractere=="A":
                index1= 0
            elif caractere=="B":
                index1= 1
            elif caractere=="C":
                index1= 2
            elif caractere=="D":
                index1= 3
            elif caractere=="E":
                index1= 4
            elif caractere=="F":
                index1= 5
            elif caractere=="G":
                index1= 6
            elif caractere=="H":
                index1= 7 
           
            else : 
                index2=int(caractere)-1

        self.input_joueur_MAJU=(index1,index2)
            

        