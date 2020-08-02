'''
Herencia:
permite modelar una jerarquia de clases
permite compartir comportamiento comun en la jerarquia
al padre se le conoce como superclase y al hijo como subclase
'''

class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
        
    def area(self):
        return self.base * self.altura
    
    
class Cuadrado(Rectangulo):
    def __init__(self, lado):
        super().__init__(lado, lado)  #permite obterner una referencia de la superclase, que en este caso es el Rectangulo
        
if __name__ == '__main__':
    #rectangulo = Rectangulo(3, 4)
    #print(rectangulo.area())
    
    cuadrado = Cuadrado(4)
    print(cuadrado.area()) #aqui notamos la herencia cuando la clase Cuadrado hereda la funcion de area de la super clase
    
        
