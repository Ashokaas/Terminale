"""NSI - Récursivité - TP - Sortir du labyrinthe (5.X)"""


class Labyrinthe:
    """Classe pour représenter un labyrinthe"""


    def __init__(self):
        """Initialise le labyrinthe"""
        self.largeur = 0
        self.hauteur = 0
        self.x_entree = 0
        self.y_entree = 0
        self.x_sortie = 0
        self.y_sortie = 0
        self.cases = []


    def charger(self, nom_du_fichier):
        """Charge un labyrinthe en mémoire depuis un fichier
        
        Parameters:
            nom_du_fichier (string) : nom du fichier contenant le labyrinthe

        File format:
            10;10       --> largeur;hauteur
            1;1         --> coordonnées du point de départ
            8;1         --> coordonnées du point d'arrivée 
            XXXXXXXXXX  --> une croix (X) est un mur, un point (.) est un vide
            X.X...XX.X
            X...X.XX.X
            XXXXX.XX.X
            X........X
            X........X
            X........X
            X........X
            X........X
            XXXXXXXXXX
        """
        # Lecture des lignes du fichiers
        with open(nom_du_fichier, "r") as fichier:
            lignes = fichier.readlines()
            fichier.close()

            # Décodage largeur et hauteur
            decoupage = lignes[0].split(";")
            self.largeur = int(decoupage[0])
            self.hauteur = int(decoupage[1])

            # Décodage coordonnées entrée labyrinthe
            decoupage = lignes[1].split(";")
            self.x_entree = int(decoupage[0])
            self.y_entree = int(decoupage[1])

            # Décodage coordonnées entrée labyrinthe
            decoupage = lignes[2].split(";")
            self.x_sortie = int(decoupage[0])
            self.y_sortie = int(decoupage[1])

            for i in range(3, self.hauteur+3):
                self.cases.append(lignes[i].strip())


    def get_case(self, i, j):
        """Retourne le contenu de la case (i,j) du labyrinthe
        
        Parameters:
            i (int) : numéro de la colonne
            j (int) : numéro de la ligne

        Returns:
            (string) : caractère contenu dans le labyrinthe en (i, j)
        """
        if i >= 0 and i < self.largeur and j >= 0 and j < self.hauteur:
            return self.cases[j][i]
        else:
            return None


    def afficher(self):
        """Affiche le labyrinthe et ses caractéristiques"""
        print("Le labyrinthe")
        print(f" => Dimensions : {self.largeur}x{self.hauteur}")
        print(f" => Entrée     : ({self.x_entree}, {self.y_entree})")
        print(f" => Sortie     : ({self.x_sortie}, {self.y_sortie})")
        print(" => Les cases  :")
        for j in range(0, self.hauteur):
            for i in range(0, self.largeur):
                if i == self.x_entree and j == self.y_entree:
                    print("e", end="")
                elif i == self.x_sortie and j == self.y_sortie:
                    print("s",  end="")
                else:
                    if self.cases[j][i] == "X":
                        print(f"\033[47;30m{self.cases[j][i]}\033[00m", end="")
                    if self.cases[j][i] == ".":
                        print(f"\033[30;37m{self.cases[j][i]}\033[00m", end="")
                    #print(self.cases[j][i], end="")
            print()


