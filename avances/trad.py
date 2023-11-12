class Torre:
    def __init__(self, name, loc):
        self.nombre = name
        self.localizacion = loc
        self.aeronaves = [Aeronave() for _ in range(10)]
        self.embarques = []
        self.hist = []

    def generarPuertas(self):
        for _ in range(10):
            p = Puerta()
            self.embarques.append(p)

    def agregarHist(self, p):
        self.hist.append(p)

    def ubicarPuerta(self):
        asig = ()
        flag = 0

        for i in range(len(self.aeronaves)):
            act = Aeronave()
            dispo = Puerta()

            if self.aeronaves[i].reportarUbi() == 1:
                act = self.aeronaves[i]
                while flag == 0:
                    for j in range(len(self.embarques)):
                        if self.embarques[j].verEstado():
                            self.embarques[j].cambiarEstado(False)
                            dispo = self.embarques[j]
                            flag = 1
                asig = (act, dispo)
                self.hist.append(asig)
            elif self.aeronaves[i].reportarUbi() == 2:
                for j in range(len(self.hist)):
                    if self.hist[j][0] == self.aeronaves[i]:
                        self.hist[j][1].cambiarEstado(True)

    def cNombre(self, n):
        self.nombre = n

    def cUbi(self, n):
        self.localizacion = n

    def buscarPuerta(self, p):
        ans = Puerta()
        for i in range(len(self.embarques)):
            if self.embarques[i] == p:
                ans = self.embarques[i]
        return ans

class Aeronave:
    def __init__(self):
        pass

    def reportarUbi(self):
        pass

class Puerta:
    def __init__(self):
        pass
    
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
        pass

    def cambiarEstado(self, estado):
        pass
