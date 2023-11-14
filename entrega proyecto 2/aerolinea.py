import viewGeneral
import model


class aerolinea:
    def __init__(self, name):
        self.nombre = name
        self.view = viewGeneral.viewGeneral()
        self.model = model.modelo()
        self.vuelos = []
        self.aeronaves = []
        self.tripulacion = []
        self.pasajeros = []

    def agregarVuelo(self, vuelo):  # agrega un nuevo vuelo a la lista de vuelo de la aerolinea
        self.vuelos.append(vuelo)

    def mostrarVuelos():# muestra los vuelos existententes disponibles en la aerolinea
        for t in range(len(self.vuelos)):
            if(self.vuelos[t].sillasV > 0):
                self.vuelos[t].mostrarVuelo()

    def agregarTripulante(self, tripulante):  # agrega un nuevo tripulante a la lista de tripulantes de la aerolinea
        self.tripulacion.append(tripulante)

    def selecVuelo(self, num,
                   pasajero):  # agrega un nuevo pasajero al vuelo seleccionado y al historial de pasajeros en la aerolinea
        self.vuelos[num].reservarCupo(pasajero)
        self.pasajeros.append(pasajero)

    def reservarAeronave(self, aeronave):  # agrega una nueva aeronave a la aerolinea
        self.aeronaves.append(aeronave)

    def asignarTripulacion(self, vuelo):
        reLi = self.model.retornarT()
        iden = self.view.pedirId(len(reLi))
        p = reLi[iden]
        puesto = p.puesto
        cap = vuelo.cap
        copi = vuelo.copi
        az = vuelo.az
        pol = vuelo.pol

        if ((cap == 0) and (puesto == 'Piloto')):
            vuelo.cap = 1
            vuelo.tripulacion.append(p)
        elif ((copi == 0) and (puesto == 'Copiloto')):
            vuelo.copi = 1
            vuelo.tripulacion.append(p)
        elif ((az == 0) and (puesto == 'Tripulante de cabina')):
            vuelo.az = 1
            vuelo.tripulacion.append(p)
        elif ((pol == 0) and (puesto == 'Policia aereo')):
            vuelo.pol = 1
            vuelo.tripulacion.append(p)

        if ((cap == 1) and (copi == 1) and (az == 1) and (pol == 1)):
            print("Tripulacion completada")

