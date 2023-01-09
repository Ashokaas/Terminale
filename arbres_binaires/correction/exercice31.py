
from arbre import *
from math import *


# une première proposition pour déterminer si un nombre est premier
def is_prime(n):
    """
    Permet de tester si un nombre est premier
    :param n: (int) entier supérieur à 2
    :return: bool:  True si n est premiern False sinon
    """
    return [k for k in range(2, int(sqrt(n) + 1)) if n%k == 0] == [] and n > 1


# une deuxième proposition qui détermine la liste des premiers
# inférieurs à un entier, sous forme récursive
def eratosthene(n, liste_premiers = [], liste = None):
    """
    renvoie la liste des nombres premiers inférieurs à un entier à l'aide du crible d'Eratosthène
    :param n: (int)
    :param liste_premiers: utilisée dans la récursion pour stocker la liste cherchée
    :param liste: utilisée dans la récursion pour le crible
    :return: list: liste des premiers inférieurs à n
    """
    if liste is None:
        liste = range(2, n + 1)
    if liste == []:
        return liste_premiers
    else:
        premier = liste[0]

        return eratosthene(n, liste_premiers + [premier], [k for k in liste if k%premier != 0])


def decomposer(n, liste = []):
    """
    renvoie la liste des facteurs premiers d'un nombre entier
    :param n: (int)
    :param liste: utilisée dans la récursion pour stocker la liste cherchée
    :return: list: liste des premiers inférieurs à n
    """
    if is_prime(n):
        return liste + [n]
    else:
        liste_premiers = eratosthene(int(sqrt(n)) + 1)
        k = 0
        while n%liste_premiers[k] != 0:
            k = k + 1
        return decomposer(n//liste_premiers[k], liste + [liste_premiers[k]])


def diviseurs(n):
    # détermination de la liste des diviseurs premiers
    liste_div = decomposer(n)
    #TODO
    pass



if __name__ == '__main__':
    print([n for n in range(100) if is_prime(n)])
    print(eratosthene(100))
    print(decomposer(72))
    diviseurs(72)