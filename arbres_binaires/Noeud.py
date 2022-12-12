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
        
        
        
if __name__ == "__main__":
    test = ListeChainee()
    test.ajouter_element(5)
    test.ajouter_element(4)
    test.ajouter_element(3)
    test.ajouter_element(2)
    test.ajouter_element(1)
    test.set_element(10, 1)
    for i in range(test.compter_elements()):
        print(test.supprimer_tete())