import vuelo
import aeronave
import viewGeneral
import streamlit as st
import time
import random
class aeropuesto:
    def __init__(self):
        self.avion = aeronave.Avion(tipo="",velocidad=0, cantPas=0, autonomia=0, yearFab=0, estado="", ubi="", marca="", modelo="", destino="", cap=0, copi=0, az=0, pol=0,
                 altMax=0, cantMotor=0, categoria="")
        self.heli = aeronave.Helicoptero(tipo="",velocidad=0, cantPas=0, autonomia=0, yearFab=0, estado="", ubi="", marca="", modelo="",destino="", cap=0, copi=0, az=0, pol=0, rotores=0,
                 capEle=0, categoria="")

    def generarAvion(self):
        self.avion.tipo = "Avión"
        categoria = viewGeneral.viewGeneral().seleccionaCategoria("Avión")
        self.avion.categoria = categoria
        self.avion.modelo = "Top AirService"
        self.avion.marca = viewGeneral.viewGeneral().marca()
        years = random.randint(2000, 2023)
        sillas = random.randint(10, 20)
        altmax = random.randint(5, 15)
        motor = random.randint(1, 5)
        self.avion.cantPas = sillas
        self.avion.yearFab = years
        self.avion.altMax = altmax
        self.avion.velocidad = altmax
        self.avion.autonomia= altmax
        self.avion.cantMotor = motor
        self.avion.estado = "En servicio"
        st.write("Selcciona el destino")
        self.avion.destino = viewGeneral.viewGeneral().persona.nacio()
        if st.button('Creando nave',type="primary"):
            with st.spinner('enviando...'):
                time.sleep(3)
                st.success('Enviado!')
                return {
                    "Tipo de nave": self.avion.tipo,
                    "Año de viejo": self.avion.yearFab,
                    "Estado":  self.avion.estado,
                    "Marca": self.avion.marca,
                    "Modelo": self.avion.modelo,
                    "Destino": self.avion.destino,
                    "Sillas": self.avion.cantPas,
                    "Categoria": self.avion.categoria
                }

    def generarHelicoptero(self):
        self.heli.tipo = "Helicóptero"
        self.heli.rotores = random.randint(1, 5)
        self.heli.capEle = random.randint(10, 40)
        self.heli.yearFab = random.randint(2000, 2023)
        self.heli.velocidad = random.randint(5, 15)
        self.heli.cantPas = random.randint(10, 20)
        self.heli.autonomia = random.randint(15, 30)
        categoria = viewGeneral.viewGeneral().seleccionaCategoria("Helicóptero")
        self.heli.marca = viewGeneral.viewGeneral().marca()
        st.write("Selcciona el destino")
        self.heli.destino = viewGeneral.viewGeneral().persona.nacio()
        self.heli.categoria = categoria
        self.heli.modelo = "Top AirService"
        self.heli.estado = "En servicio"
        if st.button('Creando nave', type="primary"):
            with st.spinner('enviando...'):
                time.sleep(3)
                st.success('Enviado!')
                return {
                    "Tipo de nave": self.heli.tipo,
                    "Año de viejo": self.heli.yearFab,
                    "Estado": self.heli.estado,
                    "Marca": self.heli.marca,
                    "Modelo": self.heli.modelo,
                    "Destino":self.heli.destino,
                    "Sillas": self.heli.cantPas,
                    "Categoria": self.heli.categoria
                }
