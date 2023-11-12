import viewPer
#import model
#import view_aeronave
#import viewTorre
import streamlit as st
import time

class viewGeneral:
    def __init__(self):
        self.persona = viewPer.viewPer()
        #self.nave = view_aeronave
        #self.torre = viewTorre



    def menu(self):
        option= st.sidebar.radio("Selecciona una opcion",["Reservar","Registro como Pasajero","Registro como Tripulante","Ver info pasajeros","Ver info tripulación","iniciar sesion","crear aeronave","ver info de aeronaves"])
        return option

    def registrarPasajero(self):
        p = self.persona.datosPasajeros()
        return p


    def registrarTripulante(self):
        t = self.persona.datosTripulacion()
        return t


    def iniciar_sesion(self,liPas,liTri):
        sel = st.selectbox("Selecciona uno: ",['Pasajero','Tripulación'])
        if(sel == 'Pasajero'):
            ingresa = st.number_input("Ingresa el ID usado: ")
            with st.spinner("Comprobando..."):
                if liPas[ingresa]:
                    time.sleep(3)
                    st.success('Entraste!')
                else:
                    st.error("No se encontro en la base, debe registrarse ")
        else:
            ingresa = st.number_input("Ingresa el ID usado: ")
            with st.spinner("Comprobando..."):
                if liTri[ingresa]:
                    time.sleep(3)
                    st.success('Entraste!')
                else:
                    st.error("No se encontro en la base, debe registrarse ")



    def verInfoPasajeros(self, lp):
            st.header("Ver info pasajeros")
            st.write("Informacion primordial del pasajero")
            informacion = []
            for info in lp:
                pasa = lp[info]
                informacion.append(
                    {"ID": pasa.id,"Nombre ": pasa.name,"Telefono ": pasa.telefono, "Estado": pasa.state})
            if informacion:
                st.table(informacion)
            else:
                st.write("NO HAY NADA")
    def verInfoTripulacion(self, lt):
        st.header("Ver info tripulantes")
        st.write("Información primordial del tripulante")
        informacion = []
        for info in lt:
            tripu = lt[info]
            informacion.append({"ID": tripu.id,"Nombre ": tripu.name,"Telefono ": tripu.telefono,"Estado": tripu.state})
        if informacion:
            st.table(informacion)
