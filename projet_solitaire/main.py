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
from colorama import Fore
import os



# Fonction pour clear la console
clear = lambda:os.system('clear')



# class Root
class Root:
    def __init__(self):

        self.bg_color = "green"
                # -- Configuration de la fenêtre
        self.root = Tk()
        self.root.title("Solitaire v3")
        self.root.resizable(False, False)
        self.root.configure(bg=self.bg_color)

        hauteur = 600
        largeur = 850
        self.root.geometry(str(largeur) + 'x' + str(hauteur))

        # -- Frame Talon
        self.frame_talon = Frame(self.root, width=200, bg="blue")
        self.frame_talon.pack(fill=Y, side=LEFT)
        self.frame_talon.pack_propagate(False)


        self.label_talon = Label(self.frame_talon, text="Talon")
        self.label_talon.pack()

        image = Image.open("img/carte_dos.jpg")
        photo = ImageTk.PhotoImage(image)


        canvas = Canvas(self.frame_talon, width=image.size[0], height=image.size[1])
        canvas.create_image(0,0, image=photo)
        canvas.pack()




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




