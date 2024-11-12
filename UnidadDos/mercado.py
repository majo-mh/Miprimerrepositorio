class Mercado:
    def __init__(self):
        self.clave = [1001, 1002, 1003, 1004, 1005]
        self.nombre = ['arroz', 'cereal', 'huevo', 'croquetas', 'pizza']
        self.costo = [19, 50, 30, 250, 197]
        self.existencia = [15, 15, 50, 15, 30]
        self.ventas = [0, 0, 0, 0, 0] 
        self.ganancia = [0.0, 0.0, 0.0, 0.0, 0.0] 

    def buscar(self):
        print("\n--- Búsqueda de Productos ---")
        buscar = input('Ingrese el nombre del producto: ')

        encontrado = False
        for i in range(len(self.nombre)):
            if self.nombre[i] == buscar:
                print(f'Producto: {self.nombre[i]}, Clave: {self.clave[i]}, Costo: {self.costo[i]}, Existencias: {self.existencia[i]}')
                encontrado = True
                break
        if not encontrado:
            print('Producto no encontrado')

    def comprar(self):
        print("\n--- Compra de Productos ---")
        producto_comprar = input('Ingrese el nombre del producto que desea comprar: ')
        
        for i in range(len(self.nombre)):
            if self.nombre[i] == producto_comprar:
                print(f'Producto: {self.nombre[i]}, Costo: {self.costo[i]}, Existencias: {self.existencia[i]}')
                cantidad_comprar = int(input("Ingrese la cantidad que desea comprar: "))
                
                if cantidad_comprar <= self.existencia[i]:
                    self.existencia[i] -= cantidad_comprar  # Reducir existencia
                    total = self.costo[i] * cantidad_comprar
                    total_con_aumento = total * 1.10  # Aumentar el total un 10%
                    
                    # Actualizar las ventas y ganancias
                    self.ventas[i] += cantidad_comprar
                    self.ganancia[i] += total_con_aumento

                    print(f"Total de la compra (con 10% de aumento): {total_con_aumento}")
                    print(f"Nueva existencia de {self.nombre[i]}: {self.existencia[i]}")
                else:
                    print("No hay suficientes existencias.")
                return
        
        print("Producto no encontrado.")

    def ventasGanacias(self):
        print("\n--- Ventas y Ganancias ---")
        for i in range(len(self.nombre)):
            print(f"Producto: {self.nombre[i]}")
            print(f"  Ventas: {self.ventas[i]} unidades")
            print(f"  Ganancias: ${self.ganancia[i]:.2f}\n")

    def maxMin(self):
        print("\n--- Mayor y Menor Existencia ---")
        indice_min = self.existencia.index(min(self.existencia))
        indice_max = self.existencia.index(max(self.existencia))

        print(f"El producto con menor existencia es {self.nombre[indice_min]} con una existencia actual de {self.existencia[indice_min]}")
        print(f"El producto con mayor existencia es {self.nombre[indice_max]} con una existencia actual de {self.existencia[indice_max]}")

def menu():
    mercado = Mercado()
    
    while True:
        print("\n--- Menú ---")
        print("1. Buscar producto")
        print("2. Comprar producto")
        print("3. Ventas y Ganancias")
        print("4. Mayor y menor existencia")
        print("5. Salir")
        
        opcion = input("Elija una opción: ")
        
        if opcion == '1':
            mercado.buscar()
        elif opcion == '2':
            mercado.comprar()
        elif opcion == '3':
            mercado.ventasGanacias()
        elif opcion == '4':
            mercado.maxMin()
        elif opcion == '5':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")

menu()
