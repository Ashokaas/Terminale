import os
import sqlite3


class database:
    """Class which manages a database of cinemas
    """
    def __init__(self, path:str):
        """Initialization

        Args:
            path (str): Database path
        """
        self.path = os.path.join(os.path.dirname(os.path.abspath(__file__)), path)
        self.id_cinema = 1
    

    def adresses_cinemas(self):
        connexion = sqlite3.connect(self.path)
        curseur = connexion.cursor()
        resultat = curseur.execute("SELECT * FROM Cinemas;").fetchall()
        connexion.close()
        return resultat
    
    
    def select_cinema(self, id_cinema):
        self.cinema_selected = id_cinema
        
        
    def get_films(self):
        connexion = sqlite3.connect(self.path)
        curseur = connexion.cursor()
        resultat = curseur.execute("""SELECT Projeter.idProjection, Films.idFilm, Films.titre, Films.annee 
                                   FROM Films
                                   INNER JOIN Projeter 
                                   ON Projeter.idCinema = ? 
                                   WHERE Projeter.idFilm = Films.idFilm;
                                   """, 
                                   (self.cinema_selected, )).fetchall()
        connexion.close()
        return resultat


os.system("clear")

base_de_donnees = database(path="cinema_v2.sqlite")

for resultat in base_de_donnees.adresses_cinemas():
    print(resultat)

base_de_donnees.select_cinema(id_cinema=1)


for resultat in base_de_donnees.get_films():
    print(resultat)

oui
    
    
