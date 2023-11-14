import streamlit as st
import vuelo
import aeropuerto
import viewGeneral
import torre
class infoNaveModel:
    def __init__(self,id,tipo,yearFab,estado,marca,modelo,destino,per,cate,propietario):
        self.tipo = tipo
        self.yearFab = yearFab
        self.estado = estado
        self.id = id
        self.marca = marca
        self.modelo = modelo
        self.destino = destino
        self.per = per
        self.categoria = cate
        self.propietario = propietario
    def setId(self,id):
        self.id = id
    def setTipo(self,tipo):
        self.tipo = tipo
    def setYear(self,yearFab):
        self.yearFab = yearFab
    def setEstado(self,estado):
        self.estado = estado
    def setMarca(self,marca):
        self.marca = marca
    def setModelo(self,modelo):
        self.modelo = modelo
    def setDestino(self,destino):
        self.destino = destino
    def setPer(self,per):
        self.per = per
    def setCate(self,categoria):
        self.categoria = categoria
    def setPro(self,propietario):
        self.propietario = propietario


class infoPasModel:
    def __init__(self, id, name,telefono,puesto,maleta):
        self.id = id
        self.telefono = telefono
        self.name = name
        self.maleta = maleta
        self.puesto = puesto
        self.state = "Sin asignar"

    def setId(self,id):
        self.id=id
    def setName(self, name):
        self.name = name

    def setDescription(self, fecha):
        self.fecha = fecha

    def setState(self, state):
        self.state = state

class modelo:
    def __init__(self):
        self.view = viewGeneral.viewGeneral()
        if 'Pasajeros' not in st.session_state:
            st.session_state['Pasajeros'] = {}
            self.liPa = {}
        else:
            self.liPa = st.session_state['Pasajeros']
        if 'Tripulantes' not in st.session_state:
            st.session_state['Tripulantes'] = {}
            self.liTri = {}
        else:
            self.liTri = st.session_state['Tripulantes']
        if 'Naves' not in st.session_state:
            st.session_state['Naves'] = {}
            self.naves = {}
        else:
            self.naves = st.session_state['Naves']

        if 'vuelo' not in st.session_state:
            st.session_state['vuelo'] = {}
            self.vu = {}

    def ingresarPasajero(self,id,liPa):   # las funciones de ingresar son las encargadas de guardar los datos con la ayuda del session_state
        self.liPa[id] = liPa
        st.session_state['Pasajeros'] = self.liPa

    def ingresarTripulante(self,id,liTri):
        self.liTri[id] = liTri
        st.session_state['Tripulantes'] = self.liTri

    def ingresarNaves(self,id,naves):
        self.naves[id] = naves
        st.session_state['Naves'] = self.naves


    def ingresarVuelo(self,vuelo):
        self.vu[0] = vuelo
        st.session_state['vuelo'] = self.vu

    def retornarN(self):   # las funciones de retornar estan encargadas de devolver las listas creadas, las de Nave,pasajeros y tripulacion
        return self.naves

    def retornarP(self):
        return self.liPa

    def retornarT(self):
        return self.liTri



    def dame_sillas(self):   #esta funcion retorna el numero de sillas que se encuentra en una de las posiciones de la lista de naves

        reLi = self.retornarN()
        iden = self.view.pedirId()
        if iden > len(reLi):
            st.error("Por ahora ese número no es valido")
        else:
            a = list(reLi)
            if((iden + 1) in a):
                p = reLi[iden + 1]
                puesto = p.per
                return puesto
        # st.subheader(puesto)

    def dame_nombre(self):  # esta funcion retorna el nombre de la persona, que se encuentra en una de las posiciones de la lista de pasajeros
        rePa = self.retornarP()
        tefi = self.view.pedirId2()
        if tefi > len(rePa):
            st.error("Por ahora ese número no es valido")
        else:
            a = list(rePa)
            if(tefi in rePa):
                n = rePa[tefi]
                nom = n.name
                return nom

    def reserva(self): #como dice su nombre, es la que permite realizar una reserva
        sillas = self.dame_sillas()
        st.title('sillas disponibles:')
        st.header(sillas)

        if( sillas == None):
            st.error("Valor no disponible")
            #st.error("Lo sentimos ha ocurrido un error, trataremos de solucionarlo lo antes posible")
        else:
            name = self.dame_nombre()
            if name== None:
                st.error("Lo sentimos ha ocurrido un error, trataremos de solucionarlo lo antes posible")
            else:
                cual = viewGeneral.viewGeneral().cualNave()
                no = vuelo.vuelo().reservar(cual,sillas,name)
                if no == 1:
                    st.info("No se pudo completar la reserva,aeronave llena")
                else:
                    st.success("Reserva exitosa")

    def generarAvion(self):    #y estas 3 funciones de generar son las encargadas de poder crear y retornar las naves que se pidan generar
        avion = aeropuerto.aeropuesto().generarAvion()
        vuelo.vuelo().naves.append(avion)
        return avion

    def generarHelicoptero(self):
        heli = aeropuerto.aeropuesto().generarHelicoptero()
        vuelo.vuelo().naves.append(heli)
        return heli
    def generarJet(self):
        jet = aeropuerto.aeropuesto().generarJet()
        vuelo.vuelo().naves.append(jet)
        return jet
    def generarPuerta(self):
        torre.Torre(name="",loc="").generarPuertas()
        self.view.im()
