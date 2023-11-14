import streamlit as st
import time
from PIL import Image

class viewPer:

    def menuPer(self):
        sel = st.sidebar.selectbox("Selecciona lo que se desea hacer",
                                   ["Reservar", "Registro como Pasajero", "Registro como Tripulante",
                                    "Ver info pasajeros","Ver info tripulación"])
        return sel

    #        if sel == "Reservar":
    #           pass
    #      elif sel == "Registro como Pasajero":
    #         self.datosPasajeros()
    #    elif sel == "Registro como Tripulante":
    #       self.datosTripulacion()
    #  elif sel == "Ver info pasajeros o tripulación":
    #     s = st.sidebar.selectbox("Selecciona una opcion", ["Info Pasajeros", "Info Tripulacón"])
    #    if (s == "Info Pasajeros"):
    #       self.verInfoPasajeros()
    #  elif s == "Info Tripulación":
    #     self.verInfoTripulacion()

    def nacio(self):
        paises ={"Argelia":'argelia.png', "Camerún":'acamerun.png', "Egipto":'aegipto.png', "Guinea Ecuatorial":'aguinea.png', "Madagascar":'amadagascar.png', "Marruecos":'amarruecos.png', "Nigeria":'aniggeria.png', "Sudáfrica":'asurafrica.png', "Sudán":'asudan.png'}
        n = ""
        na = st.selectbox('Seleccione su continente', ['África', 'América', 'Asia', 'Europa', 'Oceanía'])
        if na == 'África':
            n = st.selectbox('Seleccione su pais',
                             ["Argelia","Camerún", "Egipto",
                              "Guinea Ecuatorial",
                              "Madagascar",
                              "Marruecos",
                              "Nigeria",
                              "Sudáfrica",
                              "Sudán",
                              ])
            for clave in paises:
                if(clave == n):
                    image = Image.open(paises[clave])
                    st.image(image, caption='Bandera del pais al cual viaja')
        elif na == 'América':
            n = st.selectbox('Seleccione su pais', [
                'Argentina',
                'Brasil',
                'Canadá',
                'Chile',
                'Colombia',
                'Costa Rica',
                'Ecuador',
                'El Salvador',
                'Estados Unidos',
                'Guatemala',
                'México',
                'Panamá',
                'Paraguay',
                'Perú',
                'República Dominicana',
                'Venezuela'
            ])
        elif na == 'Asia':
            n = st.selectbox("Seleccione su pais", [
                'Arabia Saudita',
                'China',
                'Corea del Sur',
                'Emiratos Árabes Unidos',
                'India',
                'Indonesia',
                'Irán',
                'Israel',
                'Japón',
                'Mongolia',
                'Palestina',
                'Filipinas',
                'Qatar',
                'Rusia',
                'Tailandia',
                'Turquía'])
        elif na == 'Europa':
            n = st.selectbox("Seleccione su pais", [
                'Alemania',
                'Austria',
                'España',
                'Finlandia',
                'Francia',
                'Grecia',
                'Irlanda',
                'Islandia',
                'Italia',
                'Mónaco',
                'Portugal',
                'Reino Unido',
                'República Checa',
                'Rusia',
                'Suecia',
                'Suiza',
                'Turquía',
                'Ucrania', 'Vaticano'
            ])
        elif na == 'Oceanía':
            n = st.selectbox("Seleccione su pais",
                             ['Australia', 'Fiyi', 'Nueva Zelanda', 'Palaos'])

        return n

    def datosPasajeros(self):
        name = st.text_input("Ingresa tu nombre completo: ")
        if not name:
            st.error("Esta informacion es obligatoria")
        iden = st.number_input("ID",min_value=0, step=1)
        nacimiento = st.date_input("Ingrese la fecha de nacimiento: ")
        genero = st.selectbox('Seleccione su genero ', ['Femenino', 'Masculino', 'Otro'])
        direccion = st.text_input("Ingresa tu direccion de residencia: ")
        if not direccion:
            st.error("Esta informacion es obligatoria")
        correo = st.text_input("Ingresa tu correo: ")
        if not correo:
            st.error("Esta informacion es obligatoria")
        tel = st.number_input("Ingresa tu numero de telefono: ", min_value=0, step=1)
        nacionalidad = self.nacio()
        if nacionalidad is None:
            st.error("Esta informacion es obligatoria")
        med = st.text_area("Ingresa tu informacion medica", "Si no tienes nada, escribe No")
        if not med:
            st.error("Esta informacion es obligatoria")
        maleta = st.slider('Cuantas maletas vas a llevar?', 0, 12, 1)
        if maleta is None:
            st.error('Debes seleccionar un número.')
        enviar = st.button("Enviar Informacion Personal", type="primary")
        if enviar:
            with st.spinner('enviando...'):
                if (not name) or (not direccion) or (not correo):
                    st.error("Debes ingresar los datos obligatorios")
                else:
                    time.sleep(3)
                    st.success('Enviado!')
                    return {
                        "ID": iden,
                        "Nombre": name,
                        "Telefono": tel,
                        "Puesto": "---",
                        "Maletas": maleta
                        }

    def datosTripulacion(self):
        nombre = st.text_input("Ingrese su nombre completo: ", "")
        if not nombre:
            st.error("Esta informacion es obligatoria")
        iden = st.number_input("ID",min_value=0, step=1)
        naci = st.date_input("Ingresar fecha de nacimiento: ")
        gen = st.selectbox('Seleccione su genero ', ['Femenino', 'Masculino', 'Otro'])
        dire = st.text_input("Ingrese su direccion de residencia: ", "")
        if not dire:
            st.error("Esta informacion es obligatoria")
        corr = st.text_input("Ingrese su correo: ", "")
        if not corr:
            st.error("Esta informacion es obligatoria")
        telefono = st.number_input("Ingrese su número de telefono: ", min_value=0, step=1)
        horas = st.slider('Cuantas horas trabajas?', 1, 20, 4)
        years = st.slider('Cuantos años de experiencia tienes? ', 0, 50, 4)
        puesto = st.selectbox("Cual es tu puesto de trabajo",
                              ['Piloto', 'Copiloto', 'Tripulante de cabina', 'Policia aereo'])
        if st.button('Enviar Informacion Personal',type="primary"):
            with st.spinner('enviando...'):
                if (not nombre) or (not dire) or (not corr):
                    st.error("Debes ingresar los datos obligatorios")
                else:
                    time.sleep(3)
                    st.success('Enviado!')
                    #funcion de asignar   asignarPuesto(puesto)
                    return {
                        "ID": iden,
                        "Nombre": nombre,
                        "Telefono": telefono,
                        "Puesto": puesto,
                        "Maletas": "---"
                    }

    def verInfoPasajeros(self, lp):
        st.header("Ver info pasajeros")
        st.write("Informacion primordial del pasajero")
        informacion = []
        for info in lp:
            pasa = lp[info]
            informacion.append(
                {"Nombre ": pasa.name, "Direccion ": pasa.direccion, "Correo ": pasa.correo, "Telefono ": pasa.tel,
                 "Nacionalidad ": pasa.nacionalidad, "Informacion Medica ": pasa.med,
                 "Cantidad de Maletas": pasa.maleta, "Vuelo": pasa.vuelo})
        if informacion:
            st.table(informacion)


    def verInfoTripulacion(self, lt):
        st.header("Ver info tripulantes")
        st.write("Información primordial del tripulante")
        informacion = []
        for info in lt:
            tripu = lt[info]
            informacion.append({"Nombre ": tripu.nombre, "Direccion ": tripu.dire, "Correo ": tripu.corr,
                                "Telefono ": tripu.telefono, "Horas": tripu.horas, "Experiencia": tripu.years,
                                "Puesto": tripu.puesto, "Aerolinea": tripu.aero})
        if informacion:
            st.table(informacion)
