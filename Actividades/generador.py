import pieza
import random
class Generador:

    def generar_pieza(self):
        p1 = pieza.Pieza()
        p1.set_valor(random.randint(1,4))
        p1.set_forma('rectangulo')
        p1.set_color('azul')
        return p1
