'''
Abstraccion: enfocarnos en la informacion relevante
separar la informacion central de los detalles secundarios
podemos utilizar variables y metodos(privados o publicos)
'''

class Lavadora:
    def __init__(self):
        pass
    
    
    def lavar(self, temperatura='caliente'):
        self._llenar_tanque(temperatura)
        self._añadir_jabon()
        self._lavar()
        self._centrifugar()
        
    def _llenar_tanque(self, temperatura):
        print(f'llenando el tanque con agua {temperatura}')
        
    def _añadir_jabon(self):
        print('añadiendo jabon')
        
    def _lavar(self):
        print('lavando la ropa')
        
    def _centrifugar(self):
        print('centrifugando...')
        
        
if __name__ == '__main__':
    _lavadora= Lavadora()
    _lavadora.lavar()
    
