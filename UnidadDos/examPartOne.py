#Parte numero uno 

import random

class NumerosAleatorios:
    def __init__(self, cantidad, min_val, max_val):
        self.numeros = [random.randint(min_val, max_val) for _ in range(cantidad)]
    
    def obtener_numeros(self):
        return self.numeros

class VerificadorPrimos:
    def __init__(self, numeros):
        self.numeros = numeros
        self.resultados = [1 if self.es_primo(num) else 0 for num in numeros]
    
    def es_primo(self, num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True
    
    def obtener_resultados(self):
        return self.resultados

numeros_aleatorios = NumerosAleatorios(10, 100, 1000)
numeros = numeros_aleatorios.obtener_numeros()

verificador = VerificadorPrimos(numeros)
resultados_primos = verificador.obtener_resultados()

print("Números aleatorios:", numeros)
print("Resultados (1 si es primo, 0 si no lo es):", resultados_primos)
