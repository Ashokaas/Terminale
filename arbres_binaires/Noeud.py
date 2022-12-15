class Noeud:
    ''' Mise en place d'une classe Noeud pour ensuite créer
        les classes agrégats Pile et File

        Chaque noeud contient une information et un pointeur
        Un objet de la classe noeud possède deux attributs :
          - un "item" qui contient l'information
          - une "ref" qui contient éventuellement l'adresse du noeud suivant
    '''
    def __init__(self, data):
        self.item = data  # on affecte une donnée au noeud
        self.ref = None   # on pointe sur le suivant

    # les getters
    def get_attributs(self):
        return self.item, self.ref

    def get_item(self):
        return self.item

    def get_ref(self):
        return self.ref

    # les setters
    def set_item(self, data):
        self.item = data

    def set_ref(self, ref):
        self.ref = ref




class ListeChainee:
    ''' Mise en place d'une classe ListeChainee'''
    def __init__(self):
        self.tete = None
        
        
    def est_vide(self):
        return self.tete is None
    
    
    def ajouter_element(self, valeur) -> None:
        if self.est_vide():
            self.tete = Noeud(valeur)
        else:
            nouveau_noeud = Noeud(valeur)
            nouveau_noeud.set_ref(self.tete)
            self.tete = nouveau_noeud
            
            
    def supprimer_tete(self):
        if self.est_vide():
            return None
        else:
            noeud_supprime = self.tete.get_item()
            self.tete = self.tete.get_ref()
            return noeud_supprime
        
        
    def compter_elements(self) -> int:
        if self.est_vide():
            return 0
        else:
            compteur = 1
            noeud_parcouru = self.tete
            while noeud_parcouru.get_ref() is not None:
                compteur += 1
                noeud_parcouru = noeud_parcouru.get_ref()
            return compteur
        
        
    def get_element(self, indice):
        if self.est_vide() or indice > self.compter_elements():
            return None
        else:
            compteur = 0
            noeud_parcouru = self.tete
            while compteur != indice:
                compteur += 1
                noeud_parcouru = noeud_parcouru.get_ref()
            return noeud_parcouru.get_item()
        
        
    def set_element(self, valeur, indice):
        if self.est_vide() or indice > self.compter_elements():
            return None
        else:
            compteur = 1
            noeud_parcouru = self.tete
            while compteur != indice:
                compteur += 1
                noeud_parcouru = noeud_parcouru.get_ref()
            nouveau_noeud = Noeud(valeur)
            nouveau_noeud.set_ref(noeud_parcouru.get_ref())
            noeud_parcouru.set_ref(nouveau_noeud)
        
        
    def supprimer_element(self, indice):
        if self.est_vide() or indice > self.compter_elements():
            return None
        else:
            compteur = 0
            noeud_parcouru = self.tete
            while compteur != indice - 1:
                compteur += 1
                noeud_parcouru = noeud_parcouru.get_ref()
            noeud_parcouru.set_ref(noeud_parcouru.get_ref().get_ref())
        
        
class ArbreListe:
    def __init__(self):
        self.liste = [None]
        
        
    def ajouter_niveau(self):
        hauteur = self.calculer_hauteur()
        for i in range(2 ** hauteur):
            self.liste.append(None)
            
            
    def ajouter_racine(self, valeur):
        self.liste[0] = valeur
        
        
    def ajouter_fils_gauche(self, valeur, indice):
        self.liste[2 * indice + 1] = valeur
        
    
    def ajouter_fils_droit(self, valeur, indice):
        self.liste[2 * indice + 2] = valeur
        
        
    def calculer_taille(self):
        nb_noeuds = 0
        for noeud in self.liste:
            if noeud is not None:
                nb_noeuds += 1
        return nb_noeuds
    
    
    def calculer_hauteur(self):
        hauteur = 0
        while 2 ** hauteur - 1 < len(self.liste):
            hauteur += 1
        return hauteur
    
    
    def calculer_profondeur(self, indice):
        profondeur = 0
        while 2 ** profondeur - 1 <= indice:
            profondeur += 1
        return profondeur
    
    
    
    
class NoeudFils:
    def __init__(self, val=None):
        self.item = val
        self.fils_gauche = None
        self.fils_droit = None
        
        
    def get_item(self):
        return self.item
    
    
    def get_fils_gauche(self):
        return self.fils_gauche
    
    
    def get_fils_droit(self):
        return self.fils_droit
    
    
    def set_fils_gauche(self, val=None):
        self.fils_gauche = NoeudFils(val)
        
        
    def set_fils_droit(self, val=None):
        self.fils_droit = NoeudFils(val)
        
        
    def est_une_feuille(self):
        return self.fils_gauche is None and self.fils_droit is None
    
    
    def est_peigne_gauche(self):
        if self.item is None or self.fils_droit is not None:
            return False
        noeud_temp = self.fils_gauche
        while noeud_temp is not None:
            if noeud_temp.fils_droit is not None:
                return False
            noeud_temp = noeud_temp.fils_gauche
        return True


    def est_peigne_droit(self):
        if self.item is None or self.fils_gauche is not None:
            return False
        noeud_temp = self.fils_droit
        while noeud_temp is not None:
            if noeud_temp.fils_gauche is not None:
                return False
            noeud_temp = noeud_temp.fils_droit
        return True



if __name__ == "__main__":
    """test = ListeChainee()
    test.ajouter_element(5)
    test.ajouter_element(4)
    test.ajouter_element(3)
    test.ajouter_element(2)
    test.ajouter_element(1)
    test.set_element(10, 1)
    test.supprimer_element(2)
    for i in range(test.compter_elements()):
        print(test.supprimer_tete())"""
    test2 = ArbreListe()
    test2.ajouter_niveau()
    test2.ajouter_niveau()
    test2.ajouter_niveau()
    test2.ajouter_niveau()
    test2.ajouter_niveau()
    test2.ajouter_niveau()
    print(test2.calculer_profondeur(16))


