'''Tablas de multiplicar'''

class Multiplicacion:
    def __init__(self):
        self.r = 0
        self.n = 0

    def calcular(self):
        if self.r == 1:
            for i in range(1, 11):
                resul = self.n * i
                print(f'{self.n} x {i} = {resul}')
        elif self.r == 0:
            print('Adiós :)')

x = Multiplicacion()
x.r = int(input('Para comenzar/continuar presiona 1, para salir 0: '))
x.n = int(input('Dame un número: '))
x.calcular()
