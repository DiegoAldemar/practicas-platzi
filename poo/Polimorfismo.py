'''
Polimorfismo: 
habilidad de tomar varias formas
En python, nos permite cambiar el comportamiento de una superclase para adaptarlo a la subclase
'''

class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
        
    def avanza(self):
        print('ando caminando')
        
class Ciclista(Persona):
    def __init__(self, nombre):
        super().__init__(nombre)
        
    def avanza(self):
        print('ando moviendome en la bici')
        
def main():
    persona = Persona('davis')
    persona.avanza()
    
    ciclista = Ciclista('daniel')
    ciclista.avanza()
    
        
if __name__ == '__main__':
    main()
    

