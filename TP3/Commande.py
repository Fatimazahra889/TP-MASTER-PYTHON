from Produits import Produit
class Commande(Produit):
    def __init__(Self,produit,quantite):
        super().__init__(produit.get_nom(),produit.get_prix())
        Self.produit=produit
        Self.quantite=quantite
    def total_commande(Self):
        return Self.get_prix()*Self.quantite

class Panier():
    def __init__(Self):
        Self.liste=[]

    def ajouter(Self,new_commande):
        Self.liste.append(new_commande)

    def total_panier(Self):
        return sum(commande.total_commande() for commande in Self.liste)
    
    def afficher_panier(Self):
        for commande in Self.liste:
            produit = commande.produit
            print(f"{commande.quantite} x {produit.get_nom()} ({produit.get_prix()} dh each): {commande.total_commande():.2f} dh")
            print(f"Panier total: {Self.total_panier():.2f} dh")
    
p1=Produit("cleanser",160)
p2 = Produit("Shampoo", 90)
p3 = Produit("Lotion", 200)

p1.set_prix(p1.calculer_prix(15, 100))
p2.set_prix(p2.calculer_prix(0, 100))
p3.set_prix(p3.calculer_prix(0, 0))

c1 = Commande(p1, 2) 
c2 = Commande(p2, 3)  
c3 = Commande(p3, 1)  

panier = Panier()
panier.ajouter(c1)
panier.ajouter(c2)
panier.ajouter(c3)

panier.afficher_panier()

     
