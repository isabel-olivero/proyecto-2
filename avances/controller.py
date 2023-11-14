import aeronave
import aeropuerto
import model
import viewGeneral
import streamlit as st

import vuelo


class control:
    def __init__(self):
        self.view = viewGeneral.viewGeneral()
        self.model = model.modelo()
        if 'cnt' not in st.session_state:
            st.session_state['cnt'] = 0
        #self.infoPer = model.infoPasModel()
    def menu(self):
        sel = self.view.menu()
        st.session_state['Seleccion'] = sel
        if sel == 'Reservar':
            self.reservarNave()
        elif sel =='Registro como Pasajero':
            self.crearPasa()
        elif sel == 'Registro como Tripulante':
            self.crearTripu()
        elif sel == 'Ver info pasajeros':
            self.mostrarPas()
        elif sel == 'Ver info tripulación':
            self.mostrarTri()
        elif sel == 'ver info de aeronaves':
            self.mostrarNaves()
        elif sel== 'crear aeronave':
            self.crear()
        elif sel == 'selecciona':
            self.view.fondo()

    def cnt(self):
        st.session_state['cnt'] = st.session_state['cnt'] + 1
        return st.session_state['cnt']
    def cntA(self):
        st.session_state['cntA'] = st.session_state['cntA'] + 1
        return st.session_state['cntA']
    def cntH(self):
        st.session_state['cntH'] = st.session_state['cntH'] + 1
        return st.session_state['cntH']
    def cntJ(self):
        st.session_state['cntJ'] = st.session_state['cntJ'] + 1
        return st.session_state['cntJ']
    def crearPasa(self):
        p = self.view.registrarPasajero()
        if p:
            numero = self.cnt()
            person = model.infoPasModel(p["ID"], p['Nombre'], p['Telefono'], p['Puesto'], p['Maletas'])
            self.model.ingresarPasajero(numero, person)

    def crearTripu(self):
        p = self.view.registrarTripulante()
        if p:
            numero = self.cnt()
            person = model.infoPasModel(p['ID'], p['Nombre'], p['Telefono'], p['Puesto'], p['Maletas'])
            self.model.ingresarTripulante(numero, person)

    def mostrarPas(self):
        liP = self.model.retornarP()
        self.view.verInfoPasajeros(liP)

    def mostrarTri(self):
        liT = self.model.retornarT()
        self.view.verInfoTripulacion(liT)


    def reservarNave(self):
        nave = self.view.cualNave()
        reLi = self.model.retornarP()
        if len(reLi) == 0 :
            self.view.error()
        else:
            iden = self.view.pedirId(len(reLi))
            pas = reLi[iden]
            self.model.reserva(pas, nave)
    def crear(self):
        n = self.view.nave()
        if n == "Avión":
            a = self.model.generarAvion()
            if a:
                numero = self.cnt()
                av = model.infoNaveModel(a["Tipo de nave"],a["Año de viejo"], a["Estado"], a["Marca"], a["Modelo"], a["Destino"], a["Sillas"], a['Categoria'])
                self.model.ingresarNaves(numero, av)
        if n == "Helicóptero":
            h = self.model.generarHelicoptero()
            if h:
                numero = self.cnt()
                he = model.infoNaveModel(h["Tipo de nave"],h["Año de viejo"], h["Estado"], h["Marca"], h["Modelo"], h["Destino"], h["Sillas"], h['Categoria'])
                self.model.ingresarNaves(numero, he)
    def mostrarNaves(self):
        nave = self.model.retornarN()
        self.view.verInfoNaves(nave)


