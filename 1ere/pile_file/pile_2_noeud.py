from noeud import *

class Pile2noeud:
    "classe implémentée avec une liste chaînée"

    def __init__(self):
        self.top = None

    def etre_vide(self):
        return self.top == None

    def empiler(self, data):
        nouveau_noeud = Noeud(data)
        nouveau_noeud.set_ref(self.top)
        self.top = nouveau_noeud

    def depiler(self):
        if self.etre_vide():
            return None
        else:
            valeur = self.top.get_item()
            self.top = self.top.get_ref()
            return valeur

    def acceder_sommet(self):
        if self.etre_vide():
            return None
        else:
            return self.top.get_item()

    def calculer_taille(self):
        if self.etre_vide():
            return 0
        else:
            n = self.top
            taille = 1
            while n.get_ref() is not None:
                taille = taille + 1
                n = n.get_ref()
            return taille

    def afficher(self):
        if self.etre_vide():
            print("Pile vide")
        else:
            n = self.top
            print(n.get_item(), end=" -> ")
            while n.get_ref() is not None:
                n = n.get_ref()
                print(n.get_item(), end=" -> ")
            print()
        
    
    
if __name__ == "__main__":
    oui = Pile2noeud()
    oui.empiler("L'Abbé Tonneuse")
    oui.empiler("L'Abbé Tonière")
    oui.empiler("L'Abbé Nouar")
    oui.empiler("L'Abbé Thon")
    oui.empiler("Le Père Choir")
    oui.empiler("Le Père Soeur")
    print(oui.depiler())
    print(oui.acceder_sommet())
    print(oui.calculer_taille())

