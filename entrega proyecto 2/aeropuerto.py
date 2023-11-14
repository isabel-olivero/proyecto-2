import vuelo
import aerolinea
import aeronave
import viewGeneral
import streamlit as st
import time
import random
import paises
class aeropuesto:
    def __init__(self):
        self.avion = aeronave.Avion(id = 0,tipo="",velocidad=0, cantPas=0, autonomia=0, yearFab=0, estado="", ubi="", marca="", modelo="", destino="", cap=0, copi=0, az=0, pol=0,
                 altMax=0, cantMotor=0, categoria="",propietario="")
        self.heli = aeronave.Helicoptero(id=0 , tipo="",velocidad=0, cantPas=0, autonomia=0, yearFab=0, estado="", ubi="", marca="", modelo="",destino="", cap=0, copi=0, az=0, pol=0, rotores=0,
                 capEle=0, categoria="",propietario="")
        self.jet = aeronave.Jet(id=0, tipo="",velocidad=0, cantPas=0, autonomia=0, yearFab=0, estado="", ubi="", marca="", modelo="", destino="", cap=0, copi=0, az=0, pol=0,
                 propietario="", servicios="", desFre=[])
        self.vuelo = vuelo.vuelo()
        self.pais = paises.pais()
        

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
        #self.avion.destino = viewGeneral.viewGeneral().persona.nacio()
        self.avion.destino = self.pais.selecpais()
        if st.button('Creando nave',type="primary"):
            with st.spinner('enviando...'):
                time.sleep(3)
                st.success('Enviado!')
                self.vuelo.sillasA += self.avion.cantPas
                self.vuelo.sillasV += self.avion.cantPas
                return {
                    "ID": self.avion.id,
                    "Tipo de nave": self.avion.tipo,
                    "Año de viejo": self.avion.yearFab,
                    "Estado":  self.avion.estado,
                    "Marca": self.avion.marca,
                    "Modelo": self.avion.modelo,
                    "Destino": self.avion.destino,
                    "Sillas": self.avion.cantPas,
                    "Categoria": self.avion.categoria,
                    "Propietario": "---------------"
                }
            
    def mostrarAerolineas():
        return self.aerolineas
    

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
        self.heli.destino = self.pais.selecpais()
        self.heli.categoria = categoria
        self.heli.modelo = "Top AirService"
        self.heli.estado = "En servicio"
        if st.button('Creando nave', type="primary"):
            with st.spinner('enviando...'):
                time.sleep(3)
                st.success('Enviado!')
                self.vuelo.sillasH += self.heli.cantPas
                self.vuelo.sillasV += self.heli.cantPas
                return {
                    "ID": self.heli.id,
                    "Tipo de nave": self.heli.tipo,
                    "Año de viejo": self.heli.yearFab,
                    "Estado": self.heli.estado,
                    "Marca": self.heli.marca,
                    "Modelo": self.heli.modelo,
                    "Destino":self.heli.destino,
                    "Sillas": self.heli.cantPas,
                    "Categoria": self.heli.categoria,
                    "Propietario": "---------------"
                }
    def generarJet(self):
        self.jet.tipo = "Jet"
        self.jet.yearFab = random.randint(2000, 2023)
        self.jet.velocidad = random.randint(5, 15)
        self.jet.cantPas = random.randint(10, 20)
        self.jet.autonomia = random.randint(15, 30)
        self.jet.marca = viewGeneral.viewGeneral().marca()
        self.jet.propietario = viewGeneral.viewGeneral().propi()
        st.write("Selcciona el destino")
        self.jet.destino = self.pais.selecpais()
        self.jet.modelo = "Top AirService"
        self.jet.estado = "En servicio"
        if st.button('Creando nave', type="primary"):
            if not self.jet.propietario:
                st.error("Le recuerdo que debe ingresar un nombre")
            else:
                with st.spinner('enviando...'):
                    time.sleep(3)
                    st.success('Enviado!')
                    self.jet.cantPas += self.jet.cantPas
                    self.vuelo.sillasV +=  self.jet.cantPas
                    return {
                        "ID": self.jet.id,
                        "Tipo de nave": self.jet.tipo,
                        "Año de viejo": self.jet.yearFab,
                        "Estado": self.jet.estado,
                        "Marca": self.jet.marca,
                        "Modelo": self.jet.modelo,
                        "Destino": self.jet.destino,
                        "Sillas": self.jet.cantPas,
                        "Categoria": "-------------",
                        "Propietario": self.jet.propietario
                    }
