class Personne:
    def __init__(self, nom, prenom, age):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.amis = [] 

    def se_presenter(self):
        print(f"The next one that will present is {self.nom} {self.prenom}, age: {self.age}")

    def ajouter_ami(self, ami):
        if ami not in self.amis:
            self.amis.append(ami)
            print(f"{ami.nom} {ami.prenom} added to a friend.")
        else:
            print(f"{ami.nom} {ami.prenom} already a friend.")

    def afficher_amis(self):
        print(f"liste of friends are {self.nom} {self.prenom} :")
        for ami in self.amis:
                print(f"{ami.nom} {ami.prenom}, {ami.age} year")


class Etudiant(Personne):
    def __init__(self, nom, prenom, age, matricule):
        super().__init__(nom, prenom, age)
        self.matricule = matricule

    def etudier(self):
        print(f"{self.nom} {self.prenom} étudie matricule : {self.matricule}")



pers1 = Etudiant("Ema", "Sarma", 20, "SE")
pers2 = Etudiant("Walid", "Ogri", 21, "IL")
pers3 = Personne("Sofia", "Ali", 22)


pers1.se_presenter()
pers1.etudier()


pers1.ajouter_ami(pers2)
pers1.ajouter_ami(pers3)
pers1.ajouter_ami(pers2)  

pers1.afficher_amis()
