class Alumno:
    def __init__(self, nombre):
        self.nombre = nombre
        self.calificaciones = []

    def agregar_calificacion(self, calificacion):
        self.calificaciones.append(calificacion)

class Clase:
    def __init__(self):
        self.alumnos = []

    def agregar_alumno(self, alumno):
        self.alumnos.append(alumno)

    def mostrar_alumnos(self):
        for alumno in self.alumnos:
            print(f"Alumno: {alumno.nombre}")
            print(f"Calificaciones: {alumno.calificaciones}")

mi_clase = Clase()

for i in range(5):
    nombre = input(f"Ingrese el nombre del alumno {i+1}: ")
    alumno = Alumno(nombre)
    
    for j in range(3):
        calificacion = float(input(f"Ingrese la calificación {j+1} de {nombre}: "))
        alumno.agregar_calificacion(calificacion)
    
    mi_clase.agregar_alumno(alumno)

mi_clase.mostrar_alumnos()

        
