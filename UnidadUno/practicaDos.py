'''
->Datos protegidos(autorisacion), publico (cualquiera) y privado (___) 
->Funciones amigas
'''

class saludo:
    def __init__(self, saluda):
        self.h = saluda

s=saludo('hola mundo')
print (s.h)