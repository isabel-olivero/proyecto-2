class vuelo:
    def __init__(self,des,date,s,n,a,j,h):
        self.sillasV= s
        self.idVuelo = n
        #self.pasajeros =[]
        self.des= des
        self.fecha = date
        self.origen = "Cali"
        self.sillasA = a
        self.sillasJ = j
        self.sillasH =h
        self.pasajerosA = []
        self.pasajerosH = []
        self.pasajerosJ = []

    def reservar(self,pasajero,selec):
        if(selec=="Avion"):
            if(self.sillasA>0):
                self.sillasA -= 1
                self.pasajerosA.append(pasajero)
            else:
                print("No es posible reservar")
        elif(selec=="Helicoptero"):
            if(self.sillasH>0):
                self.sillasH -= 1
                self.pasajerosH.append(pasajero)
            else:
                print("No es posible reservar")
        elif(selec=="Jet"):
            if(self.sillasJ>0):
                self.sillasJ -= 1
                self.pasajerosJ.append(pasajero)
            else:
                print("No es posible reservar")
            
