#Desarrollar un sistema casa de cambio en el cual se incerta un billete o se le indica una cantidad a cambiar el sistema devuelve 
#la cantidad en monedas de $10, $5 y $1. No se puede devolver todo de una sola moneda tiene que regresar al menos una de cada denominacion 
#Ejemplo:Le damos $100 y devuelve 4 de $10, 1 de $5 y 5 de $1

#Algoritmo---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

'''
1.-Inicialización: Se define una clase con atributos para la cantidad y las monedas.
2.-Verificación: Se verifica que la cantidad sea mayor o igual a 16.
3.-Cambio básico: Se asegura que se den al menos una moneda de $10, una de $5 y una de $1.
4-Distribución restante: Se distribuyen el resto de las monedas usando ciclos.
5.-Resultado: El método muestra cuántas monedas de cada tipo se entregan.
'''
#Codigo------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

class CasaDeCambio:
    def __init__(self, cantidad):
        self.cantidad = cantidad
        self.monedas_10 = 0
        self.monedas_5 = 0
        self.monedas_1 = 0
    
    def realizar_cambio(self):
        if self.cantidad < 16:
            return "No se puede hacer el cambio, la cantidad debe ser mayor o igual a 16."
        
        self.monedas_10 += 1
        self.cantidad -= 10
        
        self.monedas_5 += 1
        self.cantidad -= 5
        
        self.monedas_1 += 1
        self.cantidad -= 1
        
        while self.cantidad > 0:
            if self.cantidad >= 10:
                self.monedas_10 += 1
                self.cantidad -= 10
            elif self.cantidad >= 5:
                self.monedas_5 += 1
                self.cantidad -= 5
            else:
                self.monedas_1 += 1
                self.cantidad -= 1
        
        return self.mostrar_cambio()

    def mostrar_cambio(self):
        return f"El cambio es: {self.monedas_10} monedas de $10, {self.monedas_5} monedas de $5, {self.monedas_1} monedas de $1."


cantidad_a_cambiar = int(input("Ingresa la cantidad a cambiar: "))
casa_cambio = CasaDeCambio(cantidad_a_cambiar)
resultado = casa_cambio.realizar_cambio()
print(resultado)
