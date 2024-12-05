class CompteBancaire():
    def __init__(Self,tituliaire,solde):
        Self.tituliaire=tituliaire
        Self.solde=solde
    
    def deposer(Self,montant):
        Self.montant=montant
        Self.solde+=montant
        
    def retirer(Self,montant):
        Self.montant=montant
        if Self.solde> 0:
            Self.solde-=montant
        else :
            print("you reached your limit : 0dh")
            

    def afficher_solde(Self):
        print("solde actuel:"+str(Self.solde))

CIH=CompteBancaire("ema",0)
CIH.retirer(10)
CIH.afficher_solde()
CIH.deposer(100)
CIH.afficher_solde()
CIH.retirer(20)
CIH.afficher_solde()