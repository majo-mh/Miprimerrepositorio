'''menu de 5 opcion con la ultima de salir'''
class Opciones:
    def __init__(self):
        self.r = 0  

    def ciclo(self):
        while self.r != 5:
            self.r = int(input('''Dime qué opción quieres:
1)...
2)...
3)...
4)...
5)Salir 
'''))
            if self.r == 1:
                print('Presionaste la opción 1')
            elif self.r == 2:
                print('Presionaste la opción 2')
            elif self.r == 3:
                print('Presionaste la opción 3')
            elif self.r == 4:
                print('Presionaste la opción 4')
            elif self.r == 5:
                print('Adiós :)')

x = Opciones()
x.ciclo()  


