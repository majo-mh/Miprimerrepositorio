alumnos = ['juan', 'pedro', 'luis', 10] 
"""
print (alumnos)

print (alumnos[0])
print (alumnos[1])
print (alumnos[2])
print (alumnos[-1])
print (alumnos[-3])
print (alumnos[-2])
print (alumnos[-1])

print ('---------recorriendo elementos-----------')
for alum in alumnos: #Recorriendo elementos 
    print (alum)

print ('------------recorriendo indices-----------')
for i in range (len(alumnos)): #recorriendo los indices
    print (alumnos[i])

print ('recorriendo con while y los indices')
indice = 0
while indice < len(alumnos):
    print (alumnos[indice])
    indice += 1 #Incrementa uno

print ('........Agregar valores al arreglo......')
numeros = []
numeros.append (4)
numeros.append (1)
numeros.append (5)
numeros.append (6)
print (numeros)

print ('..............Quitar valores...........')
numeros.pop (1)
print (numeros)

print('....Quitar valores con remove......')
alumnos.remove('juan')
print (alumnos)


print ('.........Buscar con for.............. ')

for i in  range (len(alumnos)):
    if alumnos[i] == 'luis':
        print ('Si existe luis en la lista su posicion es', i+1) 

print ('.........Buscar con una funcion...........')
if 'luis' in alumnos:
    print ('Si existe luis en la lista')
else:
    print ('No existe luis en la lista')

print ('......Buscar la posicion')
indice = alumnos.index ('luis')
print ('La posicion de luis es: ', indice+1)

print ('......Buscar la posicion try...............')
try:
    indice = alumnos.index ('miguel')
    print ('La posicion demiguel es: ', indice+1)
except ValueError:
    print ('No exciste loslis en la lista ')

"""