class Motor:
    def __init__(self, puissance, type_moteur):
        self.puissance = puissance
        self.type_moteur = type_moteur
    
    def afficher_motor(self):
        print(f"Puissance: {self.puissance} chevaux, Type de moteur: {self.type_moteur}")