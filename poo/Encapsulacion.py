'''
Encapsulacion:getters and setters
permite agrupar datos y su comportamiento
controla el acceso a dichos datos
previene modificaciones no autorizadas
'''

class Casilladevotacion:
    def __init__(self, identificador, pais):
        self._identificador=identificador
        self._pais = pais
        self._region = None
        
    @property  #Decoradores, define la funcion como una propiedad
    def region(self):
        return self._region
    
    @region.setter
    def region(self, region):
        if region in self._pais:
            self._region = region
        raise ValueError(f'La region {region} no es valida en {self._pais}')# muestra un error con ese mensaje
    
casilla = Casilladevotacion(123, ['ciudad de mexico', 'morelos'])

print(casilla.region)

casilla.region = 'mexico'
print(casilla.region)
