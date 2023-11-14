import streamlit as st
import pandas as pd
import numpy as np

st.title('Informacion que debes tener en cuenta antes de viajar')

def selecpais(self):
        paises ={"Argelia":['argelia.png', "La moneda de Argelia es el :blue[Dinar argelino], Se recomienda tener buen manejo del :blue[Arabe]" ]
                 , "Camerún":['acamerun.png',"La moneda de Camerun es el :blue[Franco CFA], Se recomienda tener buen manejo del :blue[Ingles]" ], "Egipto":['aegipto.png', "La moneda de Egipto es la :blue[Libra Egipcia], Se recomienda tener buen manejo del :blue[Arabe]"], 
                 "Guinea Ecuatorial":['aguinea.png', "La moneda de Ginea Ecuatorial es el :blue[Franco CFA], Se recomienda tener buen manejo del :blue[Frances]"],
                   "Madagascar":['amadagascar.png',"La moneda de Madagascar es el :blue[Ariary Malgache], Se recomienda tener buen manejo del :blue[Frances]"], 
                   "Marruecos":['amarruecos.png', "La moneda de Marruecos es el :blue[Dirham Marroqui], Se recomienda tener buen manejo del :blue[Arabe]"], 
                   "Nigeria":['aniggeria.png', "La moneda de Nigeria es el :blue[Naira], Se recomienda tener buen manejo del :blue[Ingles]"],
                    "Sudáfrica":['asurafrica.png',"La moneda de Sudafrica es :blue[el Rand], Se recomienda tener buen manejo del :blue[Ingles]" ], 
                    "Sudán":['asudan.png', "La moneda de Sudan es la :blue[libra sursudanesa], Se recomienda tener buen manejo del :blue[Arabe y del Ingles]"]}
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
            for clave in paises:#muestra info del pais
                if(clave == n):
                    image = Image.open(paises[clave][0])
                    st.image(image, caption='Bandera del pais al cual viaja')
                    st.subheader(paises[clave][1])

                
        elif na == 'América':
            paises1={'Argentina':['argentina.png',"La moneda de Argentina es el :blue[Peso argentino], Se recomienda tener buen manejo del :blue[Español]"],
                'Brasil':['brazil.png',"La moneda de Brazil es el :blue[Real], Se recomienda tener buen manejo del :blue[Portugues]"],
                'Canadá':['canada.png',"La moneda de Canada es el :blue[Dolar Canadiense], Se recomienda tener buen manejo del :blue[Ingles y Frances]"],
                'Chile':['chile.png',"La moneda de Chile es el :blue[Peso chileno], Se recomienda tener buen manejo del :blue[Español]"],
                'Costa Rica':['costari.png',"La moneda de Costa Rica es el :blue[Colon], Se recomienda tener buen manejo del :blue[Español]"],
                'Ecuador':['ecuador.png',"La moneda de Ecuador es el :blue[Dolar], Se recomienda tener buen manejo del :blue[Español]"],
                'El Salvador':['salvador.png',"La moneda de Salvador es el :blue[Colon], Se recomienda tener buen manejo del :blue[Español]"],
                'Estados Unidos':['estados.png',"La moneda de Estados Unidos es el :blue[Dolar], Se recomienda tener buen manejo del :blue[Ingles]"],
                }
            
            n = st.selectbox('Seleccione su pais', [
                'Argentina',
                'Brasil',
                'Canadá',
                'Chile',
                'Costa Rica',
                'Ecuador',
                'El Salvador',
                'Estados Unidos'
            ])

            for clave in paises1:#muestra info del pais
                if(clave == n):
                    image = Image.open(paises1[clave][0])
                    st.image(image, caption='Bandera del pais al cual viaja')
                    st.subheader(paises1[clave][1])

        elif na == 'Asia':
            paises2={
                'China':['china.png',"La moneda de China es el :blue[Yuan], Se recomienda tener buen manejo del :blue[Chino]"],
                'Corea del Sur':['corea.png',"La moneda de Corea del Sur es el :blue[Won], Se recomienda tener buen manejo del :blue[Coreano]"],
                'Emiratos Árabes Unidos':['emiratos.png',"La moneda de Emiratos Árabes Unidos es el :blue[Dirham], Se recomienda tener buen manejo del :blue[Ingles]"],
                'India':['india.png',"La moneda de India es la :blue[Rupia], Se recomienda tener buen manejo del :blue[Ingles]"],
                'Indonesia':['indonesia.png',"La moneda de Indonesia es el :blue[Rupia], Se recomienda tener buen manejo del :blue[Ingles]"],
                'Japón':['japon.png',"La moneda de Japón es el :blue[Yen], Se recomienda tener buen manejo del :blue[Japones]"],
                'Qatar':['qtar.png',"La moneda de Qatar es el :blue[Riyal], Se recomienda tener buen manejo del :blue[Arabe]"],
                'Turquía':['turquia.png',"La moneda de Turquía es la :blue[lLira], Se recomienda tener buen manejo del :blue[Arabe]"]}
            n = st.selectbox("Seleccione su pais", [
                'China',
                'Corea del Sur',
                'Emiratos Árabes Unidos',
                'India',
                'Indonesia',
                'Japón',
                'Qatar',
                'Turquía'])
            for clave in paises2:#muestra info del pais
                if(clave == n):
                    image = Image.open(paises2[clave][0])
                    st.image(image, caption='Bandera del pais al cual viaja')
                    st.subheader(paises2[clave][1])


        elif na == 'Europa':
            paises3={'Alemania': ['alemania.png', "La moneda de Alemania es el :blue[Euro], Se recomienda tener buen manejo del :blue[Aleman]" ],
                'Austria':['austria.png', "La moneda de Austria es el :blue[Euro], Se recomienda tener buen manejo del :blue[Ingles]" ],
                'Francia':['francia.png', "La moneda de Francia es el :blue[Euro], Se recomienda tener buen manejo del :blue[Frances]" ],
                'Grecia':['grecia.png', "La moneda de Grecia es el :blue[Euro], Se recomienda tener buen manejo del :blue[Ingles]" ],
                'Islandia':['islandia.png', "La moneda de  Islandia es la :blue[Corona], Se recomienda tener buen manejo del :blue[Ingles]" ],
                'Italia':['italia.png', "La moneda de Italia es el :blue[Euro], Se recomienda tener buen manejo del :blue[Italiano]" ],
                'Reino Unido':['reino.png', "La moneda de Reino Unido es el :blue[Libra esterlina], Se recomienda tener buen manejo del :blue[Ingles]" ],
                'Suiza':['suiza.png', "La moneda de Suiza es el :blue[Franco], Se recomienda tener buen manejo del :blue[Ingles]" ],}
            
            n = st.selectbox("Seleccione su pais", [
                'Alemania',
                'Austria',
                'Francia',
                'Grecia',
                'Islandia',
                'Italia',
                'Reino Unido',
                'Suiza',
                
            ])

            for clave in paises3:#muestra info del pais
                if(clave == n):
                    image = Image.open(paises3[clave][0])
                    st.image(image, caption='Bandera del pais al cual viaja')
                    st.subheader(paises3[clave][1])

        elif na == 'Oceanía':
            paises4={'Australia':['naustralia.png', "La moneda de  es el :blue[Dolar australiano], Se recomienda tener buen manejo del :blue[Ingles]" ], 
                     'Fiyi':['fiyi.png', "La moneda de  es el :blue[Dolar Fiyiano ], Se recomienda tener buen manejo del :blue[Ingles]" ], 
                     'Nueva Zelanda':['nueva.png', "La moneda de  es el :blue[Dolar Neozelandes], Se recomienda tener buen manejo del :blue[Ingles]" ], 
                     'Palaos':['palaos.png', "La moneda de  es el :blue[Dolar], Se recomienda tener buen manejo del :blue[Ingles]" ]}
            
            n = st.selectbox("Seleccione su pais",
                             ['Australia', 'Fiyi', 'Nueva Zelanda', 'Palaos'])
            for clave in paises4:#muestra info del pais
                if(clave == n):
                    image = Image.open(paises4[clave][0])
                    st.image(image, caption='Bandera del pais al cual viaja')
                    st.subheader(paises4[clave][1])

        return n