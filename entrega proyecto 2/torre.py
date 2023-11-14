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
        print("la nave" aero "ha sido a signada a la puerta" dispo)
        return(aero,dispo)

    def despegarAeronave(self, aeronave):
        flag,i=0,0
        while((i<(len(self.aeronaves)))and flag = 0):
            if(self.aeronaves[i].verEstado()== 2):#verifica que no hayan naves en la pista
                flag = 1
        if (flag==0):
            print("La aeronave puede despegar")
            aeronave.estado= 2
        else:
            print("La pista esta ocupada, la aeronave no puede despegar")

    def borrarAeronave(self, aero):
        if(aero.verEstado==2):
            aero.estado==3
            self.aeronaves.remove(aero)




       

    
	