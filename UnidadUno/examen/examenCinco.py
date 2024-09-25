"""
Generar un menu de opciones donde 5 es salir y cada una de las 4 opciones sea el ejercicio soliciotado con anterioridad
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

class NumeroPrimo:
    def __init__(self):
        pass
    
    def es_primo(self, numero):
        if numero <= 1:
            return False
        for i in range(2, int(numero ** 0.5) + 1):
            if numero % i == 0:
                return False
        return True

def ejercicio_1():
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

def ejercicio_2():
    verificador = NumeroPrimo()
    numero = int(input("Ingresa un número entero: "))

    if verificador.es_primo(numero):
        print(f"El número {numero} es primo.")
    else:
        print(f"El número {numero} no es primo.")

def ejercicio_3():
    numeros = SumaDigitos()
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

def mostrar_menu():
    print("\nMenú de opciones:")
    print("1. Sumar dígitos de los números ingresados y mostrar sumatoria")
    print("2. Verificar si un número es primo")
    print("3. Mostrar el número con mayor suma de dígitos y cantidad de sumas menores que 10")
    print("4. Opción adicional (ejercicio 1 sin sumatoria)")
    print("5. Salir")

def ejecutar_menu():
    while True:
        mostrar_menu()
        opcion = int(input("Elige una opción: "))

        if opcion == 1:
            ejercicio_1()
        elif opcion == 2:
            ejercicio_2()
        elif opcion == 3:
            ejercicio_3()
        elif opcion == 4:
            ejercicio_1()
        elif opcion == 5:
            print("Adios")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

ejecutar_menu()
