# Proyecto POO 2
### Diagrama UML
https://app.diagrams.net/#G1gGzPHcVHrZBGxr4V1liCN0Aj2rsWrvsm

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


### Registrar como pasajero 
 - **Nombre**: aqui podemos ingresar nuestro nombre
 - **ID**: en este campo se debe ingesar el numero de identificacion 
 - **fecha**: en este campo se debe ingresar su fecha de nacimiento
 - **genero**: en este capo se debe seleccionar su genero
 - **direccion**: en este campo debe ingresar su direccion de residencia
 - **procedencia**: en estos campos debe seleccionar su continente y pais de origen
 - **informacion medica**: en este campo debe ingresar informacion medica de importancia
 - **equipaje**: en este campo debe seleccionar el tamaño de su equipaje



### Registrar como tripulante
 - **Nombre**: aqui podemos ingresar nuestro nombre
 - **ID**: en este campo se debe ingesar el numero de identificacion 
 - **fecha**: en este campo se debe ingresar su fecha de nacimiento
 - **genero**: en este capo se debe seleccionar su genero
 - **direccion**: en este campo debe ingresar su direccion de residencia
 - **procedencia**: en estos campos debe seleccionar su continente y pais de origen
 - **Jornada laboral**: en este campo debe ingresar sus horas de trabajo
 - **Experiencia**: en este campo se debe seleccionar sus años de experiencia laboral
 - **Puesto**: en este campo debe seleccionar el puesto al que aspira

### Crear aeronave
- **vuelo**: en estos tres campos dede seleccionar la aeronave, la categoria, y la aerolinea
- **Destino**: en estos campos debe seleccionar el destino deseado

# Guia para ejecutar en un host local
- Descargar la carpeta
- Abrir el cmd, powershell o cualquier tipo de consola que utilices 
- navegar en tus archivos hasta llegar a la carpeta del programa
- utlizar el comando python streamlit run main.py
