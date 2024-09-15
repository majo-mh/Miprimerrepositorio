class Datos:
    def __init__(self):
        self.n = ""
        self.c1 = 0
        self.c2 = 0
        self.c3 = 0

class Promedio(Datos):
    def promedio(self):
        return (self.c1 + self.c2 + self.c3) / 3

class Comparacion(Promedio):
    def comparacion(self):
        promedio = self.promedio()
        if promedio >= 70:
            return 'APROBADO'
        else:
            return 'REPROBADO'

class Imprimir(Comparacion):
    def imprimir(self):
        print(f"El alumno {self.n} con calificaciones {self.c1}, {self.c2}, {self.c3} tiene un promedio de {self.promedio():.2f} y está {self.comparacion()}.")

x = Imprimir()

x.n = input('Ingrese el nombre del alumno: ')
x.c1 = int(input('Ingrese la primera calificación: '))
x.c2 = int(input('Ingrese la segunda calificación: '))
x.c3 = int(input('Ingrese la tercera calificación: '))

x.imprimir()
