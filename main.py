 #lancement du jeu

#if debug à mettre dans la classe qui fait les input; lancer input prérempli

#fonction dans engine qui lancera le jeu

#creation de engine


from engine import Engine


if __name__ == '__main__':
    engine1 = Engine() #creation de l'engine
    engine1.plateau1.update_plateau() #affichage du plateau et des joueur
    #engine1.trouver_pion_a_retourner(plateau=engine1.plateau1.grille,input_joueur=(1,1),joueur_actif=engine1.joueur1) #test
    #engine1.lister_coup_possible(plateau=engine1.plateau1.grille,joueur_actif=engine1.joueur1) #test
    
    
    while engine1.joueur1.a_joue_au_dernier_tour == True or engine1.joueur2.a_joue_au_dernier_tour == True :
        if engine1.joueur1.actif == True : 
            joueur= engine1.joueur1
        else : 
            joueur= engine1.joueur2

        coup_possible = engine1.lister_coup_possible(plateau=engine1.plateau1.grille, joueur_actif=joueur)
        if coup_possible != [] : 
            verif_ok=False
            while verif_ok!=True:
                joueur.input_joueur() #joueur 1 a un nput
                verif_ok=engine1.verif_coup_joueur(input_joueur=joueur.input_joueur_MAJU, list_coup_possible= coup_possible) #vérification coup joueur
                print("verif de l'input: ",joueur.input_joueur_MAJU)
            engine1.placer_pion(plateau = engine1.plateau1.grille, input_joueur= joueur.input_joueur_MAJU, joueur_actif=joueur)

            pion_a_retourner = engine1.trouver_pion_a_retourner(plateau=engine1.plateau1.grille, input_joueur=joueur.input_joueur_MAJU, joueur_actif=joueur) #Trouve les pions à retourner 
            print("pion a retourner: ",pion_a_retourner)
            engine1.retourner_pion(plateau=engine1.plateau1.grille, list_de_pion_a_retourner= pion_a_retourner, joueur_actif=joueur) #Retourne les pions 

            engine1.plateau1.update_plateau() #affiche le plateau

        else : 
            print("Pas de coup possible, joueur suivant joue")
            

        engine1.switch_joueur(joueur1=engine1.joueur1, joueur2=engine1.joueur2)

    engine1.plateau1.gagnant(grille= engine1.plateau1.grille)
    

        


        


        
