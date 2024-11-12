"""
Dada las siguientes notas almacenadas en un arreglo: [20, 15, 12, 11, 8, 4, 1]
Elimine la nota más baja programáticamente sin usar la función (min) y escriba
en pantalla. Luego programáticamente calcule el promedio de
notas descontando la nota eliminada.
"""

notas = [20, 15, 12, 11, 8, 4, 1]

nota_mas_baja = notas[0]

for nota in notas:
    if nota < nota_mas_baja:
        nota_mas_baja = nota

print(f"La nota más baja eliminada es: {nota_mas_baja}")

promedio = sum(notas) / len(notas)

print(f"El promedio de las notas restantes es: {promedio:.2f}")