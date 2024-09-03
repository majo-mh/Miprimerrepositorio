class Poligono:
 """
 Define un polígono según su base y su altura.
 """
 def __init__(self, b, h):
    self.b = b
    self.h = h

class Rectangulo(Poligono):
 def area(self):
    return self.b * self.h
 
class Triangulo(Poligono):
 def area(self):
    return (self.b * self.h) / 2
 
ba = float (input('Escribe la base del recatangulo: '))
ha = float(input('Escribe la altura del rectangulo: '))
rectangulo = Rectangulo(ba, ha)

ba = float (input('Escribe la base del triangulo: '))
ha = float(input('Escribe la altura del triangulo: '))
triangulo = Triangulo(ba, ha)

resp=input('De que forma decea sacar el area? A->')

print("Área del rectángulo:", rectangulo.area())
print("Área del triángulo:", triangulo.area())