class Employe():
    def __init__(Self,nom,prenom,salaire):
        Self.nom=nom
        Self.prenom=prenom
        Self.salaire=salaire

class Manager(Employe):
    def __init__(Self,nom,prenom,salaire):
        Employe.__init__(Self,nom,prenom,salaire)
        Self.liste=[]

    def ajouter_employe(Self,new_employe):
        Self.liste.append(new_employe)
    
    def afficher_manager(Self):
        print(f"{Self.nom} {Self.prenom} supervized :")
        for employe in Self.liste:
            print(f"{employe.nom} {employe.prenom} with a salary of :{employe.salaire}")


e1=Employe("ema","sarma",15000)
e2=Employe("amine","nab",14000)
e3=Employe("zahra","jamil",16000)


m1=Manager("fati","azis",40000)
m1.ajouter_employe(e1)
m1.afficher_manager()

m2=Manager("lina","maha",41000)
m1.ajouter_employe(e2)
m1.ajouter_employe(e3)
m1.afficher_manager()
