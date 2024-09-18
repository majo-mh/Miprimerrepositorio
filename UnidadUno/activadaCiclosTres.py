'''pide tu nombre'''

class Nombre:
    def __init__(self):
        self.n = ''
        self.r = 1  # Inicializa r con 1 para entrar al bucle la primera vez
    
    def pedirNombre(self):
        while self.r == 1:
            self.r = int(input('Presiona 1 para empezar o continuar y 0 para salir: '))
            if self.r == 1:
                self.n = input('Ingresa tu nombre: ')
                print(f'Hola {self.n}')
            else:
                print('Adiós.')

x = Nombre()
x.pedirNombre()
