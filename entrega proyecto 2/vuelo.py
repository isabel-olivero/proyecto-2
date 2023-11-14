import streamlit as st
class vuelo:
    def __init__(self):
        self.sillasV= 120
        self.naves =[]
        self.origen = "Cali"
        self.sillasA = 40
        self.sillasJ = 40
        self.sillasH = 40
        self.pasajerosA = []
        self.pasajerosH = []
        self.pasajerosJ = []

        if 'Vuelo' not in st.session_state:
            st.session_state['Vuelo'] = {}
            self.liTri = {}
        else:
            self.liTri = st.session_state['Vuelo']


        def setId(self, sillasV):
            self.sillasV = sillasV

        def setName(self, sillasA):
            self.sillasA = sillasA

        def setDescription(self, sillasJ):
            self.sillasJ = sillasJ

        def setState(self, sillasH):
            self.sillasH = sillasH



    def reservar(self,selec,name): #la funcion principal que permite generar la reserva
        no=0
        if(selec=="Avión"):
            self.sillasA -= 1
            self.pasajerosA.append(name)
            no=1
        elif(selec=="Helicóptero"):
            self.sillasH -= 1
            self.pasajerosH.append(name)
            no=1
        elif(selec=="Jet"):
            self.sillasJ -= 1
            self.pasajerosJ.append(name)
            no=1
        return no
            