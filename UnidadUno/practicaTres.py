class Alumno:
   def __init__(self, nombre):
    self.nom = nombre
   def saludar(self):
     print (f'¡Hola, {self.nom}!')
n=input('Escribe tu nombre: ')
x = Alumno (n) 
x.saludar ()


