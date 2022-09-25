# =====================================
#      IMPORTATIONS DES LIBRAIRIES
# =====================================

# Tkinter
from tkinter import *
from tkinter import ttk, filedialog
from PIL import ImageTk, Image

# Necessaires au bon fonctionnement d'un jeu de carte
import Carte
import JeuCarte
import pile as p

# Supplémentaires
import random
import colorama as cl
import os
import keyboard
import platform





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
        print("Voulez vous jouer à 32 ou 52 cartes ou alors laisser le hasard décider ? (1/2/3)")

        # En attente du choix de l'utilisateur : uniquement s'il a pressé 1, 2 ou 3 en minuscule ou en majuscule
        keyboard_nb_cartes = keyboard.read_key()
        while keyboard_nb_cartes not in ["1", "&", "2", "é", "3", '"']:
            keyboard_nb_cartes = keyboard.read_key()
            
        # Return le nombre de cartes
        if keyboard.read_key() in ["1", "&"]:
            self.nb_cartes = "32"
        elif keyboard.read_key() in ["2", "é"]:
            self.nb_cartes = "52"
        else:
            self.nb_cartes = random.choice(seq=["32", "52"])
            
    
        self.carreau = "♦"
        self.pique =  "♠"
        self.coeur = "♥"
        self.trefle = "♣"


        # Définition du jeu en fonction du nombre de cartes
        self.jeu_cartes = JeuCarte.JeuCarte(self.nb_cartes)
        self.jeu_cartes.melangerJeu()

        # Définition du talon et de la main en cours
        self.talon = p.Pile(self.jeu_cartes.getJeu())
        self.talon_en_main = p.Pile(self.talon.get_3_first_cards())

        # Définition des 4 défausses
        self.defausse1 = p.Pile()
        for d1 in range(4):
            self.defausse1.push(self.talon.pop())
        print(self.defausse1.get_all_cards())
        """
        self.defausse2 = p.Pile()
        for d2 in range(3):
            self.defausse2.push(self.talon.pop())
            
        self.defausse3 = p.Pile()
        for d3 in range(2):
            self.defausse3.push(self.talon.pop())
            
        self.defausse4 = p.Pile()"""
        

        # Définition des 4 familles
        self.piques = p.Pile()
        self.carreaux = p.Pile()
        self.trefles = p.Pile()
        self.coeurs = p.Pile()




    def verifier_victoire(self):
        if int(self.nb_cartes) == self.piques.taille() + self.carreaux.taille() + self.trefles.taille() + self.coeurs.taille():
            return True
        else:
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
            str: Texte coloré
        """
        if platform.system() == "Windows":
            text = f"{cl.Fore.__getattribute__(color)}{text}{cl.Fore.WHITE}"
        
        return text
        
            
            
    def text_console(self, text, debut_fin):
        text = str(text)
        text = text.replace('Carreau', self.carreau)
        text = text.replace('Pique', self.pique)
        text = text.replace('Coeur', self.coeur)
        text = text.replace('Trèfle', self.trefle)
        
        if len(text) == 1 and debut_fin == "debut":
            text = text + " "
        elif len(text) == 1 and debut_fin == "fin":
            text = " " + text
            
        return text


    
            
    def interface(self):
        #self.clear()
        
        print("""\n\n\n
                    Talon           │          Carte 1            Carte 2           Carte 3           ││          Coeurs            Piques           Carreaux           Trèfles                       
                ┌───────────┐       │       ┌───────────┐      ┌───────────┐     ┌───────────┐        ││       ┌───────────┐     ┌───────────┐     ┌───────────┐     ┌───────────┐                     
                │ {}        │       │       │ {}        │      │ {}        │     │ {}        │        ││       │ {}        │     │ {}        │     │ {}        │     │ {}        │                     
                │           │       │       │           │      │           │     │           │        ││       │           │     │           │     │           │     │           │                     
                │     ?     │       │       │           │      │           │     │           │        ││       │           │     │           │     │           │     │           │                     
                │           │       │       │           │      │           │     │           │        ││       │           │     │           │     │           │     │           │                     
                │        {} │       │       │        {} │      │        {} │     │        {} │        ││       │        {} │     │        {} │     │        {} │     │        {} │                     
                └───────────┘       │       └───────────┘      └───────────┘     └───────────┘        ││       └───────────┘     └───────────┘     └───────────┘     └───────────┘                                    
        """.format(
            # Haut
                # Talon Haut
                self.text_console(text=self.talon.taille(), debut_fin="debut"),
                
                
                # Carte 1 Haut
                self.text_console(text=self.talon_en_main.get_all_cards()[0][0], debut_fin="debut"), 
                # Carte 2 Haut
                self.text_console(text=self.talon_en_main.get_all_cards()[1][0], debut_fin="debut"),
                # Carte 3 Haut
                self.text_console(text=self.talon_en_main.get_all_cards()[2][0], debut_fin="debut"),
                
                
                # Coeurs Haut
                self.text_console(text="R", debut_fin="debut"), 
                # Piques Haut
                self.text_console(text="R", debut_fin="debut"),
                # Carreaux Haut
                self.text_console(text="R", debut_fin="debut"), 
                # Trèfles Haut
                self.text_console(text="R", debut_fin="debut"),


            # Bas
                # Talon Bas
                self.text_console(text=self.talon.taille(), debut_fin="fin"),
                
                # Carte 1 Bas
                self.text_console(text=self.talon_en_main.get_all_cards()[0][1], debut_fin="fin"), 
                
                # Carte 2 Bas
                self.text_console(text=self.talon_en_main.get_all_cards()[1][1], debut_fin="fin"),
                # Carte 3 Bas
                self.text_console(text=self.talon_en_main.get_all_cards()[2][1], debut_fin="fin"),
                
                
                # Coeurs Bas
                self.text_console(text="R", debut_fin="fin"), 
                
                # Piques Bas
                self.text_console(text="R", debut_fin="fin"),
                
                # Carreaux Bas
                self.text_console(text="R", debut_fin="fin"), 
                
                # Trèfles Bas
                self.text_console(text="R", debut_fin="fin"),
                   ))
        
        
        print((self.defausse1.taille()-1)*"┌───────" + "┌───────────┐")
        print(self.defausse1.get_all_cards())
        for carte in self.defausse1.get_all_cards():
            print(carte)

                                
                
            


"""
fenetre = Root()
# Clear la console
#clear()

# Affichage du nom du jeu
print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
print(Fore.YELLOW + "   Jouer au Solitaire (32/52) ?      " + Fore.WHITE)
print("___________________________________")

# Demande à l'utilisateur le nombre de cartes qu'il souhaite
nb_cartes = input("\nNombre de cartes (32/52) : ")

# Si il a choisi 32 ou 52 la partie se lance
if nb_cartes in ["32", "52"]:
    partie = Game(nb_cartes)

# Sinon elle d'arrête
else:
    print('Nombre de cartes invalide')
    print('Arrêt du programme')
    exit()
"""




partie1 = Game()
partie1.interface()


