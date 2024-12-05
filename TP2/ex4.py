class Personne():
    def __init__(Self,nom,prenom,age):
        Self.nom=nom
        Self.prenom=prenom
        Self.age=age
    
    def se_presenter(Self):
        print("the Next one that will present is"+" "+str(Self.nom)+" "+str(Self.prenom)+", "+"age of :"+" "+str(Self.age))

class Etudiant(Personne):
    def __init__(Self,nom,prenom,age,matricule):
        Personne.__init__(Self,nom,prenom,age)
        Self.matricule=matricule

    def etudier(Self):
        print("studies :",str(Self.matricule))


pers1=Etudiant("ema","Sarma",20,"SE")
pers1.se_presenter()
pers1.etudier()