# =====================================
#      IMPORTATIONS DES LIBRAIRIES
# =====================================


# Necessaires au bon fonctionnement d'un jeu de carte
import Carte
import JeuCarte
import pile as p
import file as f

# Supplémentaires
import random
import colorama as cl
import os
import keyboard
import platform
import time





# class Root
class Console:
    
    
        
        
            
            
    """
    def aficher_carte(self, famille:str="?", valeur:str="?"):
        Affiche une carte caspécifique

        Args:
            famille (str, optional): Famille de carte (carreau, trefle, pique, coeur). Defaults to "?".
            valeur (str, optional): Valeur de la carte (5, 8, K, etc). Defaults to "?".
        
        
        # Première ligne
        print("┌" + "─"*11 + "┐")
        
        # Deuxième ligne
        print(f"│ {valeur}{' '*(10-len(valeur))}│")
                
        # Troisième ligne
        print(f"│{' '*11}│")
        
        # Ligne du milieu (Quatrième)
        print(f"│{' '*5}{famille}{' '*5}│")
        
        # Antépénultième ligne
        print(f"│{' '*11}│")
        
        # Avant dernière ligne
        print(f"│{' '*(10-len(valeur))}{valeur} │")
                
        # Dernière ligne
        print("└" + "─"*11 + "┘")"""
        



# class Game
class Game:

    def __init__(self):
        """Affiche le menu principal du jeu et demande à l'utilisateur le nombre de cartes à utiliser

        Returns:
            str: Nombre de cartes
        """
        
        self.os = platform.system()
        
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

        # En attente du choix de l'utilisateur : uniquement s'il a pressé 1, 2 ou 3 en minuscule ou en majuscule
        keyboard_nb_cartes = keyboard.read_key()
        while keyboard_nb_cartes not in ["1", "&", "2", "é"]:
            keyboard_nb_cartes = keyboard.read_key()
            
        # Return le nombre de cartes
        if keyboard.read_key() in ["1", "&"]:
            self.nb_cartes = "32"
            self.cartes = ["7", "8", "9", "10", "V", "D", "R", "As"]
        elif keyboard.read_key() in ["2", "é"]:
            self.nb_cartes = "52"
            self.cartes = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "V", "D", "R", "As"]
            
    
        self.carreau = "♦"
        self.pique =  "♠"
        self.coeur = "♥"
        self.trefle = "♣"
        
        
        self.mouvements = 0

        # Définition du jeu en fonction du nombre de cartes
        self.jeu_cartes = JeuCarte.JeuCarte(self.nb_cartes)
        self.jeu_cartes.melangerJeu()

        # Définition du talon de la carte piochée et des cartes piochées ignorées
        self.talon = f.File(self.jeu_cartes.getJeu())
        self.carte_piochee = self.talon.retire()

        # Définition des 4 défausses
        self.defausse1 = p.Pile()
        for _ in range(4):
            c = self.talon.retire()
            c[2] = 'hidden'
            self.defausse1.push(c)
            
        self.defausse2 = p.Pile()
        for _ in range(3):
            c = self.talon.retire()
            c[2] = 'hidden'
            self.defausse2.push(c)
            
        self.defausse3 = p.Pile()
        for _ in range(2):
            c = self.talon.retire()
            c[2] = 'hidden'
            self.defausse3.push(c)
            
        self.defausse4 = p.Pile()
        c = self.talon.retire()
        c[2] = 'hidden'
        self.defausse4.push(c)
        #print(self.defausse1.get_all_cards())
        #exit()
        

        # Définition des 4 familles
        self.piques = p.Pile()
        self.piques.push(["0", "0", "Pique"])
        self.carreaux = p.Pile()
        self.carreaux.push(["0", "0", "Carreau"])
        self.trefles = p.Pile()
        self.trefles.push(["0", "0", "Trèfle"])
        self.coeurs = p.Pile()
        self.coeurs.push(["0", "0", "Coeur"])
        
        self.couleurs_familles = {"Pique": "noir", "Coeur": "rouge", "Carreau": "rouge", "Trèfle": "noir"}


    def verifier_victoire(self):
        """Vérifie si la partie a été gagnée

        Returns:
            (bool)": True si oui / False si non
        """
        if int(self.nb_cartes) == self.piques.taille() + self.carreaux.taille() + self.trefles.taille() + self.coeurs.taille():
            return True
        else:
            return False



    
    
         
    def symboles_familles(self, text):
        """Remplace le texte par le symbole correspondant (ex: "Carreau" -> "♦")

        Args:
            text (_type_): texte à modifier

        Returns:
            str: texte
        """
        text = str(text)
        text = text.replace('Carreau', self.carreau).replace('Pique', self.pique).replace('Coeur', self.coeur).replace('Trèfle', self.trefle)
        return text
    
    
    def texte_couleurs_familles(self, text):
        """Met en rouge si la famille est carreau ou coeur

        Args:
            text: text

        Returns:
            text: text
        """
        if self.carreau in text or self.coeur in text:
            return self.color_text(text=text, color="RED")
        else:
            return text
        
    
    def verifier_carte(self, carte_a_deplacer:list, carte_inferieur:list):
        """Vérifie si un déplacement de carte est possible

        Args:
            carte_a_deplacer (list): Carte qui va être déplacée sur une autre
            carte_inferieur (list): Carte qui va reçevoir la carte à déplacer

        Returns:
            (bool): True si possible / False si impossible
        """
        
        if carte_a_deplacer[0] == "As":
            return False
        
        for x in range(len(self.cartes)):
            
            if carte_a_deplacer[0] == self.cartes[x] and carte_inferieur[0] == self.cartes[x+1]:
                if self.couleurs_familles[carte_a_deplacer[1]] != self.couleurs_familles[carte_inferieur[1]]:
                    return True
        
        return False
    
    
    
    
    def clear(self):
        """Clear la console en fonction de l'os
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
            text = f"{cl.Fore.__getattribute__(color)}{text}{cl.Fore.WHITE}"
        
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
        """.format(
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
        
        
        print("\n\n")
        
        for nb_defausse in range(1, 5):
            
            if self.__getattribute__("defausse" + str(nb_defausse)).sommet()[2] == "hidden":
                self.__getattribute__("defausse" + str(nb_defausse)).sommet()[2] = "shown"
                
            
            print(self.color_text(text=f"     Défausse {nb_defausse} :\n", color="YELLOW"))
            print(("     " + (self.__getattribute__("defausse" + str(nb_defausse)).taille()-1)*"┌───────") + "┌───────────┐")
            print("     │ ", end="")
            x = 1
            for carte in self.__getattribute__("defausse" + str(nb_defausse)).get_all_cards():
                if carte[2] == "hidden":
                    if x == self.__getattribute__("defausse" + str(nb_defausse)).taille():
                        print("?  " + "       │ ")
                    else:
                        print("?  " + "   │ ", end="")
                    x += 1
                else:
                    if x == self.__getattribute__("defausse" + str(nb_defausse)).taille():
                        print(self.text_console(text=carte[0], debut_fin="debut") + self.text_console(text=self.symboles_familles(carte[1]), debut_fin="debut")+"      │")
                    else:
                        print(self.text_console(text=carte[0], debut_fin="debut") + self.text_console(text=self.symboles_familles(carte[1]), debut_fin="debut")+ "   │ ", end="")
                    x += 1
                
            [print("     " +  ((self.__getattribute__("defausse" + str(nb_defausse)).taille()-1)*"│       " + "│           │")) for _ in range(4)]
            print("     " + (self.__getattribute__("defausse" + str(nb_defausse)).taille()-1)*"└───────" + "└───────────┘\n")
        
    
    
    
    def piocher(self):
        """Piocher un carte dans le talon
        """
        if self.carte_piochee == ['0', '0', 'shown']:
            self.carte_piochee = self.talon.retire()
        else:
            self.talon.ajout(self.carte_piochee)
            self.carte_piochee = self.talon.retire()
        self.interface()
    
        
    
    def carte_piochee_vers_defausse(self):
        print("1, 2, 3, 4")
        touche_quelle_defausse = keyboard.read_key()
        while touche_quelle_defausse not in ["1", "2", "3", "4", "&", "é", '"', "'"]:
            touche_quelle_defausse = keyboard.read_key()
            
            
        if touche_quelle_defausse in ["1", "&"] and self.verifier_carte(carte_a_deplacer=self.carte_piochee, carte_inferieur=self.defausse1.sommet()) == True:
                self.defausse1.push(self.carte_piochee)
                self.carte_piochee = ['0', '0', 'shown']
                self.interface()
                
        elif touche_quelle_defausse in ["2", "é"] and self.verifier_carte(carte_a_deplacer=self.carte_piochee, carte_inferieur=self.defausse2.sommet()) == True:
                self.defausse2.push(self.carte_piochee)
                self.carte_piochee = ['0', '0', 'shown']
                self.interface()
                
        elif touche_quelle_defausse in ["3", '"'] and self.verifier_carte(carte_a_deplacer=self.carte_piochee, carte_inferieur=self.defausse3.sommet()) == True:
                self.defausse3.push(self.carte_piochee)
                self.carte_piochee = ['0', '0', 'shown']
                self.interface()
                
        elif touche_quelle_defausse in ["4", "'"] and self.verifier_carte(carte_a_deplacer=self.carte_piochee, carte_inferieur=self.defausse4.sommet()) == True:
                self.defausse4.push(self.carte_piochee)
                self.carte_piochee = ['0', '0', 'shown']
                self.interface()
        
        else:
            self.interface()
            print("Action impossible !")
            
            
            
    def carte_piochee_vers_familles(self):
        print("1, 2, 3, 4")
        touche_quelle_famille = keyboard.read_key()
        while touche_quelle_famille not in ["1", "2", "3", "4", "&", "é", '"', "'"]:
            touche_quelle_famille = keyboard.read_key()
        
        dico_touche_familles = {"1": "coeurs", "&": "coeurs", 
                "2": "piques", "é": "piques",
                "3": "carreaux", '"': "carreaux",
                "4": "trefles", "'": "trefles"}
        
        
        if self.carte_piochee[0] == "As":
            if self.__getattribute__(dico_touche_familles[touche_quelle_famille]).sommet()[2] == self.carte_piochee[1]:
                self.__getattribute__(dico_touche_familles[touche_quelle_famille]).push(self.carte_piochee)
                self.carte_piochee = ['0', '0', 'shown']
                self.interface()
        
        
        elif self.verifier_carte(carte_a_deplacer=self.carte_piochee, carte_inferieur=self.__getattribute__(dico_touche_familles[touche_quelle_famille])):
            self.__getattribute__(dico_touche_familles[touche_quelle_famille]).push(self.carte_piochee)
            self.carte_piochee = ['0', '0', 'shown']
            self.interface()
            
        else:
            self.interface()
            print("Action impossible !")



    def carte_defausse_vers_familles(self):
        print("1, 2, 3, 4")
        touche_quelle_defausse = keyboard.read_key()
        dico_touche_defausse = {"1": "1", "&": "1", 
                "2": "2", "é": "2",
                "3": "3", '"': "3",
                "4": "4", "'": "4"}
                
        while touche_quelle_defausse not in ["1", "2", "3", "4", "&", "é", '"', "'"] and True:
            touche_quelle_defausse = keyboard.read_key()

        
        while self.__getattribute__("defausse" + dico_touche_defausse[str(touche_quelle_defausse)]).pile_vide() == True:
            touche_quelle_defausse = keyboard.read_key()
        
        time.sleep(1)
        print("1, 2, 3, 4")
        touche_quelle_famille = keyboard.read_key()
        while touche_quelle_famille not in ["1", "2", "3", "4", "&", "é", '"', "'"]:
            touche_quelle_famille = keyboard.read_key()
        
        dico_touche_familles = {"1": "coeurs", "&": "coeurs", 
                "2": "piques", "é": "piques",
                "3": "carreaux", '"': "carreaux",
                "4": "trefles", "'": "trefles"}
        
        print(touche_quelle_defausse, touche_quelle_famille)
        defausse = self.__getattribute__("defausse" + dico_touche_defausse[str(touche_quelle_defausse)])
        famille = self.__getattribute__(dico_touche_familles[touche_quelle_famille])


        if defausse.sommet()[0] == "As":
            if defausse.sommet()[1] == famille.sommet()[2]:
                famille.push(defausse.pop())
                self.interface()
                exit()
        

            
        else:
            self.interface()
            print("Action impossible !")







partie1 = Game()

partie1.interface()
while True:
    print(f"Mouvements : {partie1.mouvements}")
    # Indications
    print("P : Piocher\nX : Arrêter la partie\nA : Carte piochée vers défausse\nB : Carte piochée vers familles\nC : Carte défausse vers familles")
    
    # Sécurité pour empêcher l'appui successif
    time.sleep(1)
    
    
    touche = keyboard.read_key()
    while touche not in ["p", "P", "x", "X", "a", "A", "b", "B", "c", "C"]:
        touche = keyboard.read_key()
    print(touche)
    
    if touche in ["p", "P"]:
        partie1.mouvements += 1
        partie1.piocher()
        
    elif touche in ["x", "X"]:
        partie1.clear()
        print("Arrêt du programme")
        exit()
        
    elif touche in ["a", "A"]:
        partie1.carte_piochee_vers_defausse()
        
    elif touche in ["b", "B"]:
        partie1.carte_piochee_vers_familles()

    elif touche in ["c", "C"]:
        partie1.carte_defausse_vers_familles()
