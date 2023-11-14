import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
st.title('Informacion que debes tener en cuenta antes de viajar')


def nacio(self):
        flag = 0
        paises ={"Argelia":'argelia.png', "Camerún":'acamerun.png', "Egipto":'aegipto.png', "Guinea Ecuatorial":'aginea.png', "Madagascar":'amadagascar.png', "Marruecos":'amarruecos.png', "Nigeria":'aniggeria.png', "Sudáfrica":'asurafrica.png', "Sudán":'asudan.png'}
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