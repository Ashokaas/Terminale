"""
    TODO : présentation du module
"""
######## partie import des modules externes #######
import turtle

######## définition des fonctions du module #######

# fonction de dessin de la fenêtre

def create_window(largeur, hauteur):
    window = turtle.Screen()
    window.setup(largeur, hauteur)

def close_windows():
    turtle.exitonclick()

# fonction spirale(liste_premiers, N)
def spirale(premiers, N, L=600, h=600):
    """
    représente la spirale des nombres premiers

    Params
    ------
    :param premiers: list
        les nombres premiers
    :param N: int
        dernière valeur de la spirale
    :param L: int
        dimension du rectangle en largeur. 600px par défaut
    :param h: int
        dimenseion du rectangle en hauteur. 600px par défaut

    Principe
    --------
    Les nombres sont écrits sur la spirale. En rouge si le nombre est premier, en noir sinon.

    Appel
    -----
    >>> spirale(premiers, 100) # tracé de la spirale avec la liste de nombres premiers mis en argument, jusqu'à N=100.
    """
    create_window(L, h)
    
    turtle.begin_fill()
    for i in range(N):
        if i < 10:
            l = 10
        else:
            l = i
        
        turtle.forward(l*2)
        turtle.right(20)
        if i in premiers:
            turtle.color('red')
        turtle.write(i)
        turtle.color('black')
    close_windows()
    #TODO

    # création de la spirale
    #TODO





###################################################