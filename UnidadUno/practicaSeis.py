'''
Se piden 3 calificaciones asi como el nobre del alumno
Se promedian las tres calificaciones si el promedio es mayor que 70 se escribe aprobado si es menor se indica que reprobo

Clases: Constructor, promedio, comparacion, pedir datos 
'''

class Datos():
    def __init__(self):
        self.n = ""
        self.c1 = 0
        self.c2 = 0
        self.c3 = 0
    def promedio(self):
        r = (self.c1 + self.c2 + self.c3)/3
        return r
    def comparacion(self, num):
        if num > 70:
            rs = 'aprobado'
        else:
            rs = 'reprobado'
        return rs

x=Datos() #Encapsulamiento
x.n = str(input('Ingrese el nombre del alumno: '))
x.c1 = int(input('Ingrese la primera calificacion: '))
x.c2 = int(input('Ingrese la segunda calificacion: '))
x.c3 = int(input('Ingrese la tercera calificacion: '))
#x.comparacion(x.promedio())
p = x.promedio 
c = x.comparacion(p)
print (x.n, ' con calificaciones ', x.c1, ', ', x.c2 ', ', x.3, ' su promedio es de ', p, ' esta ', c)
