'''
------Instrucciones del ejercicio

Se pide 3 calificaciones (0 - 100) asi como el nombre del alumno se promedia los alumnos que tengan calificacionesmenor a 70 mande un mensaje de reprobado, al 
finalizar el sistema imprime el nombre y promedio del alumno con con mayor calificacion y el alumno con menor calificación.

------Algoritmo

1.-Crear una lista para guardar los nombres datos de los alumnos y sus repectivos promedios 
2.-Usar un bucle para asi añadir tantos alumnos sean necesarios 
3.-Pedir los datos requeridos como nombre del alumno y sus respectivas 3 calificaciones 
4.-Realisar el promedio de las 3 calificaciónes
5.-Acomodar la lista de mayor a menor promedio 
6.-Si la calificacion es menor de 70 se mandara el mensaje de reprobado y si no sera de aprobado 
7.-Se mostrara de mayor a menor calificacion promediada, mostrando su nombre, promedio y si reprobo o no

-----Codigo
'''

alumnos = []

while True:
    nombre = input("Ingrese el nombre del alumno (o 'salir' para terminar): ")
    if nombre.lower() == 'salir':
        break
    
    calificaciones = [float(input(f"Calificación {i+1}: ")) for i in range(3)]
    promedio = sum(calificaciones) / 3
    
    alumnos.append((nombre, promedio))

alumnos.sort(key=lambda x: x[1], reverse=True)

for nombre, promedio in alumnos:
    estado = "Reprobado" if promedio < 70 else "Aprobado"
    print(f"{nombre}: {promedio:.2f} - {estado}")









