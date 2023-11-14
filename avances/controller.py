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
        if 'cntA' not in st.session_state:
            st.session_state['cntA'] = 0
        if 'cntH' not in st.session_state:
            st.session_state['cntH'] = 0
        if 'cntJ' not in st.session_state:
            st.session_state['cntJ'] = 0
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
        elif sel == 'Asignar tripulacion':
            self.cambioDeEstado()
        elif sel =='Entrar a Torre':
            pass


    def torre(self):
        sel= self.view.elemTorre()
        if sel =='generarPuertas':
            self.model.generarPuerta()
        elif sel=='ubicarPuerta':
            ubi = self.model.ubicarPuerta()
        elif sel=='despegarAeronave':
            pass
        elif sel =='borrarAeronave':
            pass
        elif sel=='agregarHist':
            pass
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
        self.view.verInfoTripulacion(liT,"No asignado")




        #st.subheader(nom)
    def reservarNave(self):
        uno =self.model.retornarP()
        dos = self.model.retornarN()
        if ((len(uno)==0)or(len(dos)==0)):
            st.error("Debes registrar o falta crear nave")
        else:
            self.model.reserva()



        '''pas = self.model.retornarP()
        num = self.view.pedirId()
        nave = self.model.retornarN()
        na = self.view.pedirId2(len(nave))
        if (len(pas) == 0) or (len(nave) == 0):
            self.view.error()
        else:
            self.model.reserva(num,na)
            '''



    def crear(self):
        n = self.view.nave()
        if n == "Avión":
            a = self.model.generarAvion()
            if a:
                nA = self.cntA()
                if nA <= 3:
                    numero = self.cnt()
                    av = model.infoNaveModel(a["ID"], a["Tipo de nave"],a["Año de viejo"], a["Estado"], a["Marca"], a["Modelo"], a["Destino"], a["Sillas"], a['Categoria'],a["Propietario"])
                    self.model.ingresarNaves(numero, av)
                else:
                    st.error("No se pueden crear más aviones")
        elif n == "Helicóptero":
            h = self.model.generarHelicoptero()
            if h:
                nh = self.cntH()
                if nh <= 3:
                    numero = self.cnt()
                    he = model.infoNaveModel(h["ID"],h["Tipo de nave"],h["Año de viejo"], h["Estado"], h["Marca"], h["Modelo"], h["Destino"], h["Sillas"], h['Categoria'],h["Propietario"])
                    self.model.ingresarNaves(numero, he)
                else:
                    st.error("No se pueden crear más Helicopteros")
        else:
            j = self.model.generarJet()
            if j:
                nj = self.cntJ()
                if nj <= 3:
                    numero = self.cnt()
                    je = model.infoNaveModel(j["ID"],j["Tipo de nave"],j["Año de viejo"], j["Estado"], j["Marca"], j["Modelo"], j["Destino"], j["Sillas"], j['Categoria'],j["Propietario"])
                    self.model.ingresarNaves(numero,je)
                else:
                    st.error("No se pueden crear más jets")
    def mostrarNaves(self):
        nave = self.model.retornarN()
        self.view.verInfoNaves(nave)


    def asignarTripu(self):
        lt = self.model.retornarT()
        cnt = self.view.pedirId()
        self.view.verInfoTripulacion(lt,"Asignado",cnt)



