 #lancement du jeu

#if debug à mettre dans la classe qui fait les input; lancer input prérempli

#fonction dans engine qui lancera le jeu

#creation de engine


from engine import Engine


if __name__ == '__main__':
    engine1 = Engine()
    engine1.plateau1.update_plateau()
    engine1.trouver_pion_a_retourner(plateau=engine1.plateau1.grille,input_joueur=(1,1),joueur_actif=engine1.joueur1)
    engine1.lister_coup_possible(plateau=engine1.plateau1.grille,joueur_actif=engine1.joueur1)