import viewPer
import model
#import view_aeronave
#import viewTorre
from PIL import Image
import streamlit as st
import time

class viewGeneral:
    def __init__(self):
        self.persona = viewPer.viewPer()
        #self.nave = view_aeronave
        #self.torre = viewTorre



    def menu(self):
        option= st.sidebar.selectbox("Selecciona una opcion",["selecciona","Reservar","Registro como Pasajero","Registro como Tripulante","Ver info pasajeros","Ver info tripulación","iniciar sesion","crear aeronave","ver info de aeronaves"])
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
                    {"ID": pasa.id,"Nombre ": pasa.name,"Telefono ": pasa.telefono,"Maletas": pasa.maleta, "Estado": pasa.state})
            if informacion:
                st.table(informacion)
            else:
                st.info("Todavia no hay pasajeros registrados")
    def verInfoTripulacion(self, lt):
        st.header("Ver info tripulantes")
        st.write("Información primordial del tripulante")
        informacion = []
        for info in lt:
            tripu = lt[info]
            informacion.append({"ID": tripu.id,"Nombre ": tripu.name,"Telefono ": tripu.telefono,"Puesto": tripu.puesto,"Estado": tripu.state})
        if informacion:
            st.table(informacion)

    def pedirId(self,num):
        ide=st.number_input("Ingresa la posición ", min_value=1,step=1,max_value=num)
        return ide

    def cualNave(self):
        sel= st.selectbox("En cúal nave deseas reservar:", ["Avión", "Helicóptero", "Jet"])
        return sel

    def error(self):
        #st.info("Por el momento no hay aeronaves disponibles")
        st.info("No hay pasajeros registrados")

    def fonfo(self):
        st.header("Aeropuerto Internacional Alfonso Bonilla Aragón")
        st.write("Una experiencia para contar :helicopter:  :airplane_departure:")
        img = Image.open('aeropuertoAlfonso.jpg')
        st.image(img,caption="Aeropuerto Internacional Alfonso Bonilla Aragón",width=735)
        st.link_button("Ver historia y la actualidad","https://www.i-torrestrella.com/aeropuerto-alfonso-bonilla-aragon-de-cali-historia-y-situacion-actual/")

