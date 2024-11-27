from pion import Pion

class Plateau : #création du plateau

    def __init__(self, list_pion : list, structure_globale_du_tableau : str) :
        self.list_pion=list_pion
        self.structure_globale_du_tableau=structure_globale_du_tableau

    def tranformation_du_tableau_a_afficher(self) :
        for pion in list:
            self.structure_globale_du_tableau.replace(pion.position,pion.couleur+" ")
              
    def affichage (self) : #affichage
        return print(self.structure_globale_du_tableau)
    
if __name__ == '__main__':
    plateau1=Plateau()
    
    