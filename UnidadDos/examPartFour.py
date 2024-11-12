# Parte Cuatro

class MaquinaRefrescos:
    def __init__(self):

        self.refrescos = {
            "coca-cola": 15,
            "fanta": 13,
            "sprite": 14,
            "pepsi": 15,
            "jarrito": 13
        }
    
        self.vendidos = {nombre: 0 for nombre in self.refrescos}
        self.cobrado = {nombre: 0 for nombre in self.refrescos}
        self.cambios = []

    def comprar_refresco(self, nombre, cantidad_pagada):
        if nombre in self.refrescos:
            precio = self.refrescos[nombre]
            if cantidad_pagada >= precio:
                cambio = cantidad_pagada - precio
                cambio_monedas = self.calcular_cambio(cambio)
                self.cambios.append(cambio_monedas)

                self.vendidos[nombre] += 1
                self.cobrado[nombre] += precio
                print(f"Compra exitosa. Cambio devuelto: ${cambio} en monedas {cambio_monedas}")
            else:
                print("Monto insuficiente.")
        else:
            print("Refresco no disponible.")

    def calcular_cambio(self, cambio):
        monedas = {"$10": 0, "$5": 0, "$1": 0}
        monedas["$10"], cambio = divmod(cambio, 10)
        monedas["$5"], cambio = divmod(cambio, 5)
        monedas["$1"] = cambio
        return monedas

    def mostrar_resultados(self):
        print("\n--- Reporte de Ventas ---")
        for nombre in self.refrescos:
            print(f"{nombre.capitalize()}: Vendidos {self.vendidos[nombre]}, Total cobrado ${self.cobrado[nombre]}")
        
        print("\n--- Cambios devueltos ---")
        for i, cambio in enumerate(self.cambios, start=1):
            print(f"Compra {i}: Cambio en monedas {cambio}")

def main():
    maquina = MaquinaRefrescos()

    while True:
        nombre = input("Introduce el nombre del refresco que deseas comprar (o '*' para finalizar): ").lower()
        if nombre == '*':
            break

        cantidad_pagada = int(input("Introduce la cantidad pagada: "))
        maquina.comprar_refresco(nombre, cantidad_pagada)

    # Mostrar el reporte final
    maquina.mostrar_resultados()

main()
