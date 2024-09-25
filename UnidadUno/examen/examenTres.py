"""
Requeriri al usuiario que ingrese un numero entero e informar si es primo o no, utilizando la funcion booleana que lo decida
"""

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

verificador = NumeroPrimo()

numero = int(input("Ingresa un número entero: "))

if verificador.es_primo(numero):
    print(f"El número {numero} es primo.")
else:
    print(f"El número {numero} no es primo.")








