from assignement_2 import Chien


balbochien = Chien("Balbochacal","BalboSnoop")


class Chat:

    def __init__(self,couleur,nom):
        self.couleur = couleur
        self.nom = nom

    def combat(self,chien):
        print(f"Énorme combat entre {self.nom} et {chien.nom}")
        print()


balbochat = Chat("Vert", "Mamie Zazou")

balbochat.combat(balbochien)
print(balbochien.balbohazard())