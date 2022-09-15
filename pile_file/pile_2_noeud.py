import noeud

class Pile_2_noeud:
    def __init__(self):
        self.top = None
        
    def empiler(self, valeur):
        nouveau_noeud = noeud.Noeud(valeur)
        nouveau_noeud.set_ref(self.top)
        self.top = nouveau_noeud
        return self.top.get_item()
        
    def depiler(self):
        if self.etre_vide() == False:
            self.top = self.top.get_ref()
            return self.top.get_item()
        else:
            return "Pile vide !!!!!!!!!!!!"
        
    def etre_vide(self):
        return self.top == None
    
    def get_item(self):
        return self.top.get_item()
    
    def get_ref(self):
        return self.top.get_ref()
    
    def get_sommet(self):
        return self.top.get_item()
    
    def get_taille(self):
        x = True
        taille = 1
        noeud_a_etudier = self.top
        while x:
            if noeud_a_etudier.get_ref() is None:
                x = False
            else:
                noeud_a_etudier = noeud_a_etudier.get_ref()
                taille += 1
        return taille
        
    
    
        
oui = Pile_2_noeud()
oui.empiler("L'Abbé Tonneuse")
oui.empiler("L'Abbé Tonière")
oui.empiler("L'Abbé Nouar")
oui.empiler("L'Abbé Thon")
oui.empiler("Le Père Choir")
oui.empiler("Le Père Soeur")
print(oui.get_ref().get_ref().get_ref().get_item())
print(oui.depiler())
print(oui.get_item())
print(oui.get_taille())

