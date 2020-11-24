import pieza
class Tablero:

    def set_tamano(self,tamano_i,tamano_j):
        self._tamano_i = tamano_i
        self._tamano_j = tamano_j

    def get_tamano(self):
        return self._tamano

    def set_matriz(self):
        self._filas = []
        self._columnas = []
        for i in range(self._tamano_i):
            for i in range(self._tamano_j):
                self._columnas.append(-1)
            self._filas.append(self._columnas)
            self._columnas = []
    
    def get_matriz(self):
        return self._filas
    
    def imprimir_matriz(self):
        print(self.get_matriz())

    def generar_tablero(self,tamano_i,tamano_j):
        t = Tablero()
        t.set_tamano(tamano_i,tamano_j)

    #def ubicar_pieza(pieza, region):
