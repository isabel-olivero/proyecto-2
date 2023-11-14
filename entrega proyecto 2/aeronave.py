import viewGeneral
import random
import streamlit as st
import time

class Aeronave:
    def __init__(self, tipo,velocidad, id,cantPas, autonomia, yearFab, estado, ubi, marca, modelo, destino,propietario,cap, copi, az, pol):
        self.velocidad = velocidad
        self.cantPas = cantPas
        self.autonomia = autonomia
        self.yearFab = yearFab
        self.estado = estado
        self.ubi = ubi
        self.id = id
        self.marca = marca
        self.modelo = modelo
        self.destino = destino
        self.tipo = tipo
        self.creadas = []
        self.origen = "Cali"
        self.cap = cap
        self.copi = copi
        self.az = az
        self.pol = pol



class Avion(Aeronave):
    def __init__(self, velocidad, cantPas,id, autonomia, yearFab, estado, ubi, marca, modelo, destino,tipo,propietario, cap, copi, az, pol,
                 altMax, cantMotor, categoria):
        super().__init__(velocidad, cantPas, id,autonomia, yearFab, estado, ubi, marca, modelo, destino,tipo,propietario, cap, copi, az,
                         pol)
        self.altMax = altMax
        self.cantMotor = cantMotor
        self.categoria = categoria
        self.estado = estado
        self.destino = destino
        self.tipo = tipo
        self.cap = cap
        self.copi = copi
        self.az = az
        self.pol = pol

    def verCate(self):
        print(f"Esta es la categoria de este avion = {self.categoria}")


class Helicoptero(Aeronave):
    def __init__(self, velocidad, cantPas, autonomia, yearFab, estado, ubi, marca, modelo,destino,tipo,propietario, cap, copi, az, id,pol, rotores,
                 capEle, categoria):
        super().__init__(velocidad, cantPas, autonomia, yearFab, estado, ubi, marca, modelo,destino,tipo,propietario,cap, copi, az, pol,id)
        self.rotores = rotores
        self.capEle = capEle
        self.categoria = categoria
        self.tipo = tipo
        self.cap = cap
        self.copi = copi
        self.az = az
        self.pol = pol

    def verUso(self):
        print(f"Este es el uso que se le da al helicoptero {self.categoria}")




class Jet(Aeronave):
    def __init__(self, velocidad, cantPas, autonomia, yearFab, estado, ubi, marca, modelo,destino,tipo,cap, copi, az, pol,id,
                 propietario, servicios, desFre):  # desFre == destinos frecuentes
        super().__init__(velocidad, cantPas, autonomia, yearFab, estado, ubi, marca, modelo,destino,tipo,propietario,cap, copi, az, pol,id)
        self.propietario = propietario
        self.servicios = "\n1.Mayordomo a bordo\n2.Spa a bordo\n3.Tripulación profesional\n4.Wi-Fi a bordo\n5.Entretenimiento a bordo\n6.Bar y bebidas\n7.Catering gourmet\n8.Conserje personal\n\n"
        self.desFre = desFre
        self.cap = cap
        self.copi = copi
        self.az = az
        self.pol = pol

    def verServicios(self):
        print(f"Estos son los servicios dados por el Jet = {self.servicios} ")