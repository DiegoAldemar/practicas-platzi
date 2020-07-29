#Decomposicion: partir un problema enorme, en problemas pequeños
#las clases permiten crear mayores abstracciones en forma dde ccomponentes
#cada clase se encarga de una parte del problema, y el programa se vuelve mas facil de manterner

class Automovil:
    def __init__(self, modelo, marca, color):
        self.modelo = modelo
        self.marca = marca
        self.color = color
        self.estado = 'En reposo'
        self.motor = Motor(cilindros=4)
        
    def Acelerar(self, tipo='despacio'):
        if tipo == 'rapido':
            self.motor.inyecta_gasolina(10)
        else:
            self.motor.inyecta_gasolina(3)
            
        self.estado = 'en movimiento'
            
        
        
class Motor:
    def __init__(self, cilindros, tipo='gasolina'):
        self.cilindros = cilindros 
        self.tipo = tipo
        self.temperatura = 0
        
        
    def inyecta_gasolina(self, cantitad):
        pass

