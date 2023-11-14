import streamlit as st
import vuelo
import aeropuerto
import viewGeneral
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

    def ingresarPasajero(self,id,liPa):
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

    def retornarN(self):
        return self.naves

    def retornarP(self):
        return self.liPa

    def retornarT(self):
        return self.liTri

    def posNav(self,nav):
        cnt=0
        for posi in self.naves:
            cnt += 1
            if (cnt == nav):
                nave = self.naves[posi]
                return nave
    def posPas(self,num):
        cnt=0
        for i in self.liPa:
            cnt += 1
            if (cnt == num):
                pas = self.liPa[i]
                return pas

    def dame_sillas_tipo(self,cual):
        reLi = self.retornarN()
        iden = self.view.pedirId()
        p = reLi[iden + 1]
        if cual == "Sillas":
            puesto = p.per
            return puesto
        else:
            puesto = p.tipo
            return puesto
        # st.subheader(puesto)

    def dame_nombre(self):
        rePa = self.retornarP()
        tefi = self.view.pedirId2()
        n = rePa[tefi]
        nom = n.name
        return nom

    def reserva(self):

        sillas = self.dame_sillas_tipo("Sillas")
        name = self.dame_nombre()
        cual = self.dame_sillas_tipo("Tipo")
        st.header(sillas)
        st.header(name)
        st.header(cual)
        #no = vuelo.vuelo(s=0, a=0, j=0, h=0).reservar(cual,sillas,name)
        #if no == 1:
         #   st.info("No se pudo completar la reserva,aeronave llena")
        #else:
#            st.success("Reserva exitosa")

    def generarAvion(self):
        avion = aeropuerto.aeropuesto().generarAvion()
        return avion

    def generarHelicoptero(self):
        heli = aeropuerto.aeropuesto().generarHelicoptero()
        return heli
    def generarJet(self):
        jet = aeropuerto.aeropuesto().generarJet()
        return jet
