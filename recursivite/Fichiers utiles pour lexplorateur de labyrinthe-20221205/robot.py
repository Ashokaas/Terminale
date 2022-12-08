"""NSI - Récursivité - TP - Sortir du labyrinthe (5.X)"""

# Librairie utilisée
from labyrinthe import Labyrinthe


class Robot:
    """Classe représentant le robot"""


    def __init__(self, labyrinthe):
        """Initialise le robot avec un labyrinthe
        
        Parameters:
            labyrinthe (Labyrinthe) : le labyrinthe à explorer par le robot
        """
        self.l = labyrinthe
        self.x = self.l.x_entree
        self.y = self.l.y_entree
        self.chemin = []


    def rechercher_chemin(self, profondeur_max):
        """Calcule et retourne le chemin de l'entrée à la sortie
        
        Parameters: 
            profondeur_max (int) : profondeur maximum de recherche

        Returns:
            (list of tuples) : la liste des positions pour sortir du labyrinthe [(1,1), (1,2), (1,3)]        
        """
        
        # TODO : à faire


    def afficher_chemin(self):
        """Affiche le chemin trouvé en vert pour sortir du labyrinthe"""
        # TODO : à faire
        
        
        
    def etre_possible(self, x, y):
        """Vérifie si le robot peut se déplacer sur la case (x, y)
        
        Parameters:
            x (int) : position en x du robot
            y (int) : position en y du robot

        Returns:
            (bool) : True si le robot peut se déplacer sur la case, False sinon
        """
        try:
            if self.l.get_case(x, y) is not None:
                return True
            return False
        except:
            return False

        
    def parcourir(self, x, y, profondeur, profondeur_max):
        """Parcours récursif du labyrinthe
        
        Parameters:
            x (int) : position en x du robot
            y (int) : position en y du robot
            profondeur (int) : profondeur de recherche
            profondeur_max (int) : profondeur maximum de recherche

        Returns:
            (bool) : True si le chemin est trouvé, False sinon
        """
        
        
        if x == self.l.x_sortie and y == self.l.y_sortie:
            self.chemin.append((x, y))
            return True
        elif profondeur == profondeur_max:
            return False
        elif 
        
        