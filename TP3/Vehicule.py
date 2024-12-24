from abc import ABC ,abstractmethod
class Vehicule():
    @abstractmethod
    def deplacer(Self):
        pass

class Voiture(Vehicule):
    def deplacer(Self):
        print("your car is moving faster")

class Bicyclette(Vehicule):
    def deplacer(Self):
        print("your bicycle has passed the speed limit")

v1=Voiture()
b1=Bicyclette()
print(v1.deplacer())
print(b1.deplacer())


