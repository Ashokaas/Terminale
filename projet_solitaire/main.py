# ============================================================
#    IMPORTATIONS DES LIBRAIRIES + Vérification utilisateur
# ============================================================

# On importe uniquement OS en premier afin de ne pas créer d'erreur
import os

# Vérifie que l'utilisateur a bien suivi les intructions pour éviter une erreur
print("Avez-vous bien lu le fichier 'lisez-moi.txt' ?")
touche = input("Appuyez sur 'O' puis 'Entrée' pour l'ouvrir ou simplement sur 'Entrée' pour continuer : ")

# Si touche = O alors on ouvre le fichier et on quitte le programme
if touche in ['o', 'O']:
    os.startfile('lisez_moi.txt')
    exit()


# Necessaires au bon fonctionnement d'un jeu de carte
import JeuCarte   # Création d'un jeu de carte
import pile as p  # Utilisation des piles
import file as f  # Utilisation des files

# Supplémentaires
import colorama   # Coloriser un texte
import keyboard   # Accès au clavier
import platform   # Connaître l'OS de l'utilisateur
import time       # Pour effectuer des pauses et éviter l'appui involontaire d'une touche




# =====================================
#             class Game
# =====================================
class Game:

    def __init__(self):
        """Affiche le menu principal du jeu et demande à l'utilisateur le nombre de cartes à utiliser

        Returns:
            str: Nombre de cartes
        """
        # OS de l'utilisateur
        self.os = platform.system()
        
        # Effacement de l'interface
        self.clear()
        
        # Titre du jeu (ASCII Art : https://fsymbols.com/generators/carty/)
        print(f"""  
            ░██████╗░█████╗░██╗░░░░░██╗████████╗░█████╗░██╗██████╗░███████╗
            ██╔════╝██╔══██╗██║░░░░░██║╚══██╔══╝██╔══██╗██║██╔══██╗██╔════╝
            ╚█████╗░██║░░██║██║░░░░░██║░░░██║░░░███████║██║██████╔╝█████╗░░
            ░╚═══██╗██║░░██║██║░░░░░██║░░░██║░░░██╔══██║██║██╔══██╗██╔══╝░░
            ██████╔╝╚█████╔╝███████╗██║░░░██║░░░██║░░██║██║██║░░██║███████╗
            ╚═════╝░░╚════╝░╚══════╝╚═╝░░░╚═╝░░░╚═╝░░╚═╝╚═╝╚═╝░░╚═╝╚══════╝
                        
                    {self.color_text(text='Appuyez sur ESPACE pour commencer une partie !', color="YELLOW")}
        """)
        
        keyboard.wait('space')
        print("Voulez vous jouer à 32 ou 52 cartes ? (1/2)")

        # En attente du choix de l'utilisateur : uniquement s'il a pressé 1 ou 2
        keyboard_nb_cartes = keyboard.read_key()
        while keyboard_nb_cartes not in ["1", "&", "2", "é"]:
            keyboard_nb_cartes = keyboard.read_key()
            
        # Ajuste les paramètres de jeu en fonction du nombre de cartes
        if keyboard_nb_cartes in ["1", "&"]:
            self.nb_cartes = "32"
            self.cartes = ["7", "8", "9", "10", "V", "D", "R", "As"]
        elif keyboard_nb_cartes in ["2", "é"]:
            self.nb_cartes = "52"
            self.cartes = ["As", "2", "3", "4", "5", "6", "7", "8", "9", "10", "V", "D", "R"]
            
        # Caractère spécial de chaque famille
        self.carreau = "♦"
        self.pique =  "♠"
        self.coeur = "♥"
        self.trefle = "♣"
        
        # Définition du score
        self.score = 0

        # Définition du jeu en fonction du nombre de cartes
        self.jeu_cartes = JeuCarte.JeuCarte(self.nb_cartes)
        self.jeu_cartes.melangerJeu()

        # Définition du talon de la carte piochée et des cartes piochées ignorées
        self.talon = f.File(self.jeu_cartes.getJeu())
        self.talon_temp = f.File()
        self.carte_piochee = self.talon.retire()

        # Définition des 4 défausses ('hidden' pour spécifier qu'on cache la carte)
        
                # Défausse 1
        self.defausse1 = p.Pile()
        for _ in range(4):
            c = self.talon.retire()
            c[2] = 'hidden'
            self.defausse1.push(c)
            
                # Défausse 2
        self.defausse2 = p.Pile()
        for _ in range(3):
            c = self.talon.retire()
            c[2] = 'hidden'
            self.defausse2.push(c)
            
                # Défausse 3
        self.defausse3 = p.Pile()
        for _ in range(2):
            c = self.talon.retire()
            c[2] = 'hidden'
            self.defausse3.push(c)
            
                # Défausse 4
        self.defausse4 = p.Pile()
        c = self.talon.retire()
        c[2] = 'hidden'
        self.defausse4.push(c)
        
        
        # Définition des 4 familles
            # Piques
        self.piques = p.Pile()
        self.piques.push(["0", "0", "Pique"])
            # Carreaux
        self.carreaux = p.Pile()
        self.carreaux.push(["0", "0", "Carreau"])
            # Trèfles
        self.trefles = p.Pile()
        self.trefles.push(["0", "0", "Trèfle"])
            # Coeurs
        self.coeurs = p.Pile()
        self.coeurs.push(["0", "0", "Coeur"])
        
        # Couleur de chaque famille
        self.couleurs_familles = {"Pique": "noir", "Coeur": "rouge", "Carreau": "rouge", "Trèfle": "noir"}
        
        # Défini une defausse en fonction de la touche appuyée
        self.dico_touche_defausse = {"1": "1", "&": "1", 
                                     "2": "2", "é": "2",
                                     "3": "3", '"': "3",
                                     "4": "4", "'": "4"}
        
        # Défini une famille en fonction de la touche appuyée
        self.dico_touche_familles = {"1": "coeurs", "&": "coeurs", 
                                "2": "piques", "é": "piques",
                                "3": "carreaux", '"': "carreaux",
                                "4": "trefles", "'": "trefles"}




    def verifier_victoire(self):
        """Vérifie si la partie a été gagnée
        """
        # Si la somme des familles (+ 4 car on ajouté des cartes nulles au début) est égale au nombre de cartes du jeu alors c'est gagné
        if int(self.nb_cartes) == self.piques.taille() + self.carreaux.taille() + self.trefles.taille() + self.coeurs.taille() + 4:
            print("""\n\n
                ██╗░░░██╗██╗░█████╗░████████╗░█████╗░██╗██████╗░███████╗
                ██║░░░██║██║██╔══██╗╚══██╔══╝██╔══██╗██║██╔══██╗██╔════╝
                ╚██╗░██╔╝██║██║░░╚═╝░░░██║░░░██║░░██║██║██████╔╝█████╗░░
                ░╚████╔╝░██║██║░░██╗░░░██║░░░██║░░██║██║██╔══██╗██╔══╝░░
                ░░╚██╔╝░░██║╚█████╔╝░░░██║░░░╚█████╔╝██║██║░░██║███████╗
                ░░░╚═╝░░░╚═╝░╚════╝░░░░╚═╝░░░░╚════╝░╚═╝╚═╝░░╚═╝╚══════╝""")

            print(f"Score : {self.score}")
            print("Appuyez sur 'espace' pour quitter !")
            keyboard.wait('space')
            exit()
            



    def symboles_familles(self, texte):
        """Remplace le texte par le symbole correspondant (ex: "Carreau" -> "♦")

        Args:
            text (_type_): texte à modifier

        Returns:
            str: texte
        """
        texte = str(texte)
        texte = texte.replace('Carreau', self.carreau).replace('Pique', self.pique).replace('Coeur', self.coeur).replace('Trèfle', self.trefle)
        return texte
    
    
    
    
    def texte_couleurs_familles(self, texte):
        """Met en rouge si la famille est carreau ou coeur
        """
        if self.carreau in texte or self.coeur in texte:
            return self.color_text(text=texte, color="RED")
        else:
            return texte
        
        
        
    
    def verifier_carte(self, carte_a_deplacer:list, carte_inferieur:list, defausse_ou_famille:str):
        """Vérifie si un déplacement de carte est possible

        Args:
            carte_a_deplacer (list): Carte qui va être déplacée sur une autre
            carte_inferieur (list): Carte qui va reçevoir la carte à déplacer
            defausse_ou_famille (str): Si la carte est déplacée vers une défause ou une famille

        Returns:
            (bool): True si possible / False si impossible
        """
        """
        if carte_a_deplacer[0] == "7":
            return False"""
        # Pour toutes les cartes du jeu
        for x in range(len(self.cartes)):
            # Si on déplace vers une défausse
            if defausse_ou_famille == "defausse":
                # Quand on atteint la carte à déplacer et si la carte inférieur est égale à la carte d'avant de self.cartes
                if carte_a_deplacer[0] == self.cartes[x] and carte_inferieur[0] == self.cartes[x-1]:
                    # Si les cartes sont d'une couleur opposée
                    if self.couleurs_familles[carte_a_deplacer[1]] != self.couleurs_familles[carte_inferieur[1]]:
                        return True
            # Si on déplace vers une famille
            elif defausse_ou_famille == "famille":
                # Quand on atteint la carte à déplacer et si la carte inférieur est égale à la carte d'avant de self.cartes
                if carte_a_deplacer[0] == self.cartes[x] and carte_inferieur[0] == self.cartes[x-1]:
                    # Si les cartes sont de la même couleur
                    if self.couleurs_familles[carte_a_deplacer[1]] == self.couleurs_familles[carte_inferieur[1]]:
                        self.score += 2
                        return True
        return False

        
    
    
    def clear(self):
        """Clear la console en fonction de l'OS
        """
        if self.os == "Windows":
            os.system('cls')
        elif self.os == "Linux":
            os.system('clear')
        
        
        
        
    def color_text(self, text:str, color:str):
        """Change la couleur d'un texte si l'utilisateur est sur Windows

        Args:
            text (str): Texte dont il faut changer la couleur
            color (str): Couleur choisie

        Returns:
            (str): Texte coloré
        """
        if platform.system() == "Windows":
            text = f"{colorama.Fore.__getattribute__(color)}{text}{colorama.Fore.WHITE}"
        
        return text
        
            
            
    def text_console(self, text, debut_fin):
        """Ajuste le texte s'il est trop court pour que l'interface soit alignée (ex: "1" -> "1 ", "10" -> "10")

        Args:
            text (_type_): Texte
            debut_fin (_type_): Si le texte est en début ou fin de la carte

        Returns:
            (str): texte
        """
        text = str(text)
        text = self.symboles_familles(text)
        
        if len(text) == 1 and debut_fin == "debut":
            text = text + " "
        elif len(text) == 1 and debut_fin == "fin":
            text = " " + text
            
        text = self.texte_couleurs_familles(text)
        return text


    
            
    def interface(self):
        """ Affiche l'interface
        """
        self.clear()
            
        print("""
                    Talon           │       Carte Piochée       ││          Coeurs            Piques           Carreaux           Trèfles                       
                ┌───────────┐       │       ┌───────────┐       ││       ┌───────────┐     ┌───────────┐     ┌───────────┐     ┌───────────┐                     
                │ {}        │       │       │ {}        │       ││       │ {}        │     │ {}        │     │ {}        │     │ {}        │                     
                │           │       │       │           │       ││       │           │     │           │     │           │     │           │                     
                │     ?     │       │       │           │       ││       │           │     │           │     │           │     │           │                     
                │           │       │       │           │       ││       │           │     │           │     │           │     │           │                     
                │        {} │       │       │        {} │       ││       │        {} │     │        {} │     │        {} │     │        {} │                     
                └───────────┘       │       └───────────┘       ││       └───────────┘     └───────────┘     └───────────┘     └───────────┘                                    
        \n""".format(
            # Haut
                # Talon Haut
                self.text_console(text=self.talon.taille(), debut_fin="debut"),
                
                # Carte 1 Haut
                self.text_console(text=self.carte_piochee[0], debut_fin="debut"), 
                
                
                # Coeurs Haut
                self.text_console(text=self.coeurs.sommet()[0], debut_fin="debut"),
                 
                # Piques Haut
                self.text_console(text=self.piques.sommet()[0], debut_fin="debut"),
                
                # Carreaux Haut
                self.text_console(text=self.carreaux.sommet()[0], debut_fin="debut"), 
                
                # Trèfles Haut
                self.text_console(text=self.trefles.sommet()[0], debut_fin="debut"),


            # Bas
                # Talon Bas
                self.text_console(text=self.talon.taille(), debut_fin="fin"),
                
                # Carte 1 Bas
                self.text_console(text=self.carte_piochee[1], debut_fin="fin"), 
                
                
                # Coeurs Bas
                self.text_console(text=self.coeurs.sommet()[1], debut_fin="fin"), 
                
                # Piques Bas
                self.text_console(text=self.piques.sommet()[1], debut_fin="fin"),
                
                # Carreaux Bas
                self.text_console(text=self.carreaux.sommet()[1], debut_fin="fin"), 
                
                # Trèfles Bas
                self.text_console(text=self.trefles.sommet()[1], debut_fin="fin"),
                   ))
        
        
        # Pour chaque défausse
        for nb_defausse in range(1, 5):
            # On défini la défausse actuel afin de ne pas rendre le code plus visible et on l'affiche
            defausse = self.__getattribute__("defausse" + str(nb_defausse))
            print(self.color_text(text=f"     Défausse {nb_defausse} :\n", color="YELLOW"))
            
            # Si la défausse est vide on affiche quand même un espace vide
            if defausse.pile_vide():
                print('\n'*7)

            else:
                # Si le sommet de la défausse est caché on le rend visible
                if defausse.sommet()[2] == "hidden":
                    defausse.sommet()[2] = "shown"
                    
                # Première ligne
                print(("     " + (defausse.taille()-1)*"┌───────") + "┌───────────┐")
                print("     │ ", end="")
                
                # Deuxième ligne
                # Pour chaque carte de la défausse
                nb_passage = 1
                for carte in defausse.get_all_cards():
                    # Si elle doit être caché
                    if carte[2] == "hidden":
                        # Si c'est le sommet de la défausse
                        if nb_passage == defausse.taille():
                            print("?  " + "       │ ")
                        else:
                            print("?  " + "   │ ", end="")
                    # Si elle doit être affiché
                    else:
                        # Si c'est la dernière
                        if nb_passage == defausse.taille():
                            print(self.text_console(text=carte[0], debut_fin="debut") + self.text_console(text=self.symboles_familles(carte[1]), debut_fin="debut")+ "      │")
                        else:
                            print(self.text_console(text=carte[0], debut_fin="debut") + self.text_console(text=self.symboles_familles(carte[1]), debut_fin="debut")+ "   │ ", end="")
                    nb_passage += 1
                
                # Ligne 3 à 4
                [print("     " +  ((defausse.taille()-1)*"│       " + "│           │")) for _ in range(4)]
                # Dernière ligne
                print("     " + (defausse.taille()-1)*"└───────" + "└───────────┘\n")
        
    
    
    
    def piocher(self):
        """Piocher un carte dans le talon
        """
        # Si le talon est vide
        if self.talon.file_vide():
            # Tant que le talon_temp n'est pas vide
            while not self.talon_temp.file_vide():
                # On prends chaque carte du talon_temp pour la mettre dans le talon
                self.talon.ajout(self.talon_temp.retire())
            # On retire 20 au score
            self.score -= 20
            
        # Si aucune carte n'est présente dans la pioche alors on pioche
        if self.carte_piochee == ['0', '0', 'shown']:
            self.carte_piochee = self.talon.retire()
        # Sinon on ajoute la carte précèdente au talon_temp puis on pioche
        else:
            self.talon_temp.ajout(self.carte_piochee)
            self.carte_piochee = self.talon.retire()
        self.interface()
    
        
    
    def carte_piochee_vers_defausse(self):
        # Vers quelle défausse
        print("Vers quelle défausse (1, 2, 3, 4) ?")
        touche_quelle_defausse = keyboard.read_key()
        while touche_quelle_defausse not in ["1", "2", "3", "4", "&", "é", '"', "'"]:
            touche_quelle_defausse = keyboard.read_key()

        # Défausse temporaire à utiliser pour clarifier le code
        defausse_temp = self.__getattribute__("defausse" + str(self.dico_touche_defausse[touche_quelle_defausse]))
            
        # Si défausse_temp est vide
        if defausse_temp.pile_vide():
            # Alors on peut mettre n'importe quelle carte sans vérification
            defausse_temp.push(self.carte_piochee)
            self.carte_piochee = ['0', '0', 'shown']
            self.interface()
        
        # Sinon on vérifie si la carte peut être déplacée, si oui on la déplace
        elif self.verifier_carte(carte_a_deplacer=self.carte_piochee, carte_inferieur=defausse_temp.sommet(), defausse_ou_famille="defausse"):
            defausse_temp.push(self.carte_piochee)
            self.carte_piochee = ['0', '0', 'shown']
            self.interface()
       
        # Sinon l'action est impossible
        else:
            self.interface()
            print("Action impossible !")
            
            
            
    def carte_piochee_vers_familles(self):
        # Vers quelle famille
        print("Vers quelle famille (1, 2, 3, 4) ?")
        touche_quelle_famille = keyboard.read_key()
        while touche_quelle_famille not in ["1", "2", "3", "4", "&", "é", '"', "'"]:
            touche_quelle_famille = keyboard.read_key()
            
        # Défausse temporaire à utiliser pour clarifier le code            
        defausse_temp = self.__getattribute__(self.dico_touche_familles[touche_quelle_famille])
        
        # Si c'est la première carte
        if (self.nb_cartes == "32" and self.carte_piochee[0] == "7" and defausse_temp.sommet()[2] == self.carte_piochee[1]) \
            or (self.nb_cartes == "52" and self.carte_piochee[0] == "As" and defausse_temp.sommet()[2] == self.carte_piochee[1]):
                    defausse_temp.push(self.carte_piochee)
                    self.carte_piochee = ['0', '0', 'shown']
                    self.interface()

        # Sinon, si le déplacement est possible on l'effectue
        elif self.verifier_carte(carte_a_deplacer=self.carte_piochee, carte_inferieur=defausse_temp.sommet(), defausse_ou_famille="famille"):
            defausse_temp.push(self.carte_piochee)
            self.carte_piochee = ['0', '0', 'shown']
            self.interface()
        
        # Sinon l'action est impossible    
        else:
            self.interface()
            print("Action impossible !")




    def carte_defausse_vers_familles(self):
        # De quelle défausse
        print("De quelle défausse (1, 2, 3, 4) ?")
        touche_quelle_defausse = keyboard.read_key()
        while touche_quelle_defausse not in ["1", "2", "3", "4", "&", "é", '"', "'"]:
            touche_quelle_defausse = keyboard.read_key()
            
        while self.__getattribute__("defausse" + self.dico_touche_defausse[str(touche_quelle_defausse)]).pile_vide():
            while touche_quelle_defausse not in ["1", "2", "3", "4", "&", "é", '"', "'"]:
                touche_quelle_defausse = keyboard.read_key()
            
        time.sleep(0.5)
        
        # Vers quelle famille
        print("Vers quelle famille (1, 2, 3, 4) ?")
        touche_quelle_famille = keyboard.read_key()
        while touche_quelle_famille not in ["1", "2", "3", "4", "&", "é", '"', "'"]:
            touche_quelle_famille = keyboard.read_key()
        

        # Défausse et famille temporaires à utiliser pour clarifier le code            
        defausse = self.__getattribute__("defausse" + self.dico_touche_defausse[str(touche_quelle_defausse)])
        famille = self.__getattribute__(self.dico_touche_familles[touche_quelle_famille])


        # Si la defausse n'est pas vide
        if not defausse.pile_vide():
            # Si le sommet de la défausse est la première carte du jeu (7 ou As)
            if defausse.sommet()[0] == self.cartes[0]:
                # Si la famille est la même on déplace la carte
                if defausse.sommet()[1] == famille.sommet()[2]:
                    famille.push(defausse.pop())
                    self.interface()
            # Sinon on vérifie le déplacement et on l'effectue ou non
            elif self.verifier_carte(carte_a_deplacer=defausse.sommet(), carte_inferieur=famille.sommet(), defausse_ou_famille="famille"):
                famille.push(defausse.pop())
                self.interface()
                    
        # Sinon l'action est impossible
        else:
            self.interface()
            print("Action impossible !")




    def carte_defausse_vers_defausse(self):
        # De quelle défausse
        print("De quelle défausse (1, 2, 3, 4) ?")
        touche_1_quelle_defausse = keyboard.read_key()
        while touche_1_quelle_defausse not in ["1", "2", "3", "4", "&", "é", '"', "'"] and True:
            touche_1_quelle_defausse = keyboard.read_key()

        time.sleep(0.5)
        
        # Vers quelle défausse
        print("Vers quelle defausse (1, 2, 3, 4) ?")
        touche_2_quelle_defausse = keyboard.read_key()
        while touche_2_quelle_defausse not in ["1", "2", "3", "4", "&", "é", '"', "'"]:
            touche_2_quelle_defausse = keyboard.read_key()


        # Défausses temporaires à utiliser pour clarifier le code            
        defausse_temp_1 = self.__getattribute__("defausse" + str(self.dico_touche_defausse[touche_1_quelle_defausse]))
        defausse_temp_2 = self.__getattribute__("defausse" + str(self.dico_touche_defausse[touche_2_quelle_defausse]))

        # Si l'utilisateur a choisi les 2 mêmes défausses ou si la 1ère défausse est vide
        if defausse_temp_1 == defausse_temp_2 or defausse_temp_1.pile_vide():
            self.interface()
            print("Action Impossible")
        
        # Si la 2ème défausse est vide ou 
        elif defausse_temp_2.pile_vide() or self.verifier_carte(carte_a_deplacer=defausse_temp_1.sommet(), carte_inferieur=defausse_temp_2.sommet(), defausse_ou_famille="defausse"):
            defausse_temp_2.push(defausse_temp_1.pop())
            self.interface()
            
            
            
            
    def quitter(self):
        print("Voulez-vous vraiment quitter ?\nAppuyez sur O ou Y pour valider, sinon n'importe quelle autre touche pour refuser.")
        time.sleep(0.5)
        if keyboard.read_key() in ["o", "O", "y", "Y"]:
            exit()
        else:
            partie1.interface()
            
            
        



partie1 = Game()

partie1.interface()
while True:
    print(f"Score : {partie1.score}")
    # Indications
    print("T : Piocher\nD : Déplacer une carte\nX : Arrêter la partie\n")
    
    # Sécurité pour empêcher l'appui successif
    #time.sleep(0.5)
    
    # Enrigistrment touche
    touche = keyboard.read_key()
    while touche not in ["x", "X", "d", "D", "t", "T"]:
        touche = keyboard.read_key()
    
    # Si touche = T
    if touche in ["t", "T"]:
        partie1.piocher()

    # Si touche = D
    if touche in ["d", "D"]:
        print('A : Carte piochée vers défausse\nB : Carte piochée vers familles\nC : Carte défausse vers familles\nE : Carte défausse vers défausse')
        # Sécurité pour empêcher l'appui successif
        time.sleep(0.5)
        # Enrigistrment touche
        touche = keyboard.read_key()
        while touche not in ["a", "A", "b", "B", "c", "C", "e", "E"]:
            touche = keyboard.read_key()

        if touche in ["a", "A"]:
            partie1.carte_piochee_vers_defausse()
        
        elif touche in ["b", "B"]:
            partie1.carte_piochee_vers_familles()

        elif touche in ["c", "C"]:
            partie1.carte_defausse_vers_familles()
            
        elif touche in ["e", "E"]:
            partie1.carte_defausse_vers_defausse()

    # Si touche = X
    elif touche in ["x", "X"]:
        partie1.clear()
        partie1.quitter()


    partie1.verifier_victoire()
    
        
    
