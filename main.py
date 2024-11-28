 #lancement du jeu

#if debug à mettre dans la classe qui fait les input; lancer input prérempli

#fonction dans engine qui lancera le jeu

#creation de engine


from engine import Engine


if __name__ == '__main__':
    engine1 = Engine()
    engine1.plateau1.update_plateau()
    engine1.trouver_pion_a_retourner(plateau=engine1.plateau1.grillef,input_joueur=(4,6),Joueur_actif=engine1.joueur1)