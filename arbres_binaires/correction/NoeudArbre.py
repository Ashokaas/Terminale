# Mise en place d'une classe noeud pour un arbre binaire
######################################################################
# Chaque noeud contient une information et deux pointeurs
# Un objet de la classe noeud possède deux attributs :
#  - un "item" qui contient l'information
#  - un "fils_gauche" qui contient éventuellement l'adresse d'un autre noeud
#  - un "fils_droit" qui contient éventuellement l'adresse d'un autre noeud


class Noeud:
    def __init__(self, data, fg = None, fd = None):
        self.item = data  # on affecte une donnée au noeud
        self.fils_gauche = fg   # on pointe sur le fils gauche
        self.fils_droit = fd    # on pointe su rle fils droit

    # les getters
    def get_item(self):
        return self.item

    def get_filsgauche(self):
        return self.fils_gauche

    def get_filsdroit(self):
        return self.fils_gauche

    # les setters
    def set_item(self, data):
        self.item = data

    def set_filsgauche(self, ref):
        self.fils_gauche = ref

    def set_filsdroit(self, ref):
        self.fils_droit = ref
