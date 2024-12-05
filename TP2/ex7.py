class livre():
    def __init__(Self,titre,auteur,an_pub):
        Self.titre=titre
        Self.auteur=auteur
        Self.an_pub=an_pub
    def __str__(self):
        return f"'{self.titre}' par {self.auteur} ({self.an_pub})"

class Biblio():
    def __init__(Self):
        Self.Livre=[]

    def ajouter_livre(Self,livre):
        Self.Livre.append(livre)
        print("Il est ajouter ")

    def afficher_livres(Self):
        for livre in Self.Livre:
                print(f"{livre}")


ma_biblio = Biblio()                

livre1 = livre("Les Misérables", "Victor Hugo", 1862)
livre2 = livre("1984", "George Orwell", 1949)
livre3 = livre("Le Petit Prince", "Antoine de Saint-Exupéry", 1943)

ma_biblio.ajouter_livre(livre1)
ma_biblio.ajouter_livre(livre2)
ma_biblio.ajouter_livre(livre3)

ma_biblio.afficher_livres()

    