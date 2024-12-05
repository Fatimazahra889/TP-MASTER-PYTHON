class Rectangle():
    def __init__(Self,largeur,hauteur):
        Self.largeur=largeur
        Self.hauteur=hauteur

    def calculer_surface(Self):
        Self.surface =Self.largeur *Self.hauteur
        print(str(Self.surface)) 
    
    def calculer_perimetre(Self):
        Self.perimetre= (Self.largeur +Self.hauteur)*2
        print(str(Self.perimetre)) 
    
    

rec=Rectangle(5,3)
rec.calculer_surface()
rec.calculer_perimetre()
            
