import Carte
import JeuCarte
import pile as p
import random
from colorama import Fore
import os


"""
Class game
"""

# Fonction pour clear la console
clear = lambda:os.system('clear')

class Game:
    
    def __init__(self, nb_cartes:str):
        assert nb_cartes in ["32", "52"], "Le nombre de cartes doit être égal à 32 ou 52"
        self.jeu_cartes = JeuCarte.JeuCarte(nb_cartes)
        self.jeu_cartes.melangerJeu()
        
        self.talon = p.Pile(self.jeu_cartes.getJeu())
        self.talon_pioche = p.Pile()
        
        self.defausse1 = p.Pile()
        self.defausse2 = p.Pile()
        self.defausse3 = p.Pile()
        self.defausse4 = p.Pile()
        
        self.piques = p.Pile()
        self.carreaux = p.Pile()
        self.trefles = p.Pile()
        self.coeurs = p.Pile()
        
        
        print(self)
        
        
        exit()
        
        

# Clear la console
clear()

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
    
    
    
while True:
    pass