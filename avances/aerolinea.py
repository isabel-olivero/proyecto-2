import vuelo
import aeronave
import persona
import view
import model


class aerolinea:
    def __init__(self, name):
        self.nombre =name
        self.view = viewGeneral.viewGeneral()
        self.model = model.modelo()
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
        reLi = self.model.retornarT()
        iden = self.view.pedirId(len(reLi))
        p = reLi[iden]
        puesto = p.puesto
        tripu = []
        cap,copi,az,k= 0,0,0,0
        cap = vuelo.cap
        copi = vuelo.copi
        az = vuelo.az 
        pol = vuelo.pol
     
        if((cap = 0) and (puesto == 'Piloto')):
            cap = 1
            vuelo.tripulacion.append(p)
        elif((copi = 0) and(puesto == 'Copiloto')):
            copi= 1
            vuelo.tripulacion.append(p)
        elif((az = 0) and(puesto == 'Tripulante de cabina')):
            az=1
            vuelo.tripulacion.append(p)
        elif((pol=0) and (puesto == 'Policia aereo')):
            pol=1
            vuelo.tripulacion.append(p)
            
        if((cap = 1)and (copi= 1) and(az = 1)):
            print("Tripulacion completada")





    # def asignarTripulacion(vuelo):
    #     reLi = self.model.retornarT()
    #     iden = self.view.pedirId(len(reLi))
    #     p = reLi[iden]
    #     puesto = p.puesto

    #     tripu = []
    #     cap,copi,az,k= 0,0,0,0
    #     while((k < (len(self.tripulacion))) and ((cap = 0)or (copi= 0) or(az = 0) ):
    #         if((cap = 0) and (self.tripulacion[j].cargo()== "capitan")):
    #             cap = 1
    #             tripu.append(self.tripulacion[j])
    #         elif((copi = 0) and(self.tripulacion[j].cargo()== "copiloto")):
    #             copi= 1
    #             tripu.append( self.tripulacion[j])
    #         elif((az = 0) and(self.tripulacion[j].cargo()== "azafata")):
    #             az=1
    #             tripu.append( self.tripulacion[j])
    #         k += 1
        
    #     if((cap = 1)and (copi= 1) and(az = 1)):
    #         vuelo.tripulacion = tripu
    #     else:
    #         print("No es posible asignar una tripulacion")
    
    

