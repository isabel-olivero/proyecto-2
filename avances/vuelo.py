
class vuelo:
    def __init__(self,s,a,j,h):
        self.sillasV= s
        self.naves =[]
        self.origen = "Cali"
        self.sillasA = a
        self.sillasJ = j
        self.sillasH =h
        self.pasajerosA = []
        self.pasajerosH = []
        self.pasajerosJ = []

        def setId(self, sillasV):
            self.sillasV = sillasV

        def setName(self, sillasA):
            self.sillasA = sillasA

        def setDescription(self, sillasJ):
            self.sillasJ = sillasJ

        def setState(self, sillasH):
            self.sillasH = sillasH



    def reservar(self,pasajero,nave):
        no=0
        selec = nave["Tipo de nave"]
        silla = nave["Sillas"]
        if(selec=="Avión"):
            if(self.sillasA>0 and silla>0):
                nave["Sillas"] -= 1
                self.sillasA -= 1
                self.pasajerosA.append(pasajero)
            else:
                no=1
        elif(selec=="Helicóptero"):
            if(self.sillasH>0 and silla>0):
                nave["Sillas"] -= 1
                self.sillasH -= 1
                self.pasajerosH.append(pasajero)
            else:
                no=1
        elif(selec=="Jet"):
            if(self.sillasJ>0 and silla>0 ):
                nave["Sillas"] -= 1
                self.sillasJ -= 1
                self.pasajerosJ.append(pasajero)
            else:
                no=1
        return no
            
