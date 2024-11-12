class Arreglo:
    def __init__(self):
        self.nombre = ''
        self.unidaduno =[80, 90, 78, 40, 87]
        self.unidadesdos = [67, 89, 34, 78, 10]
        self.unidadTres = [56, 100, 56, 78, 90]
        self.nombres = ['carlos', 'maria, rafael', 'lesslie', 'karen']
        self.prom = []

    def promedio (self):
        for i in range (len(self.unidaduno)):
            sum = (self.unidaduno[i] + self.unidadesdos[i] + self.unidadTres[i] ) / 3
            self.prom.append(sum)

    def maximoPromedio (self):
        valormax = max (self.prom)
        indice = self.prom.index(valormax)
        print ('El alumno con el promedio mas alto: ', self.nombres[indice], 'con un promedio de ', valormax)

    def imprimirArreglos (self):
        for i in range (len (self.nombres)):
            print (self.nombres[i], ' ', self.unidaduno[i], ' ', self.unidadesdos[i], ' ', self.unidadTres[i], ' ', self.prom[i])

    def minimoPromedio (self):
        valormin = min (self.prom)
        indice = self.prom.index(valormin)
        print ('El alumno con el promedio mas alto: ', self.nombres[indice], 'con un promedio de ', valormin)

    def pedirNombre (self):
        buscar = input ('Escribe el nombre de a quien quieres buscar: ')
        for i in range (len(self.nombres)):
            if self.nombres[i] == buscar:
                print (self.nombres[i], ' ', self.unidaduno[i], ' ', self.unidadesdos[i], ' ', self.unidadTres[i], ' ', self.prom[i])

    def minCalificacion (self):
        vm = []
        vm.append (min (self.unidaduno ))
        vm.append (min (self.unidaddos))
        vm.append (min (self.unidadTres))

x = Arreglo()
x.promedio()
#x.maximoPromedio()
#x.imprimirArreglos()
x.minimoPromedio()
x.pedirNombre()
x.minCalificacion()
x.minCalificacion()