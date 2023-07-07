"""
    Escribir una función que reciba por parámetro una dimensión 𝑛, e imprima la
    matriz identidad correspondiente a esa dimensión.
"""

def matriz_identidad(dimension):
    # Imprime la matriz identidad según su dimensión

    for i in range(dimension):
        print("")
        for j in range(dimension):
            if i==j:
                print("1",end=" ")
            else:
                print("0",end=" ")
    print("")

matriz_identidad(5)
matriz_identidad(3)
matriz_identidad(10)