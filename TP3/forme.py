from abc import ABC , abstractmethod
from math import pi
class forme(ABC):
    @abstractmethod
    def calculer_surface(Self):
        pass
    
class cercle(forme):
    
    def __init__(Self,ray):
        Self.ray=ray
    
    def calculer_surface(Self):
        return pi * Self.ray**2

class rectangle(forme):
     
    def __init__(Self,l,h):
        Self.l=l
        Self.h=h

    def calculer_surface(Self):
        return Self.l * Self.h
    
if __name__ == "__main__":
   C= cercle(2)
   print(f"surface of a cercle is : {C.calculer_surface():.1f}")

   R= rectangle(2,3)
   print(f"surface of a rectangle is : {R.calculer_surface():.1f}")
