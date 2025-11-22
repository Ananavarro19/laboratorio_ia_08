def calcular_promedio(notas):
    suma = 0
    for n in notas:
        suma = suma + n
    promedio = suma / len(notas)
    return promedio

notas = [3.5, 4.0, 2.8, 3.9]
print(calcular_promedio(notas))
