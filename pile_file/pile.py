"""
Classe Pile
"""

from noeud import Noeud


class Pile:
    """
    Classe Pile implémentée avec un liste
    """

    def __init__(self, valeurs:list=[]):
        """Initialisation de la pile"""
        self.valeurs = valeurs

    def pile_vide(self):
        """
        Vérifie si la pile est vide
        Renvoie un booléen
        """
        if len(self.valeurs) == 0:
            return True
        else:
            return False

    def push(self, element):
        """Ajoute un élément à la fin de la pile"""

        self.valeurs.append(element)

    def pop(self):
        """Supprime le dernier élément de la pile et le renvoie"""
        if not(self.pile_vide()):
            return self.valeurs.pop()
        else:
            return "List is empty"

    def sommet(self):
        """Renvoie le dernier élément de la pile"""
        if not(self.pile_vide()):
            return self.valeurs[-1]

    def taille(self):
        """Renvoie la taille de la pile"""
        return len(self.valeurs)


if __name__ == "__main__":
    ma_pile = Pile([Noeud(12).set_ref(1), Noeud(14).set_ref(2),
                    Noeud(8).set_ref(3), Noeud(7).set_ref(4),
                    Noeud(19).set_ref(5), Noeud(22)])
    print(ma_pile.pop())
    ma_pile.push(42)
    print(ma_pile.sommet())
    print(ma_pile.pop())
    print(ma_pile.taille())
    for loop in range(5):
        print(ma_pile.pop())
    print(ma_pile.pile_vide())
