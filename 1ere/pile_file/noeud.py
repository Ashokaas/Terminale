class Noeud:
    ''' Mise en place d'une classe Noeud pour ensuite créer
        les classes agrégats Pile et File

        Chaque noeud contient une information et un pointeur
        Un objet de la classe noeud possède deux attributs :
          - un "item" qui contient l'information
          - une "ref" qui contient éventuellement l'adresse du noeud suivant
    '''
    def __init__(self, data=None):
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
