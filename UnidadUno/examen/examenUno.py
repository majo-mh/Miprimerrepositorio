#Solicitar numeros al usuario hasta que ingrese el cero. Por cada uno, mostrarla suma de sus digitos (utilizando una funcion que realice dicha suma) 

class SumaDigitos:
    def __init__(self):
        pass
    
    def sumar_digitos(self, numero):
        suma = 0
        while numero > 0:
            suma += numero % 10  
            numero //= 10  
        return suma

calculadora = SumaDigitos()

while True:
    numero = int(input("Ingresa un número (0 para salir): "))
    if numero == 0:
        break
    print(f"La suma de los dígitos de {numero} es {calculadora.sumar_digitos(numero)}")

