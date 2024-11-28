
class Plateau : #création du plateau
    l1 = [0, 0, 0, 0, 0, 0, 0, 0]
    l2 = [0, 0, 0, 0, 0, 0, 0, 0]
    l3 = [0, 0, 0, 0, 0, 0, 0, 0]
    l4 = [0, 0, 0, 0, 0, 0, 0, 0]
    l5 = [0, 0, 0, 0, 0, 0, 0, 0]
    l6 = [0, 0, 0, 0, 0, 0, 0, 0]
    l7 = [0, 0, 0, 0, 0, 0, 0, 0]
    l8 = [0, 0, 0, 0, 0, 0, 0, 0]

    # Création de la grille
    grille = [l1, l2, l3, l4, l5, l6, l7, l8]

    def update_plateau(grille):
        col_width = max(len(str(word)) for row in grille for word in row) + 2  # Calcul de la largeur des colonnes
        separator = '+' + '+'.join('-' * col_width for _ in range(len(grille[0]) + 1)) + '+'

        # Ajouter la ligne d'en-tête
        header = [' '] + [chr(ord('A') + i) for i in range(len(grille[0]))]
        print(separator)
        print('|' + '|'.join(str(word).ljust(col_width) for word in header) + '|')
        print(separator)
        
        # Imprimer les lignes avec séparateurs
        for i, row in enumerate(grille, start=1):
            row = [i] + row  # Ajouter les numéros de ligne
            print('|' + '|'.join(str(word).ljust(col_width) for word in row) + '|')
            print(separator)  # Imprimer le séparateur après chaque ligne

    update_plateau(grille)
        

    def __init__(self, grille) : 
        self.grille = grille