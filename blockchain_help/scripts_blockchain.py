import random

class Chien:

    def __init__(self,race,nom):
        self.race = race
        self.nom = nom

    def same_race(self,otherRace):
        if otherRace.race == self.race:
            print("Yes")
            return True
        else:
            print("No")
            return False

    def balbohazard(self):
        return str([random.random() for _ in range(20)])



class Chat:

    def __init__(self,couleur,nom):
        self.couleur = couleur
        self.nom = nom

    def combat(self,chien):
        print(f"Énorme combat entre {self.nom} et {chien.nom}")




if __name__ == '__main__':
    balbochien = Chien("Balbochacal", "BalboSnoop")

    print(balbochien.same_race(balbochien))

    print(balbochien.balbohazard())
    balbochat = Chat("Vert", "Mamie Zazou")

    balbochat.combat(balbochien)

    print("Hoi")