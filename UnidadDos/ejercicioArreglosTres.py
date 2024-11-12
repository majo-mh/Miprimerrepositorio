"""
Dado el siguiente arreglo de números: [1, 5, 8, 3, 30, 9, 13]
Imprimir en pantalla programáticamente los números impares mayores a 3.
"""

numeros = [1, 5, 8, 3, 30, 9, 13]

print("Números impares mayores a 3:")
for numero in numeros:
    if numero > 3 and numero % 2 != 0:
        print(numero)