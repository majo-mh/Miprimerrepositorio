"""
Dada las siguientes notas almacenadas en un arreglo: [20, 15, 12, 11, 8, 4, 1]
solicitar al usuario en número a buscar, indicar si el numero existe y e que
posición se encuentra
"""

notas = [20, 15, 12, 11, 8, 4, 1]

resp = int(input('Ingrese el numero que desea buscar: '))

try:
    indice = notas.index (resp)
    print (f'La posicion {resp} es: {indice+1}')
except ValueError:
    print (f'No exciste {resp} en la lista')