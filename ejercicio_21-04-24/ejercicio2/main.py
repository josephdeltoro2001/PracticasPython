def convertir_monedas(cantidad):
    #Definimos las denominaciones de monedas y sus cantidades
    denominaciones = [20, 10, 5, 1]
    cantidades = [0, 0, 0, 0]

    #Iteramos sobre las denominaciones de monedas
    for i, valor_moneda in enumerate(denominaciones):
        # Calculamos la cantidad de monedas de esta denominación
        cantidades[i] = cantidad // valor_moneda
        # Actualizamos la cantidad para la próxima iteración
        cantidad %= valor_moneda

    return cantidades

#Solicitamos al usuario la cantidad a convertir
cantidad = int(input("Cantidad a convertir: "))

#Se obtienen las cantidades de monedas
cantidades_monedas = convertir_monedas(cantidad)

#Se imprime el resultado
print("Cantidad de monedas")
for i, valor in enumerate([20, 10, 5, 1]):
    print("Monedas de ${}: {}".format(valor, cantidades_monedas[i]))
