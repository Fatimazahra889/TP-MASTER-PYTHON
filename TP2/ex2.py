class voiture ():
    def __init__(Self,marque,modele,annee):
        Self.marque=marque
        Self.modele=modele
        Self.annee=annee

    def afficher_info(Self):
        print("marque:"+ str(Self.marque) +"\nmodele:"+str(Self.modele)+"\nannee:"+str(Self.annee))
   

voi1=voiture("tesla","model X",2019)
voi2=voiture("renault","arkana",2021)
voi3=voiture("mercedece","SL Roadster",2002)
voi1.afficher_info()
voi2.afficher_info()
voi3.afficher_info()
