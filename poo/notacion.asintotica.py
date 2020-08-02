'''
crecimiento asintótico:
no importan variaciones pequeñas
el enfoque se centra en lo que pasa conforme el tamaño del problema se acerca al infinito


Un loop => crecimiento lineal.
Un loop dentro de otro => crecimiento cuadratico
Llamadas recursivas => crecimiento exponecncial.


Clases de complejidad algorítmica
Existen distintos tipos de complejidad algorítmica:

O(1) Constante: no importa la cantidad de input que reciba, siempre demorara el mismo tiempo.
O(n) Lineal: la complejidad crecerá de forma proporcional a medida que crezca el input.
O(log n) Logarítmica: nuestra función crecerá de forma logarítmica con respecto al input. Esto significa que en un inicio crecerá rápido, pero luego se estabilizara.
O(n log n) Log lineal: crecerá de forma logarítmica pero junto con una constante.
O(n²) Polinomial: crecen de forma cuadrática. No son recomendables a menos que el input de datos en pequeño.
O(2^n) Exponencial: crecerá de forma exponencial, por lo que la carga es muy alta. Para nada recomendable en ningún caso, solo para análisis conceptual.
O(n!) Factorial: crece de forma factorial, por lo que al igual que el exponencial su carga es muy alta, por lo que jamas utilizar algoritmos de este tipo.

'''

#ley de la suma
def f(n):
    for i in range(n):
        print(i)
        
    for i in range(n):
        print(i)
        
#O(n) + O(n) = O(n+n) = O(2n) = O(n) la funcion crece en O de n

def f(n):
    for i in range(n):
        print(i)
        
    for i in range(n * n):
        print(i)

#O(n) + O(n*n) = O(n+n^2) = O(n^2) la funcion crece en O de n^2


#ley de la multiplicacion
def f(n):
    for i in range(n):
        for j in range(n):
            print(i,j)
            
#O(n)*O(n) = O(n^2)


def fibonacci(n):
    if n==0 or n==1:
        return 1
    return fibonacci(n-1) + fibonacci(n - 2)
#O(2**n) o O(2n^2)