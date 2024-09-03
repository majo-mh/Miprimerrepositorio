class Rectangulo:
 """
 Define un rectángulo según su base y su altura.
 """
 def __init__(self, b, h):
    self.b = b
    self.h = h
 def area(self):
    return self.b * self.h
ba=float(input('Escribe la base: '))
ha=float(input('Escribe la altura: '))
rectangulo = Rectangulo(ba, ha)
print("Área del rectángulo que tiene una base de :", ba, ' y con altura de ', ha, ' es ', rectangulo.area())

