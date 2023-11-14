# Proyecto POO 2
### Diagrama UML

### Guía del programa
Una vez ejecutes el programa con las instruciones que se encuentaran al final de este documento se abrira tu navegador predeterminado en la pagina principal del programa, en nuesto caso seria la pestaña que muestra informacion sobre el aeropuerto.
En la parte izquierda se mostrara una pestaña de seleccion con las opciones -reservar-Registro como pasajero-Registro como tripulante-ver info pasajeros- ver info tripulantes-iniciar sesion-crear aeronave- ver info aeronaves.
Lo primero que debemos hacer es dirigirnos a Registro como pasajero, para asi poder crear el primer usuario, para posteriormente agregar y visualizar en info pasajeros, misma opcion si se elige la pestaña ingresar como tripulante.
Para reservar debe ingresar a la pestaña ver info aeronave para ver las opciones de vuelos, si ninguna es de su agrado puede dirigirse a la pestaña crear aeronave, posteriormente dirigirse a la pestaña reservar, seleccionar el id de su usuario y el id de su vuelo(lo puede consultar en la pestaña ver info pasajeros y en la pestaña info aeronaves) respectivamente. 

### Reservar

Presionamos la opcion Reservar en la parte izquierda. Esto nos redigira hacia otra pestaña con el formulario para agregar reservar.

 - Aqui podemos ingresar el valor del id del vuelo y el usuario.
 - Se muestra la cantidad de sillas disponibles en el vuelo seleccionado
 - Se muestra el nombre correspondiente al id de usuario
 - Se selecciona la nave deseada y de esta forma la reserva se hara automaticamente


### Registro de pasajero
 - **Nombre**: Aqui podemos ingresar cualquier cadena la cual correspondera al nombre de usuario.
 - **Id**: El numero de identificacion
 - **fecha de nacimiento**: Debemos elegir una fecha
 - **Genero**: Para elegir si el genero es femenino,masculino u otro
 - **Direccion de residencia**: En este campo se debe ingresar una direccion
 - **Correo electronico**: En este campo se debe ingresar el correo de contacto. 
 - **Continente**: Se debe seleccionar el continente de procedencia.
 - **Pais**: Se debe seleccionar el pais de procedencia.
 - **informacion medica**: este campo debe ser llenado con informarcion importante de salud
 - **equipaje**: se debe llenar la cantidad maletas.

### Registro de tripulante
 - **Nombre**: Aqui podemos ingresar cualquier cadena la cual correspondera al nombre de usuario.
 - **Id**: El numero de identificacion
 - **fecha de nacimiento**: Debemos elegir una fecha
 - **Genero**: Para elegir si el genero es femenino,masculino u otro
 - **Direccion de residencia**: En este campo se debe ingresar una direccion
 - **Correo electronico**: En este campo se debe ingresar el correo de contacto. 
 - **Horas de trabajo**: Se debe seleccionar la cantidad de horas laborales.
 - **Experiencia**: Se debe seleccionar la cantidad de años de experiencia.
 - **Puesto de trabajo**: se debe seleccionar el puesto al que aspira


### crear aeronave

 En este apartado tendremos todas las opciones de aeronaves y destinos.
 - **Aeronave**: se debe seleccionar la aeronave que se desea
 - **detalles**: dependiendo de la aeronave seleccionada se deben elegir las carracteristicas
 -**Destino**: se debe seleccionar los campos con el destino al que se desa viajar



# Guia para ejecutar en un host local
- Descargar la carpeta que contiene el proyecto
- Abrir el cmd, powershell o cualquier tipo de consola que utilices 
- navegar en tus archivos hasta llegar a la carpeta del programa
- utlizar el comando python streamlit run main.py
