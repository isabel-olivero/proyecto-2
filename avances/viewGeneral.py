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

    def pedirId(self):
        id = st.number_input("Ingresa tu id",min_value= len(model.modelo().retornarP()),step=1)
        return id

    def pedirId2(self):
        number = st.slider("Ingresa la posición de la nave que desee", min_value=1, max_value=10)
        return number


    def cualNave(self):
        sel= st.selectbox("En cúal nave deseas reservar:", ["Avión", "Helicóptero", "Jet"])
        return sel

    def error(self):
        #st.info("Por el momento no hay aeronaves disponibles")
        st.info("Por el momento no se puede reservar")

    def fondo(self):
        st.header("Aeropuerto Internacional Alfonso Bonilla Aragón")
        st.write("Una experiencia para contar :helicopter:  :airplane_departure:")
        img = Image.open('aeropuertoAlfonso.jpg')
        st.image(img,caption="Aeropuerto Internacional Alfonso Bonilla Aragón",width=735)
        st.link_button("Ver historia y la actualidad","https://www.i-torrestrella.com/aeropuerto-alfonso-bonilla-aragon-de-cali-historia-y-situacion-actual/")

    def seleccionaCategoria(self,nave):
        if(nave == "Avión"):
            sele = st.selectbox("Selecciona categoria de Avión",["Carga","Transporte","Militar"])
            return sele
        elif(nave == "Helicóptero"):
            sele = st.selectbox("Selecciona categoria de Helicóptero",["Rescate", "Turismo", "Transporte","Fuerza policial", "Ambulancia" ])
            return sele

    def marca(self):
        mar = st.selectbox("Selecciona la marca de la aeronave",["ArgueFlight","GIAL Air","Latem","AC Air","AFGM"])
        return mar

    def nave(self):
        nav = st.selectbox("Selecciona la nave que se desee crear",["Avión","Helicóptero","Jet"])
        return nav

    def verInfoNaves(self, nave):
        st.header("Ver informacion de aeronaves")
        st.write("Información primordial de la aeronave")
        informacion = []
        for info in nave:
            n = nave[info]
            informacion.append({"ID": n.id,"Tipo de nave": n.tipo,"Año de viejo": n.yearFab,"Estado": n.estado,"Marca": n.marca,"Modelo": n.modelo,"Destino": n.destino,"Sillas": n.per,"Categoria": n.categoria,"Propietario": n.propietario })
        if informacion:
            st.table(informacion)


    def propi(self):
        nombre= st.text_input("Ingresa nombre de propietario")
        if not nombre:
            st.error("Debes ingreasar un nombre")
        else:
            return nombre
