"""NSI - Récursivité - TP - Sortir du labyrinthe (5.X)"""

# Librairies utilisées
from labyrinthe import Labyrinthe
from robot import Robot
import os


# Bannière d'accueil
print("**************************************")
print("*** Explorateur de labyrinthe v0.1 ***")
print("**************************************")

# Création, chargement et affichage du labyrinthe
l = Labyrinthe()
l.charger("labyrinthe00.txt"))
l.afficher()

# Création du robot et recherche du chemin vers la sortie
r = Robot(l)
r.rechercher_chemin(10)