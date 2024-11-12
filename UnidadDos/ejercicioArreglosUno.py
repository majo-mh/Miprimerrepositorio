"""
Crea un array o arreglo unidimensional donde le indiques el tamaño por teclado
y crear una función que rellene el array o arreglo con los múltiplos de un
número pedido por teclado. Por ejemplo, si defino un array de tamaño 5 y elijo
un 3 en la función, el array contendrá 3, 6, 9, 12, 15. Muestralos por pantalla
usando otra función distinta.
"""

tamaño = int(input("Introduce el tamaño del arreglo: "))
multiplo = int(input("Introduce el número para obtener sus múltiplos: "))

arreglo = []
for i in range(1, tamaño + 1):
    arreglo.append(i * multiplo)

print("El arreglo contiene los siguientes elementos:")

for elemento in arreglo:
    print(elemento)
