"""
Solicitar numeros al usuario hasta que ingrese el cero. Por cada uno, mostrarla suma de sus digitos. Al finalizar, mostrar la sumatoria de todos los numeros ingresados 
y la suma de sus diguitos. Reutilizar la misma funcion realizada en el ejercicio 1 

"""

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

sumatoria_numeros = 0
sumatoria_digitos = 0

while True:
    numero = int(input("Ingresa un número (0 para salir): "))
    if numero == 0:
        break
    
    suma_digitos = calculadora.sumar_digitos(numero)
    
    print(f"La suma de los dígitos de {numero} es {suma_digitos}")
    
    sumatoria_numeros += numero
    sumatoria_digitos += suma_digitos

print(f"La sumatoria de todos los números ingresados es: {sumatoria_numeros}")
print(f"La suma de los dígitos de todos los números ingresados es: {sumatoria_digitos}")





