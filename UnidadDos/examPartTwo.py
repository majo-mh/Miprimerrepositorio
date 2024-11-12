# Parte numero Dos 

class Curso:
    def __init__(self):
        self.nombres = []
        self.edades = []

    def agregar_alumno(self, nombre, edad):
        self.nombres.append(nombre)
        self.edades.append(edad)

    def mostrar_alumnos(self):
        print("\nLista completa de alumnos:")
        for nombre, edad in zip(self.nombres, self.edades):
            print(f"Nombre: {nombre}, Edad: {edad}")

    def mostrar_mayores_de_edad(self):
        print("\nAlumnos mayores de edad:")
        for nombre, edad in zip(self.nombres, self.edades):
            if edad >= 18:
                print(f"Nombre: {nombre}, Edad: {edad}")

    def mostrar_dos_mayores(self):
        print("\nLos dos alumnos de mayor edad:")
        if len(self.edades) >= 2:
            # Encontrar los índices de las dos edades más altas
            edades_ordenadas = sorted(zip(self.edades, self.nombres), reverse=True)
            for edad, nombre in edades_ordenadas[:2]:
                print(f"Nombre: {nombre}, Edad: {edad}")
        else:
            print("No hay suficientes alumnos para mostrar los dos mayores.")

def main():
    curso = Curso()

    while True:
        nombre = input("Introduce el nombre del alumno (o '*' para finalizar): ")
        if nombre == '*':
            break
        edad = int(input(f"Introduce la edad de {nombre}: "))
        curso.agregar_alumno(nombre, edad)

    curso.mostrar_alumnos()
    curso.mostrar_mayores_de_edad()
    curso.mostrar_dos_mayores()

main()
