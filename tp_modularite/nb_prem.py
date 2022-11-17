########### partie import des modules ###########
import fcts_turtle

########### définition des fonctions ############
# définition des fonctions du fichier main
# pour le calcul des nombres premiers
def est_premier(entier):
    """
    teste la primalité d'un nombre
    :param entier: (int) entier supérieur à 2
    :return: (bool) True s'il s'agit d'un entier, False sinon
    """
    for i in range(2, entier):
        if (entier % i == 0):
            return False
    return True

def prem(entier):
    """
    donne la liste des nombres premiers inférieurs à un entier donné
    :param entier: (int) entier strictement positif
    :return: (list) liste des nombres premiers inférieurs à l'entier donné
    """
    liste_prem=[]
    for nb in range(entier+1):
        if est_premier(nb):
            liste_prem.append(nb)
    return liste_prem

########### corps du programme ##################
### à exécuter si fichier main ##################
if __name__ == '__main__':
    # affichage de l'aide du module
    #print(dir(fcts_turtle))
    #help(fcts_turtle)
    #print(fcts_turtle.__name__)
   
    # saisie d'un nombre entier supérieur ou égal à 2
    
    N = int(input('Nombre entier supérieur ou égal à 2 : '))
    assert N >= 2, "nb < 2"
    
    # calcul d'une liste de nombre premiers
    
    liste_premiers = prem(N)
    
    # appel de la fonction de dessin du module
    fcts_turtle.spirale(liste_premiers, N)
#################################################