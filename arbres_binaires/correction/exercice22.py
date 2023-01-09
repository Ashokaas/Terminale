
from NoeudArbre import *

def construit(arbre):
    if arbre == None:
        return ()
    else:
        return (arbre.item, construit(arbre.fils_gauche), construit(arbre.fils_droit))

def hauteur(arbre):
    """Retourne la hauteur de l'arbre"""
    #TODO
    pass

def taille(arbre):
    """Retourne la taille de l'arbre"""
    #TODO
    pass



f = Noeud('f')
e = Noeud('e')
d = Noeud('d', e, f)
c = Noeud('c')
b = Noeud('b', c, None)
a = Noeud('a', b, d)
print(construit(a))
print(hauteur(construit(a)))
print(taille(construit(a)))
