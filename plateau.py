l1 = [0, 0, 0, 0, 0, 0, 0, 0]
l2 = [0, 0, 0, 0, 0, 0, 0, 0]
l3 = [0, 0, 0, 0, 0, 0, 0, 0]
l4 = [0, 0, 0, 1, 2, 0, 0, 0]
l5 = [0, 0, 0, 2, 1, 0, 0, 0]
l6 = [0, 0, 0, 0, 0, 0, 0, 0]
l7 = [0, 0, 0, 0, 0, 0, 0, 0]
l8 = [0, 0, 0, 0, 0, 0, 0, 0]

# Création de la grille
grille = [l1, l2, l3, l4, l5, l6, l7, l8]


class Plateau : #création du plateau
    
    def __init__(self) : 
        

        self.grille = grille


    def update_plateau(self, grille):
        col_width = max(len(str(word)) for row in grille for word in row) + 2  # Calcul de la largeur des colonnes
        separator = '+' + '+'.join('-' * col_width for _ in range(len(grille[0]) + 1)) + '+'

        # Ajouter la ligne d'en-tête
        header = [' '] + [chr(ord('A') + i) for i in range(len(grille[0]))]
        print(separator)
        print('|' + '|'.join(str(word).ljust(col_width) for word in header) + '|')
        print(separator)

        # Créer un dictionnaire de mappage
        mapping = {1: 'X', 2: 'O', 0: ' '}  # Remplacez 1 par 'X', 2 par 'O', et 0 par ' ' (espace)

        # Imprimer les lignes avec séparateurs
        for i, row in enumerate(grille, start=1):
            # Remplacer les valeurs dans la rangée
            row = [mapping.get(word, word) for word in row]
            row = [i] + row  # Ajouter les numéros de ligne
            print('|' + '|'.join(str(word).ljust(col_width) for word in row) + '|')
            print(separator)  # Imprimer le séparateur après chaque ligne
        
    #update_plateau(grille)
        
    def gagnant(self,grille):
        scour_joueur_1 = 0
        scour_joueur_2 = 0
        for X in range(0,8):
            for Y in range(0, 8):
                if grille[X][Y] == 1:
                    scour_joueur_1 +=1
                elif grille [X][Y] == 2:
                    scour_joueur_2 += 1
        if scour_joueur_1 > scour_joueur_2:
            print("le joueur 1 a gagné")
        elif scour_joueur_1 < scour_joueur_2:
            print("le joueur 2 a gagné")
        else:
            print("egalité")
        
        print("noir :" ,scour_joueur_1 ,"blanc :"  ,scour_joueur_2)
