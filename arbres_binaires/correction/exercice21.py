

class ArbreBinaireListe:
    # classe représentant un arbre binaire à l'aide d'une liste

    def __init__(self, racine):
        self.donnees = [racine, None, None]


    def get_valeur(self, indice):
        """retourne la valeur du noeud situé à l'indice donné"""
        try:
            return self.donnees[indice]
        except:
            print("indice non valide")


    def get_profondeur(self, indice):
        """retourne la profondeur du noeud d'indice donné"""
        #TODO
        pass


    def get_hauteur(self):
        """renvoie la hauteur du noeud d'indice donné"""
        #TODO
        pass


    def get_taille(self):
        """renvoie la taille de l'arbre"""
        #TODO
        pass


    def ajouter_generation(self):
        """ajoute un nouveau niveau vide à l'arbre"""
        l = len(self.donnees)
        self.donnees = self.donnees + [None]*(l + 1)


    def set_gauche(self, indice_pere, valeur):
        """ajoute un noeud fils gauche à un noeud pere"""
        try:
            if self.donnees[indice_pere] is None: # on écarte le cas du noeud père vide
                print("noeud père vide")
            elif self.donnees[2*indice_pere + 1] is not None: #on écarte le cas du fils non vide
                print("fils gauche non vide")
            else:
                niv = self.get_profondeur(indice_pere)
                hauteur_totale = self.get_profondeur(len(self.donnees) -1)
                # ajout d'une génération si nécessaire
                if hauteur_totale - niv < 2:
                    self.ajouter_generation()
                # ajout de la valeur au fils gauche
                self.donnees[2*indice_pere + 1] = valeur
        except:
            print("indice non valide")


    def set_droit(self, indice_pere, valeur):
        """ajoute un noeud fils droit à un noeud pere"""
        try:
            if self.donnees[indice_pere] is None:
                print("noeud père vide")
            elif self.donnees[2 * indice_pere + 2] is not None:
                print("fils droit non vide")
            else:
                niv = self.get_profondeur(indice_pere)
                hauteur_totale = self.get_profondeur(len(self.donnees)-1)                # ajout d'une génération si nécessaire
                if hauteur_totale - niv < 2:
                    self.ajouter_generation()
                    # ajout de la valeur au fils droit
                self.donnees[2 * indice_pere + 2] = valeur
        except:
            print("indice non valide")

    def supprimer_noeud(self, indice):
        """supprime le noeud d'indice donné s'il n'a pas d'enfant"""
        try:
            if self.donnees[2*indice + 1] is not None and self.donnees[2*indice + 2] is not None:
                print("le noeud a des enfants")
            else:
                self.donnees[indice] = None
        except:
            print("indice non valide")


    def afficher(self):
        print(self.donnees)


if __name__ == '__main__':
    arbre = ArbreBinaireListe('A')
    arbre.set_gauche(0, 'B')
    arbre.set_droit(0,'D')
    arbre.set_gauche(1, 'C')
    arbre.set_gauche(2,'E')
    arbre.set_droit(2, 'F')
