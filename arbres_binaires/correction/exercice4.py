
from arbre import *


def appartient(valeur, arbre):
    """
    détermine si la valeur appartient à l'arbre
    :param valeur: (int ou str) valeur du type des étiquettes de l'arbre
    :param arbre: arbre binaire
    :return: bool : True si la valeur est dans l'arbre, false sinon
    """
    #TODO
    pass


def ajoute(valeur, arbre):
    """
    ajoute la valeur à l'arbre binaire de recherche
    :param valeur: (int ou str) valeur du type des étiquettes de l'arbre
    :param arbre: (ABR) arbre binaire de recherche
    :return: (ABR)
    """
    #TODO
    pass

class ABR:
    """classe définissant un arbre binaire de recherche"""
    def __init__(self):
        self.racine = None

    def ajouter(self, valeur):
        self.racine = ajoute(valeur, self.racine)

    def contient(self, valeur):
        return appartient(valeur, self.racine)


if __name__ == '__main__':
    a = ABR()
    a.ajouter(8)
    a.ajouter(3)
    a.ajouter(10)
    a.ajouter(1)
    a.ajouter(6)
    a.ajouter(4)
    a.ajouter(7)
    a.ajouter(14)
    a.ajouter(13)
    print(a.contient(7))
    print(get_hauteur(a.racine))
    print(get_taille(a.racine))