import generador
import tablero

G = generador.Generador()
tablero = tablero.Tablero()
tablero.set_tamano(5,5)
tablero.set_matriz()
p1 = G.generar_pieza()
p1.mostrar()
tablero.imprimir_matriz()