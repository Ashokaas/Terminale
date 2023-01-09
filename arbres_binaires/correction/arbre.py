
def _est_parfait(arbre):
    if arbre.est_une_feuille():
        return True
    if (arbre.G is None) != (arbre.D is None):
        return False
    return _est_parfait(arbre.G) and _est_parfait(arbre.D)


class Noeud:
    def __init__(self, data, fg=None, fd=None):
        """Initialise un arbre avec des enfants vides"""
        self.valeur = data
        self.G = fg
        self.D = fd

    def est_vide(self):
        """
        Permet de savoir si l'arbre est vide

        :return:
            bool: True si l'arbre est vide, False sinon
        """
        # TODO
        return self is None

    def greffer_gauche(self, greffe):
        """
        Greffe un noeud sur le fils gauche
        :parameter:
            greffe: Noeud
        """
        self.G = greffe

    def greffer_droit(self, greffe):
        """
        Greffe un arbre sur le fils droit

        :parameter:
            greffe: Noeud
        """
        self.D = greffe

    def get_filsgauche(self):
        """
        Renvoie le fils gauche

        :return:
            Noeud: noeud gauche
        """
        if self.est_vide():
            return None
        else:
            return self.G

    def get_filsdroit(self):
        """
        Renvoie le fils droit

        :return:
            Noeud: noeud gauche
        """
        if self.est_vide():
            return None
        else:
            return self.D

    def est_une_feuille(self):
        """
        Permet de savoir si l'avoir est une feuille
        :return:
            bool: True si l'abre est une feuille, False sinon
        """
        # TODO
        return self.G is None and self.D is None

    def est_peigne_gauche(self):
        """
        Permet de savoir si l'arbre est un peigne gauche

        :return:
            bool: True si l'arbre est un peigne gauche, False sinon
        """
        # TODO
        nd = self
        while nd.G is not None:
            if nd.D is not None:
                return False
            nd = nd.G
        return True

    def est_peigne_droit(self):
        """
        Permet de savoir si l'arbre est un peigne gauche

        :return:
            bool: True si l'arbre est un peigne gauche, False sinon
        """
        nd = self
        while nd.D is not None:
            if nd.G is not None:
                return False
            nd = nd.D
        return True


def get_hauteur(arbre):
    """
    Renvoie la hauteur d'un arbre
    :parameter:
        arbre : Noeud

    :return:
        int: hauteur de l'arbre
    """
    if arbre is None:
        return 0
    return 1 + max(get_hauteur(arbre.G), get_hauteur(arbre.D))


def get_taille(arbre):
    """
    Renvoie la taille d'un arbre
    :parameter:
        arbre : Noeud

    :return:
        int: taille de l'arbre
    """
    # TODO
    if arbre is None:
        return 0
    return 1 + get_taille(arbre.G) + get_taille(arbre.D)


def est_parfait(arbre):
    """
    Détermine si un arbre est parfait
    :param arbre: Nœud
    :return: bool: True si l'arbre est parfait, False sinon
    """
    # TODO
    if arbre.est_une_feuille():
        return True
    if (arbre.G is None) != (arbre.D is None):
        return False
    return est_parfait(arbre.G) and est_parfait(arbre.D)


# tests
if __name__ == '__main__':
    T = Noeud('A')
    T.G = Noeud('B')
    print(T.est_peigne_gauche())
    T.D = Noeud('D')
    T.G.G = Noeud('C')
    T.G.D = Noeud('Amog')
    T.D.G = Noeud('E')
    T.D.D = Noeud('F')
    print(get_hauteur(T))
    print(get_taille(T))
    print(est_parfait(T))
    print(T.est_peigne_droit())
