from arbre import *
from parcours import *


# les noeuds sont des tuples (équipe 1, équipe 2, score équipe 1, score équipe 2)

# finale
coupe = Noeud(('Chambéry', 'Dunkerque', 31, 21))

# demi-finales
coupe.G = Noeud(('Chambéry', 'Montpellier', 33, 29))
coupe.D = Noeud(('Nancy', 'Dunkerque', 17, 27))

# quarts de finale
coupe.G.G = Noeud(('Chambéry', 'Nantes', 36, 33))
coupe.G.D = Noeud(('Montpellier', 'PSG', 32, 31))
coupe.D.G = Noeud(('Nancy', 'Saran', 33, 29))
coupe.D.D = Noeud(('Dunkerque', 'Aix', 26, 23))

# 8èmes de finale
coupe.G.G.G = Noeud(('Chambéry', 'Saint-Raphaël', 33, 31))
coupe.G.G.D = Noeud(('Nantes', 'Nîmes', 23, 21))
coupe.G.D.G = Noeud(('Istres', 'Montpellier', 23, 30))
coupe.G.D.D = Noeud(('Tremblay', 'PSG', 32, 34))
coupe.D.G.G = Noeud(('Nancy', 'Rennes', 36, 31))
coupe.D.G.D = Noeud(('Saran', 'Massy', 28, 25))
coupe.D.D.G = Noeud(('Dunkerque', 'Toulouse', 31, 30))
coupe.D.D.D = Noeud(('Aix', 'Chartres', 26, 23))

# 16èmes de finale
coupe.G.G.G.G = Noeud(('Saint-Gratien', 'Chambéry', 20, 30))
coupe.G.G.G.D = Noeud(('Antibes', 'Saint-Raphaël', 25, 43))
coupe.G.G.D.G = Noeud(('Caen', 'Nantes', 23, 31))
coupe.G.G.D.D = Noeud(('Villeurbanne', 'Nîmes', 25, 31))
coupe.G.D.G.G = Noeud(('Pau', 'Istres', 27, 35))
coupe.G.D.G.D = Noeud(('Limoges', 'Montpellier', 25, 26))
coupe.G.D.D.G = Noeud(('Créteil', 'Tremblay', 31, 32))
coupe.G.D.D.D = Noeud(('Dijon', 'PSG', 25, 29))
coupe.D.G.G.G = Noeud(('Nancy', 'Sélestat', 36, 35))
coupe.D.G.G.D = Noeud(('Rennes', 'Cherbourg', 26, 24))
coupe.D.G.D.G = Noeud(('Saran', 'Ivry', 37, 35))
coupe.D.G.D.D = Noeud(('Massy', 'Pontrault-Combault', 25, 24))
coupe.D.D.G.G = Noeud(('Rezé', 'Dunkerque', 23, 41))
coupe.D.D.G.D = Noeud(('Nice', 'Toulouse', 29, 40))
coupe.D.D.D.G = Noeud(('Besançon', 'Aix', 30, 37))
coupe.D.D.D.D = Noeud(('Chartres', 'Cesson', 35, 31))


def lire_resultats(arbre, dic):
    """
    lit les résultats par parcours infixe de l'arbre
    :param arbre: arbre de tuples
    :param dic: dictionnaire
    :return: dictionnaire associant à chaque équipe une liste [matchs joués, points marqués, points encaissés]
    """
    #TODO
    pass


resultats = {}
lire_resultats(coupe, resultats)


# Affichage

print('##### meilleure attaque #####')
#TODO


print('##### meilleure défense #####')
#TODO


print('##### meilleure attaque par match #####')
#TODO


print('##### meilleure défense par match #####')
#TODO