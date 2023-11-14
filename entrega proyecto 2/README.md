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


### Añadir animal 
 - **Nombre**: aqui podemos ingresar cualquier cadena (Asi se llamara nuestro animal).
 - **Edad**: La edad de nuestro animal (Puse un limite de 100)
 - **Tamaño**: Debemos elegir entre pequeño, mediano y grande, esta eleccion afectara directamente en la capacidad de nuestro habitat debido que un animal pequeño ocupara 1 slot, el mediano 2 y el grande 3.
 - **Dieta**: Para elegir si el animal es Carnivoros, Omnivoros o herbivoros
 - **Especie**: Elegir la clasificacion de nuestro animal (Luego usaremos para validar si el animal puede entrar al habitat)
 - **Temperatura**: La temperatura necesaria para que nuestro animal pueda vivir (Luego usaremos para validar si el animal puede entrar al habitat). 
 - **Salud**: El estado actual del animal.
 - **habitats**: Aqui podemos selecionar a que habitat queremos añadir 

Luego tendremos las actividades, existe hasta 3 (Depende de que tipo de animal estamos creando)
 - **Comidas al dia**: Elegimos cuantas veces podemos alimentar al animal
 - **Horas dormidas**: La cantidad de horas que puede dormir nuestro animal.
 - **Horas de juego**: Elegimos cuantas horas puede jugar nuestro animal.


### Listar hábitats y animales

 En este apartado tendremos todos los habitats y animales creados con las opciones dormir, jugar y comer segun corresponda.

 - Dormir: Al darle click haremos que el animal duerma 1 hora, se puede precionar varias veces hasta que las horas dormidas sean igual a las horas permitidas, si tratas de precionarlo de nuevo se mostrara un aviso que el animal no puede dormir mas

 - Jugar: Al darle click haremos que el animal juegue 1 hora, se puede precionar varias veces hasta que las horas dormidas sean igual a las horas permitidas, si tratas de precionarlo de nuevo se mostrara un aviso que el animal no puede jugar mas

 - Comer: Al darle click haremos que el animal coma 1 unidad, se puede precionar varias veces hasta que las horas dormidas sean igual a las horas permitidas, si tratas de precionarlo de nuevo se mostrara un aviso que el animal no pueda comer mas


# Guia para ejecutar en un host local
- Descargar o clonar el repositorio
- Abrir el cmd, powershell o cualquier tipo de consola que utilices 
- navegar en tus archivos hasta llegar a la carpeta del programa
- utlizar el comando python -m streamlit run Info.py
