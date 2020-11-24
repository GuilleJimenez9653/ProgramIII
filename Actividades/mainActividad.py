import generador
import tablero

G = generador.Generador()
tablero = tablero.Tablero()
tablero.set_tamano(5,5)
tablero.set_matriz()
p1 = G.generar_pieza(tablero)
p1.mostrar()
tablero.imprimir_matriz()
tablero.ubicar_pieza(p1)
tablero.imprimir_matriz()
