from Vehicule import *
from Motor import *

class Moto(Vehicule, Motor):
    def __init__(self, marque, modele, annee, puissance, type_moteur, type_moto):
        super().__init__(self, marque, modele, annee)
        super().__init__(self, puissance, type_moteur)
        self.type_moto = type_moto
    
    def afficher_info(self):
        Vehicule.afficher_info(self)
        Motor.afficher_motor(self)
        print(f"Type de moto: {self.type_moto}")



# Création d'une instance de Moto
moto = Moto("Yamaha", "MT-07", 2020, 75, "Essence", "Sport")
print("Informations de la Moto:")
moto.afficher_info()