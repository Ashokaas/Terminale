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
    
    def __init__(self):
        self.carreau = self.color_text(text="♦", color="RED")
        self.pique =  self.color_text(text="♠", color="BLACK")
        self.coeur = self.color_text(text="♥", color="RED")
        self.trefle = self.color_text(text="♣", color="BLACK")
        self.nb_cartes = None
        
        self.os = platform.system()
        
        self.clear()
        
        
    
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
        
    
    def main_menu(self):
        """Affiche le menu principal du jeu et demande à l'utilisateur le nombre de cartes à utiliser

        Returns:
            str: Nombre de cartes
        """
        
        self.clear()
        
        # Titre du jeu (ASCII Art : https://fsymbols.com/generators/carty/)
        print(f"""  
            ░██████╗░█████╗░██╗░░░░░██╗████████╗░█████╗░██╗██████╗░███████╗
            ██╔════╝██╔══██╗██║░░░░░██║╚══██╔══╝██╔══██╗██║██╔══██╗██╔════╝
            ╚█████╗░██║░░██║██║░░░░░██║░░░██║░░░███████║██║██████╔╝█████╗░░
            ░╚═══██╗██║░░██║██║░░░░░██║░░░██║░░░██╔══██║██║██╔══██╗██╔══╝░░
            ██████╔╝╚█████╔╝███████╗██║░░░██║░░░██║░░██║██║██║░░██║███████╗
            ╚═════╝░░╚════╝░╚══════╝╚═╝░░░╚═╝░░░╚═╝░░╚═╝╚═╝╚═╝░░╚═╝╚══════╝
                        
                    {cl.Fore.YELLOW}Appuyez sur ESPACE pour commencer une partie !{cl.Fore.WHITE}
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
            
        return self.nb_cartes
            
            

    def aficher_carte(self, famille:str="?", valeur:str="?"):
        """Affiche une carte caspécifique

        Args:
            famille (str, optional): Famille de carte (carreau, trefle, pique, coeur). Defaults to "?".
            valeur (str, optional): Valeur de la carte (5, 8, K, etc). Defaults to "?".
        """
        
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
        print("└" + "─"*11 + "┘")
        



# class Game
class Game:

    def __init__(self, nb_cartes:str):
        # Asssertion pour le nombre de cartes
        assert nb_cartes in ["32", "52"], "Le nombre de cartes doit être égal à 32 ou 52"

        self.nb_cartes = nb_cartes

        # Définition du jeu en fonction du nombre de cartes
        self.jeu_cartes = JeuCarte.JeuCarte(nb_cartes)
        self.jeu_cartes.melangerJeu()

        # Définition du talon et de la main en cours
        self.talon = p.Pile(self.jeu_cartes.getJeu())
        self.talon_en_main = p.Pile(self.talon.get_3_first_cards())

        # Définition des 4 défausses
        self.defausse1 = p.Pile()
        self.defausse2 = p.Pile()
        self.defausse3 = p.Pile()
        self.defausse4 = p.Pile()

        # Définition des 4 types
        self.piques = p.Pile()
        self.carreaux = p.Pile()
        self.trefles = p.Pile()
        self.coeurs = p.Pile()


        print(self)


        exit()



    def verifier_victoire(self):
        if int(self.nb_cartes) == self.piques.taille + self.carreaux.taille + self.trefles.taille + self.coeurs.taille:
            return True
        else:
            return False



#fenetre = Root()
# Clear la console
#clear()
"""
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
    exit()"""




console = Console()
console.aficher_carte(famille=console.trefle, valeur="K")
#nb_cartes = console.main_menu()
#partie = Game(nb_cartes=nb_cartes)


