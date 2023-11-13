class aeropuerto:
    def __init__(self,name):
        self.nombre= name
        self.histVuelos=[]
    
    def crearVuelo(des,date,id):
        nave= crearAeronave()#funcion que crea la aeronave
        n = nave.sillas# numero de sillas de la aeronave
        vuelo = vuelo(des,date,n,id)
        print("su vuelo se ha creado exitosamente:")
        vuelo.mostrarVuelo()
        
