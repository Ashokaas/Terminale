"""Module pour gérer des rectangles

Caractéristiques du module :
    * Les rectangles peuvent être caractérisés par une largeur et une hauteur
    * L'unité pour la largeur et la hauteur est le caractère texte
    * les rectangles pourront être représentés sous 2 formats. Exemples pour un rectangle de 7x3 :
        Format    Format
        simple    complexe
        #######   +-----+
        #######   |     |
        #######   +-----+
"""

# Librairie(s) utilisée(s)
import math

# Métainformations du script
__author__ = "Johnny BEGOOD"
__license__ = "GPL"
__version__ = "0.0.1"
__email__ = "johnny.begood@geoforme.fr"
__status__ = "Development"
__date__ = "27/08/2020"


class Rectangle:
    """Classe représentant un rectangle"""

    def __init__(self, largeur, hauteur):
        """Initialise les dimensions du rectangle

        Parameters:
            largeur (int): largeur du rectangle
            hauteur (int): hauteur du rectangle
        """
        self.largeur = largeur
        self.hauteur = hauteur


    def get_largeur(self):
        """Accesseur retournant la largeur du rectangle

        Returns:
            (int): la largeur du rectangle
        """
        return self.largeur
        

    def get_hauteur(self):
        """Accesseur retournant la hauteur du rectangle

        Returns:
            (int): la hauteur du rectangle
        """
        return self.hauteur    
    

    def set_largeur(self, nouvelle_largeur):
        """Mutateur fixant la largeur du rectangle

        Parameters:
            nouvelle_largeur (int): la nouvelle largeur du rectangle
        """
        self.largeur = nouvelle_largeur
        

    def set_hauteur(self, nouvelle_hauteur):
        """Mutateur fixant la hauteur du rectangle

        Parameters:
            nouvelle_hauteur (int): la nouvelle hauteur du rectangle
        """
        self.hauteur = nouvelle_hauteur    

        
    def calculer_perimetre(self):
        """Calcule et retourne le périmètre du rectangle

        Returns:
            (int): le périmètre du rectangle
        """
        return self.hauteur*2 + self.largeur*2     
    

    def calculer_aire(self):
        """Calcule et retourne l'aire du rectangle

        Returns:
            (int): l'aire du rectangle
        """
        return self.hauteur * self.largeur
        

    def calculer_diagonale(self):
        """Calcule et retourne la longueur de la diagonale du rectangle

        Returns:
            (float): la longueur de la diagonale du rectangle
        """
        return math.sqrt(self.largeur**2 + self.hauteur**2)

    def calculer_ratio(self):
        """Calcule et retourne le ratio hauteur/largeur du rectangle

        Returns:
            (float): le ratio hauteur/largeur du rectangle
        """
        return self.hauteur / self.largeur
        

    def etre_carre(self):
        """Précise si le rectangle est carré ou pas

        Returns:
            (bool): True si le rectangle est carré, False sinon
        """
        return self.hauteur == self.largeur
    

    def etre_horizontal(self):
        """Précise si le rectangle est plutôt horizontal ou vertical

        Rectangle plutôt horizontal VS Rectangle plutôt vertical
               10x3                         4x5
            ##########                     ####
            ##########                     ####
            ##########                     ####
                                           ####
                                           ####
        On considérera un rectangle carré comme plutôt horizontal

        Returns:
            (bool): True si le rectangle est plutôt horizontal, False si vertical
        """
        return self.hauteur < self.largeur
            

    def etre_similaire(self, un_autre_rectangle):
        """Précise si le rectangle est similaire à un autre à une rotation de 90 degrés près

        Exemples de rectangles similaires:
              6x3   ~  3x6
            ######     ###
            ######     ###
            ######     ###
                       ###
                       ###
                       ###
        Parameters:
            un_autre_rectangle (Rectangle): l'autre rectangle peut-être similaire

        Returns:
            (bool): True si les rectangles sont similaires, False sinon
        """
        return self.hauteur == un_autre_rectangle.get_largeur() \
            and self.largeur == un_autre_rectangle.get_hauteur() 


    def etre_plus_grand_que(self, un_autre_rectangle):
        """Précise si le rectangle est plus grand (ou pas) qu'un autre passé en paramètre

        Details:
            * La comparaison de taille se fera avec l'aire des rectangles.
            * Pour être plus grand l'aire devra être strictement plus grande
            * Le rectangle à la base de la comparaison sera représenté par la variable self
            * Le second rectangle sera celui passé en paramètre

        Parameters:
            un_autre_rectangle (Rectangle) : l'autre rectangle avec lequel on veut se comparer

        Returns:
            (bool): True si le rectangle est plus grand, False sinon
        """
        return self.calculer_aire() > un_autre_rectangle.calculer_aire()
        

    def pouvoir_contenir(self, un_autre_rectangle):
        """Précise si le rectangle peut en contenir un autre

        Details:
            * Le rectangle de référence sera représenté par la variable self
            * Le second rectangle sera passé en paramètre
            * Le test se fera sur la largeur et la hauteur
            * Si la largeur et/ou la hauteur sont identiques on considérera que le rectangle
            ne peut pas contenir l'autre

        Parameters:
            un_autre_rectangle (Rectangle): rectangle dont on veut savoir si il est
            contenu dans le premier

        Returns:
            (bool): True si le premier contient le second, False sinon
        """
        return self.hauteur > un_autre_rectangle.get_hauteur() \
            and self.largeur > un_autre_rectangle.get_largeur()
            


    def creer_representation(self, version="simple"):
        """Créer et retourne une chaîne de caractères représentation le rectangle

        Exemple de représentations selon le format :
            Format    Format
            simple    complexe
            #######   +-----+
            #######   |     |
            #######   +-----+

        Parameters:
            version (string): format d'affichage du rectangle

        Returns:
            (string): chaîne de caractères représentant le rectangle
        """
        if version == "simple":
            for _ in range(self.hauteur):
                print("#"*self.largeur)
                
        elif version == "complexe":
            print("+" + "─"*(self.largeur-2) + "+")
            for _ in range(self.hauteur-2):
                print("|" + " "*(self.largeur-2) + "|")
            print("+" + "─"*(self.largeur-2) + "+")
            


# Pour mettre au point le codage de la classe Rectangle
if __name__ == '__main__':
    rectangle_1 = Rectangle(10, 10)
    rectangle_1.creer_representation(version="complexe")



