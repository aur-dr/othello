l1 = [0, 0, 0, 0, 0, 0, 0, 0]
l2 = [0, 0, 0, 0, 0, 0, 0, 0]
l3 = [0, 0, 0, 0, 0, 0, 0, 0]
l4 = [0, 0, 0, 1, 2, 0, 0, 0]
l5 = [0, 0, 0, 2, 1, 0, 0, 0]
l6 = [0, 0, 0, 0, 0, 0, 0, 0]
l7 = [0, 0, 0, 0, 0, 0, 0, 0]
l8 = [0, 0, 0, 0, 0, 0, 0, 0]

emoji_choice = {
    "1": '🎁',
    "2": '🍪',
    "3": '⭐',
    "4": '🦌',
    "5": '🎅',
    "6": '🎄',
}

# Création de la grille
grille = [l1, l2, l3, l4, l5, l6, l7, l8]


class Plateau : #création du plateau
    
    def __init__(self) : 
        

        self.grille = grille

    def update_plateau(self, grille, couleur1, couleur2):
        emoji_width = 3  # Emojis visually take up more space
        col_width = max(emoji_width, max(len(str(word)) for row in grille for word in row)) + 2

        separator = '+' + '+'.join('-' * col_width for _ in range(len(grille[0]) + 1)) + '+'

        # Add the header row
        header = [' '] + [chr(ord('A') + i) for i in range(len(grille[0]))]
        print(separator)
        print('|' + '|'.join(self.adjust_padding(str(word), col_width, emoji_width) for word in header) + '|')
        print(separator)

        # Create a mapping dictionary
        mapping = {1: couleur1, 2: couleur2, 0: ' '}  # Map 1 to couleur1, 2 to couleur2, and 0 to ' ' (space)

        # Print rows with separators
        for i, row in enumerate(grille, start=1):
            # Replace values in the row
            row = [mapping.get(word, word) for word in row]
            row = [i] + row  # Add line numbers
            # Adjust padding for emojis
            print('|' + '|'.join(self.adjust_padding(str(word), col_width, emoji_width) for word in row) + '|')
            print(separator)  # Print separator after each line

    def adjust_padding(self, word, col_width, emoji_width):
        if any(e in word for e in emoji_choice.values()):
            # If the word is an emoji, reduce padding to compensate for visual space
            return word.center(col_width - emoji_width // 2)
        else:
            # Regular centering for normal words
            return word.center(col_width)

        
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
