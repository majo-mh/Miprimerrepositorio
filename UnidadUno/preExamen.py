'''
El sistema es para la cocecha de manzanas a cada trabajador se le paga por caja de manzanas cocechadas, las primeras 10 cajas se le ppaga a $50 cada caja 
mas de 50 y menos de 80 cajas más se le paga 50% mas, mas de 80 se les paga el doble del subtotal de pago se le descuenta el 5% para caja de ahorro 

generar un sistema que pida el nombre del trabajador y la cantidad de cajas cocechadas ese dia, asi como el pago que obtiene indicando la cantidad pagadade acuerdo
de cajas cocechadas asi como el descuento que se hace por su pago

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''

class Sistema:
    def __init__(self):
        self.nombre = ''
        self.cajas_cocechadas = 0
        self.pago_por_caja = 50
        self.subtotal = 0
        self.descuento = 0
        self.total_pago = 0
         
    def calcular_pago(self):
        if self.cajas_cocechadas <= 10:
            self.subtotal = self.cajas_cocechadas * self.pago_por_caja
        elif 10 < self.cajas_cocechadas <= 50:
            self.subtotal = self.cajas_cocechadas * self.pago_por_caja
        elif 50 < self.cajas_cocechadas <= 80:
            self.subtotal = (50 * self.pago_por_caja) + ((self.cajas_cocechadas - 50) * self.pago_por_caja * 1.5)
        else:
            self.subtotal = (50 * self.pago_por_caja) + (30 * self.pago_por_caja * 1.5) + \
                            ((self.cajas_cocechadas - 80) * self.pago_por_caja * 2)

        self.descuento = self.subtotal * 0.05
        self.total_pago = self.subtotal - self.descuento

        print(f'A {self.nombre} se le debe pagar ${self.total_pago:.2f}, con un descuento de ${self.descuento:.2f} para caja de ahorro.')

x = Sistema()
x.nombre = input('Ingrese el nombre del trabajador: ')
x.cajas_cocechadas = int(input('Ingrese el número de cajas cosechadas: '))
x.calcular_pago()
