"""
Escribir un programa que pida numeros positivos al usuario. Mostrar el numero cuya sumatoria de digitos fue mayor a la cantidad 
de numeros cuya sumatoria de digitos fue menor que 10. Utilizar una o mas funciones, Segun sea necesario
"""

class Numeros:
    def __init__(self):
        pass
    
    def sumar_digitos(self, numero):
        suma = 0
        while numero > 0:
            suma += numero % 10  
            numero //= 10 
        return suma

numeros = Numeros()

mayor_suma_digitos = 0
numero_mayor_suma = 0
cantidad_suma_menor_que_10 = 0

while True:
    numero = int(input("Ingresa un número positivo (0 para salir): "))
    if numero == 0:
        break
    
    suma_digitos = numeros.sumar_digitos(numero)
    
    if suma_digitos > mayor_suma_digitos:
        mayor_suma_digitos = suma_digitos
        numero_mayor_suma = numero
    
    if suma_digitos < 10:
        cantidad_suma_menor_que_10 += 1

print(f"El número cuya suma de dígitos fue mayor es: {numero_mayor_suma} con una suma de {mayor_suma_digitos} dígitos.")
print(f"La cantidad de números cuya suma de dígitos fue menor que 10 es: {cantidad_suma_menor_que_10}.")




