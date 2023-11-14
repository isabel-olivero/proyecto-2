import streamlit as st
import per
import controller
def main():
    #st.title("Mi Aplicación Streamlit")
    #servicios = st.selectbox("Selecciona los servicios que desees", ["Servicio 1", "Servicio 2", "Servicio 3"])
    #st.write('Servicios seleccionados:', servicios)
    controller.control().menu()


main()