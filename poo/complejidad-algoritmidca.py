'''
complejidad algorítmica:
permite comparar la eficiencia entre 2 algoritmos
complejidad temporal vs complejidad espacial
complegidad temporal: se define como T(input(n)) determina el tiempo que tardara el alguritmo
'''
import time

def factorial(n):
    respuesta = 1
    
    while n>1:
        respuesta *= n
        n -= 1
    return respuesta


def factori_recursivo(n):
    if n == 1:
        return 1
    
    return n * factorial(n -1)


if __name__ == '__main__':

    n = 500000
    
    comienzo = time.time()
    factorial(n)
    final = time.time()
    print(final- comienzo)
    
    
    comienzo = time.time()
    factori_recursivo(n)
    final = time.time()
    print(final - comienzo)
    
