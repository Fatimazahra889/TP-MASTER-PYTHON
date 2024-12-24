class personne():

    def __init__(Self,nom,prenom,age):
        Self.__nom=nom
        Self.__prenom=prenom
        Self.__age=age
    
    @property
    def nom(Self):
        return Self.__nom
    @nom.setter
    def nom(Self,nom):
        Self.__nom= nom
    #def get_nom(Self):
        return Self.__nom
    #def set_nom(Self,nom):
        Self.__nom=nom
    
    @property
    def prenom(Self):
        return Self.__prenom
    @prenom.setter
    def prenom(Self,prenom):
        Self.__prenom=prenom
    #def get_prenom(Self):
        return Self.__prenom
    #def set_prenom(Self,prenom):
        Self.__prenom=prenom
    
    @property
    def age(Self):
        return Self.__age
    @age.setter
    def age(Self,age):
        Self.__age=age
    #def get_age(Self):
        return Self.__age
    #def set_age(Self,age):
        Self.__age=age
    

per1=personne("ema","sarma",21)
#print(per1.get_nom())
print(per1.nom)
#print(per1.set_nom("salwa"))
per1.nom="salwa"
#print(per1.get_nom())
print(per1.nom)
#print(per1.get_prenom())
print(per1.prenom) 
#print(per1.set_prenom("jamil")) 
per1.prenom="jamil"
#print(per1.get_prenom())
print(per1.prenom)
#print(per1.get_age())
print(per1.age)
#print(per1.set_age(26))
per1.age=26
#print(per1.get_age())
print(per1.age)