import Vehicule
import Motor

class Voiture(Vehicule, Motor):
    def __init__(self, marque, modele, annee, puissance, type_moteur, nombre_de_places):
        super().__init__(self, marque, modele, annee)
        super().__init__(self, puissance, type_moteur)
        self.nombre_de_places = nombre_de_places
    
    def afficher_info(self):
        Vehicule.afficher_info(self)
        Motor.afficher_motor(self)
        print(f"Nombre de places: {self.nombre_de_places}")



# Création d'une instance de Voiture
voiture = Voiture("Skoda","Octavia",2019, 132, "Diesel", 5)
print("Informations de la Voiture:")
voiture.afficher_info()
print()