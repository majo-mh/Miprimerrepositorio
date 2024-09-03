class Alumno:
   def __init__(self):
    self.nombre = "Pablo"
   def saludar(self):
     print (f"¡Hola, {self.nombre}!")

x = Alumno () #Parentecis es para el encapsulado
x.saludar ()
print (x.nombre) #Esta dentro del encapsulado

