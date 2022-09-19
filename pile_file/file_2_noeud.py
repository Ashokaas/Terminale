"""
Classe File
"""

import noeud


class File2Noeud:
    """
    Classe File gérant les noeuds
    """
    def __init__(self, data=None):
        self.noeud_entree = noeud.Noeud()
        self.noeud_sortie = noeud.Noeud(data)
        self.noeud_sortie.set_ref(self.noeud_entree)
        if data is None:
            self.taille = 0
        else:
            self.taille = 1

    def get_first_item(self):
        if self.noeud_entree.get_item() is not None:
            return self.noeud_entree.get_item()
        return self.noeud_sortie.get_item()

    def get_last_item(self):
        return self.noeud_sortie.get_item()

    def get_ref(self):
        return self.noeud_sortie.get_ref()

    def etre_vide(self):
        return self.noeud_sortie is None

    def push(self, data):
        n = noeud.Noeud(data)
        self.noeud_entree.set_ref(n)
        self.noeud_entree = n
        self.taille += 1
        return self.noeud_entree.get_item()

    def pop(self):
        n = self.get_last_item()
        self.noeud_sortie = self.get_ref()
        self.taille -= 1
        return n

    def dernier(self):
        return self.get_last_item()

    def premier(self):
        return self.get_first_item()

    def long(self):
        return self.taille


if __name__ == "__main__":
    file = File2Noeud("L'Abbé Tonneuse")
    print(file.long())
    print(file.push("L'Abbé Tonneuse"))
    print(file.push("L'Abbé Tonière"))
    print(file.push("L'Abbé Nouar"))
    print(file.push("L'Abbé Thon"))
    print(file.push("Le Père Choir"))
    print(file.push("Le Père Soeur"))
    print(file.long())
    print(file.pop())
    print(file.long())
