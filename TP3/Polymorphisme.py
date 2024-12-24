from forme import *   #import all the functions that exist in the forme class

def afficher_surface(forme):
    for forme in forme:
        print(f"Surface of a {type(forme).__name__} is: {forme.calculer_surface():.1f}")

if __name__ == "__main__":
   forme= [cercle(1),rectangle(2,3),cercle(4),rectangle(5,6)]
   afficher_surface(forme) 