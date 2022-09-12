class CompteBancaire:
    def __init__(self, numero_compte:str, pre_nom:str, argent:float):
        self.num_compte = numero_compte
        self.nom = pre_nom
        self.solde = argent
        
    def get_num_compte(self):
        return self.num_compte
    
    def get_nom(self):
        return self.nom
    
    def get_solde(self):
        return self.solde
    
    def tout(self):
        return self.num_compte, self.nom, self.solde
    
    def versement(self, argent_a_ajouter):
        if argent_a_ajouter > 0:
            self.solde += argent_a_ajouter
            return argent_a_ajouter
        else:
            return "Le montant à ajouter est inférieur à 0€"
    
    def retrait(self, argent_a_retirer):
        if argent_a_retirer > self.solde:
            return "Il est impossible de retirer plus que ce vous avez"
        self.solde -= argent_a_retirer
        return argent_a_retirer
    
    def agios(self):
        if self.solde < 0:
            agios_prev = abs(self.solde)*0.05
            self.solde -= agios_prev
            return f"{agios_prev}€ ont été prélevé"
        else:
            return "Vous solde est positif"
        
    def virement(self, argent, compte_receveur):
        if self.solde > argent: 
            argent_a_virer = self.retrait(argent)
            compte_receveur.versement(argent_a_virer)
        else:
            return "Vous êtes pauvre"

        
compte_1 = CompteBancaire("FR2145", "L'abbé Tonière", 30.25)
compte_2 = CompteBancaire("FR2398", "L'abbé Nouar", -5.65)

print(compte_1.tout())
print(compte_2.tout())

print(compte_2.virement(1, compte_1))

print(compte_1.tout())
print(compte_2.tout())