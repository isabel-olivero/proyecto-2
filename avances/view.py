
#torre--------------------------------------------------------------
def ubicarPuerta(self, aero):
        dispo = puerta()
        nave = aero
        flag = 0
        i = 0

        while((i < len(self.embarques)) and (flag == 0)):
            if(self.embarques[i].verEstado() == True):
                embarques[i].cambiarEstado(False)
                dispo = embarques[i]
                flag = 1
                aero.ubi= dispo
            else:
                i+= 1
        print("la nave" aero "ha sido a signada a la puerta" dispo)
        return(aero,dispo)

# Puerta_-------------------------------------------------------------------
def infoEstado(self):
        ans = self.dispo
        print(ans)


#vuelo---------------------------------------------------------------------------
 def reservar(pasajero):
        if (self.sillasV > 0):
            sillas -= 1
            self.pasajeros.append(pasajero)

        else:
            print("No es posible reservar")