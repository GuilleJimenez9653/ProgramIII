class Pieza:
    
    def set_valor(self,valor):
        self._valor = valor
    
    def get_valor(self):
        return self._valor
    
    def set_forma(self,forma):
        self._forma = forma

    def get_forma(self):
        return self._forma

    def set_color(self,color):
        self._color = color
    
    def get_color(self):
        return self._color

    def mostrar(self):
        print('Valor:', self.get_valor())
        print('Forma:', self.get_forma())
        print('Color:', self.get_color())