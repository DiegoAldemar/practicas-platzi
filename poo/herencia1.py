from random import randint


class Musica_aleatoria:
    def __init__(self, siguiente, artista=None, cancion=None):
        self.siguiente = siguiente
        self.artista = artista
        self.cancion = cancion
        self.num_cancion = None
        
    def canciones(self):
        self.num_cancion = randint(1, self.siguiente)
        if self.num_cancion == 1:
            return 'estas escuchando adele - someone'
        if self.num_cancion == 2:
            return 'estas escuchando avicii - wake'
        if self.num_cancion == 3:
            return 'estas escuchando eminem - love'
        
        #return f'cancion aleatoria: {self.num_cancion}'
    
    def nombre_cancion(self):
        return f'estas escuchando {self.artista} - {self.cancion}'
        
class Musica_normal(Musica_aleatoria):
    def __init__(self, artista, cancion):
        super().__init__(0, artista, cancion)

if __name__ == '__main__':
    
    cancion_aleatoria = int(input('digite numero: '))
    musica = Musica_aleatoria(cancion_aleatoria)
    print(musica.canciones())
    
    normal = Musica_normal(input('busque su artista: '), input('busque su cancion: '))
    print(normal.nombre_cancion())
        
