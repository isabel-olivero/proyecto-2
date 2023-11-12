class vuelo:
    def __init__(self,des,date,s,n):
        self.sillasV= s
        self.idVuelo = n
        self.pasajeros =[]
        self.des= des
        self.fecha = date
        self.origen = "Cali"


    def reservar(pasajero):
        if (self.sillasV > 0):
            sillas -= 1
            self.pasajeros.append(pasajero)

        else:
            print("No es posible reservar")
            