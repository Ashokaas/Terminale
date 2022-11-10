import os
import sqlite3

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "cinema_v2.sqlite")

connexion = sqlite3.connect(db_path)
curseur = connexion.cursor()
resultat = curseur.execute("SELECT * FROM Films WHERE ")

for ligne in resultat:
    print(ligne)

connexion.close()

