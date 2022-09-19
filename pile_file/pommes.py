from random import randint
from pile_2_noeud import Pile2noeud


class PanierAdam:
    def __init__(self):
        self.pommes = Pile2noeud()
        self.tps = 0
    
    def collecte(self):
        serie = 0
        while self.pommes.calculer_taille() != 25:
            self.pommes.empiler("pomme")
            if serie % 3 == 0:
                if randint(0, 3) in [0, 1]:
                    self.pommes.depiler()
                serie = 0
            serie += 1
            self.tps += 10
        return self.tps
    
panier_1 = PanierAdam()

oui = 0
for e in range(1000000):
    oui += panier_1.collecte()/60
print(round(oui/1000000, 2))
            
            