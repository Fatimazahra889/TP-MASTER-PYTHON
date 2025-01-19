class Vehicule:
    def __init__(self, marque, modele, annee):
        self.marque = marque
        self.modele = modele
        self.annee = annee
    
    def afficher_info(self):
        print(f"Marque: {self.marque}, Modèle: {self.modele}, Année: {self.annee}")

