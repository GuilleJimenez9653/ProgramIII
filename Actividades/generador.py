import pieza
import random
import tablero

class Generador:

    def generar_pieza(self,tablero):
        p1 = pieza.Pieza()
        direccion = random.randint(0,1)
        lista = []
        if direccion == 1:
            direccion = "Vertical"
        else:
            direccion = "Horizontal"
        p1.set_direccion(direccion)
        tamano_pieza = random.randint(0,tablero.get_tamano())
        for i in range(tamano_pieza):
            lista.append(i)
        p1.set_valor(lista)
        p1.set_forma('rectangulo')
        p1.set_color('azul')
        return p1

