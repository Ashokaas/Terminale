
from arbre import *

def optimiser_grotte(liste_objets, poids_max):
    """
    optimise la valeur des objets choisis dans une liste dans la limite d'un poids maximal
    :param liste_objets: tuple de listes (nom, poids, valeur)
    :param poids_max: poids maximum
    :return: tuple : list: liste des objets à emporter pour optimiser la valeur
                     int: valeur totale
    """
    #TODO
    pass


if __name__ == '__main__':
    objets1 = (["bracelet", 2, 7], ["pièce", 1, 1], ["vase", 3, 10], ["gemme", 1, 1],
               ["couronne", 3, 12], ["collier", 2, 7], ["coffret", 5, 15])
    print(optimiser_grotte(objets1, 4))
    objets2 = tuple([["bracelet", 5, 2]] * 2 + [["chandelier", 17, 27]] * 2 +
                    [["collier", 21, 71]] * 2 + [["diamant", 2, 3]] * 3 +
                    [["pièce", 1, 1]] * 4 + [["statue", 37, 120]] * 1 +
                    [["statuette", 75, 150]] * 1)
    print(optimiser_grotte(objets2, 80))