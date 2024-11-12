#Parte tres

class EmpresaTransporte:
    def __init__(self):
        self.nombres = []
        self.kms = []
    
    def agregar_conductor(self, nombre, kms_semanales):
        self.nombres.append(nombre)
        self.kms.append(kms_semanales)

    def calcular_total_kms(self):
        
        return [sum(kms) for kms in self.kms]

    def mostrar_conductores(self):
        print("\nLista de conductores y kilómetros recorridos:")
        total_kms = self.calcular_total_kms()
        for nombre, kms, total in zip(self.nombres, self.kms, total_kms):
            print(f"Conductor: {nombre}, Kilómetros por día: {kms}, Total kilómetros: {total}")

def main():
    empresa = EmpresaTransporte()

    while True:
        nombre = input("Introduce el nombre del conductor (o '*' para finalizar): ")
        if nombre == '*':
            break

        kms_semanales = []
        for dia in ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]:
            km = float(input(f"Introduce los kilómetros recorridos el {dia} por {nombre}: "))
            kms_semanales.append(km)

        empresa.agregar_conductor(nombre, kms_semanales)

    empresa.mostrar_conductores()

main()
