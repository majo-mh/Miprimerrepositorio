"""
Crea dos arrays o arreglos unidimensional es que tengan el mismo tamaño (lo
pedirá por teclado), en uno de ellos almacenarás nombres de personas como
cadenas, en el otro array o arreglo ira almacenando la longitud de los nombres.
"""

tamaño = int(input('Ingrese el tamaño: '))

nombres = []
longitud = []

for i in range (tamaño):
    nombre = input(f'Introduce el nombre {i+1}: ')
    nombres.append (nombre)
    longitud.append(len(nombre))

print ('Nombre y su longitud:')
for i in range (tamaño):
    print (f'Nombre: {nombres[i]}, Longuitud: {longitud[i]}')