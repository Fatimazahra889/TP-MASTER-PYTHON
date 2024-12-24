class Produit:
    def __init__(self, nom, prix):
        self.__nom = nom
        self.__prix = prix

    def get_nom(self):
        return self.__nom

    def set_nom(self, nom):
        self.__nom = nom

    def get_prix(self):
        return self.__prix

    def set_prix(self, prix):
        self.__prix = prix

    def calculer_prix(self, remise, montant):
        if self.__prix > montant and montant > 0:
            return self.__prix - (self.__prix * (remise / 100))
        else:
            return self.__prix


if __name__ == "__main__":
    p1 = Produit("cleanser", 160)
    p2 = Produit("Shampoo", 90)
    p3 = Produit("Lotion", 200)

    print(f"Prix final de {p1.get_nom()}: {p1.calculer_prix(15, 100)} dh")
    print(f"Prix final de {p2.get_nom()}: {p2.calculer_prix(0, 100)} dh")
    print(f"Prix final de {p3.get_nom()}: {p3.calculer_prix(0, 0)} dh")
