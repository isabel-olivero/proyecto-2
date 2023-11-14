import random

class Puerta:
    def __init__(self):
        self.numID = random.randint(1, 65)
        al = random.randint(0, 15)
        self.ubi = str(al)  # + "A"
        self.dispo = True
        self.horaE = 24 - random.randint(0, 15)

    def verEstado(self):
        ans = self.dispo
        return ans

    def cambiarEstado(self, n):
        self.dispo = n


    def verEstado(self):
        ans = self.dispo
        return ans
