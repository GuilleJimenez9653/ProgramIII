import generador
import tablero

G = generador.Generador()
tablero = tablero.Tablero()
tablero.set_tamano(5,5)
p1 = G.generar_pieza()
p1.mostrar()