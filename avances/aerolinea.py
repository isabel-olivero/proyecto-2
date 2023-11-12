import vuelo
import aeronave
import persona


class aerolinea:
    def __init__(self, name):
        self.nombre =name
        self.vuelos = []
        self.aeronaves= []
        self.tripulacion=[]
        self.pasajeros=[]

    def agregarVuelo(vuelo): #agrega un nuevo vuelo a la lista de vuelo de la aerolinea
        self.vuelos.append(vuelo)

    def mostrarVuelos():# muestra los vuelos existententes en la aerolinea
        for t in range(len(self.vuelos)):
            self.vuelos[t].mostrarVuelo()

    def agregarTripulante(tripulante): #agrega un nuevo tripulante a la lista de tripulantes de la aerolinea
        self.tripulacion.append(tripulante)

    def selecVuelo(num,pasajero):#agrega un nuevo pasajero al vuelo seleccionado y al historial de pasajeros en la aerolinea
        self.vuelos[num].reservarCupo(pasajero)
        self.pasajeros.append(pasajero)



    def reservarAeronave(aeronave): #agrega una nueva aeronave a la aerolinea
        self.aeronaves.append(aeronave)

    def asignarTripulacion(vuelo):
        tripu = []
        cap,copi,az,k= 0,0,0,0
        while((k < (len(self.tripulacion))) and ((cap = 0)or (copi= 0) or(az = 0) ):
            if((cap = 0) and (self.tripulacion[j].cargo()== "capitan")):
                cap = 1
                tripu.append(self.tripulacion[j])
            elif((copi = 0) and(self.tripulacion[j].cargo()== "copiloto")):
                copi= 1
                tripu.append( self.tripulacion[j])
            elif((az = 0) and(self.tripulacion[j].cargo()== "azafata")):
                az=1
                tripu.append( self.tripulacion[j])
            k += 1
        
        if((cap = 1)and (copi= 1) and(az = 1)):
            vuelo.tripulacion = tripu
        else:
            print("No es posible asignar una tripulacion")
    
    

