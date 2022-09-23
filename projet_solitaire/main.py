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



# Fonction pour clear la console
clear = lambda:os.system('cls')



# class Root
class Console:
    
    def __init__(self):
        self.carreau = cl.Fore.RED + "♦" + cl.Fore.WHITE
        self.pique =  cl.Fore.BLACK + "♠" + cl.Fore.WHITE
        self.coeur = cl.Fore.RED + "♥" + cl.Fore.WHITE
        self.trefle = cl.Fore.BLACK + "♣" + cl.Fore.WHITE
        clear()
    
    def main_menu(self):
        clear()
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
        clear()
        print("Voulez vous jouer à 32 ou 52 cartes ?\n< >")
        #keyboard.wait('left', )
    

    def aficher_carte(self, type=None, valeur=None):
        print("┌" + "─"*11 + "┐")
        
        
        if valeur:
            if len(valeur) == 1:
                print(f"│ {valeur}{' '*9}│")
            elif len(valeur) > 1:
                print(f"│ {valeur}{' '*8}│")
                
        print(f"│{' '*11}│")
        print(f"│{' '*5}{type}{' '*5}│")
        print(f"│{' '*11}│")
        
        if valeur:
            if len(valeur) == 1:
                print(f"│{' '*9}{valeur} │")
            elif len(valeur) > 1:
                print(f"│{' '*8}{valeur} │")
                
        
        
        print("└" + "─"*11 + "┘")
        



console = Console()
console.aficher_carte(type=console.trefle, valeur="10")
console.main_menu()




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




