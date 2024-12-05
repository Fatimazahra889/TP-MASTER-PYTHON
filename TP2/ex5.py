class Animal():
    def faire_du_bruit(self):
        print("Make a sound :")

class Chien(Animal):
    def faire_du_bruit(self):
        print("Woof!")

class Chat(Animal):
    def faire_du_bruit(self):
        print("Meow!")

animal = Animal()
animal.faire_du_bruit()  

chien = Chien()
chien.faire_du_bruit()  

chat = Chat()
chat.faire_du_bruit()  
