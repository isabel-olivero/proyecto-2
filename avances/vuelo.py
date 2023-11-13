class vuelo:
    def __init__(self,des,date,s,n,a,j,h,cap,copi,az,pol):
        self.sillasV= s
        self.idVuelo = n
        self.cap = cap
        self.copi = copi
        self.az = az
        self.pol = pol
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
        no=0
        if(selec=="Avión"):
            if(self.sillasA>0):
                self.sillasA -= 1
                self.pasajerosA.append(pasajero)
            else:
                no=1
        elif(selec=="Helicóptero"):
            if(self.sillasH>0):
                self.sillasH -= 1
                self.pasajerosH.append(pasajero)
            else:
                no=1
        elif(selec=="Jet"):
            if(self.sillasJ>0):
                self.sillasJ -= 1
                self.pasajerosJ.append(pasajero)
            else:
                no=1
        return no
            
