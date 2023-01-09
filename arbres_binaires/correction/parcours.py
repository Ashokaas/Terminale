from arbre import *


def parcours_infixe(arbre: Noeud):
    """
    Affiche les éléments de l'arbre dans un parcours infixe
    :param arbre: objet de la classe Noeud
    :return: les valeurs des étiquettes dans l'ordre infixe
    """

    # TODO
    if arbre is None:
        return
    else:
        parcours_infixe(arbre.G)
        print(arbre.valeur)
        parcours_infixe(arbre.D)


def parcours_prefix(arbre:Noeud):
    """
    Affiche les éléments de l'arbre dans un parcours préfixe
    :param arbre: objet de la classe Noeud
    :return: les valeurs des étiquettes dans l'ordre préfixe
    """

    # TODO
    if arbre is None:
        return
    else:
        print(arbre.valeur)
        parcours_prefix(arbre.G)
        parcours_prefix(arbre.D)


def parcours_suffixe(arbre:Noeud):
    """
    Affiche les éléments de l'arbre dans un parcours suffixe
    :param arbre: objet de la classe Noeud
    :return: les valeurs des étiquettes dans l'ordre suffixe
    """
    # TODO
    if arbre is None:
        return
    else:
        parcours_suffixe(arbre.G)
        parcours_suffixe(arbre.D)
        print(arbre.valeur)


def parcours_largeur(arbre:Noeud):
    """
    Affiche les éléments de l'arbre dans un parcours suffixe
    :param arbre: objet de la classe Noeud
    :return: les valeurs des étiquettes dans l'ordre suffixe
    """
    # TODO
    file = [arbre]
    retour = []
    while file:
        noeud = file.pop(0)
        retour.append(noeud.valeur)
        if noeud.get_filsgauche() is not None:
            file.append(noeud.get_filsgauche())
        if noeud.get_filsdroit() is not None:
            file.append(noeud.get_filsdroit())
    return retour


if __name__ == '__main__':
    T = Noeud('A')
    T.G = Noeud('B')
    T.D = Noeud('D')
    T.G.G = Noeud('C')
    T.D.G = Noeud('E')
    T.D.D = Noeud('F')
    print("Parcours infixe :")
    parcours_infixe(T)
    print("\nParcours prefix :")
    parcours_prefix(T)
    print("\nParcours suffixe :")
    parcours_suffixe(T)
    print("\nParcours en largeur :")
    print(parcours_largeur(T))
