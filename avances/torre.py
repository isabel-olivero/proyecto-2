import puerta

class Torre:
    def __init__(self, name, loc):
        self.nombre = name
        self.localizacion = loc
        self.aeronaves = []
        self.embarques = []
        self.hist = []

    def generarPuertas(self):
        for i in range(11):
            p = puerta()
            self.embarques.append(p)

    def agregarHist(self, p):
        self.hist.append(p)


    def ubicarPuerta(self, aero):
        dispo = puerta()
        nave = aero
        flag = 0
        i = 0

        while((i < len(self.embarques)) and (flag == 0)):
            if(self.embarques[i].verEstado() == True):
                embarques[i].cambiarEstado(False)
                dispo = embarques[i]
                flag = 1
                aero.ubi= dispo
            else:
                i+= 1
        return(aero,dispo)



#la aeronave puede tener una puerta fija?         

    
	