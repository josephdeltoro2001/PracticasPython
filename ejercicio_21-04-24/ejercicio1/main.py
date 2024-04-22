def calcular_nivel_y_dinero(salario, puntuacion):
    #Determinar el nivel de rendimiento
    if puntuacion >= 0 and puntuacion <= 3:
        nivel = "Inaceptable"

    elif puntuacion >= 4 and puntuacion <= 6:
        nivel = "Aceptable"

    elif puntuacion >= 7 and puntuacion <= 10:
        nivel = "Meritorio"

    else:
        return "Puntuación inválida. Debe estar entre 0 y 10."

    #Calcular la cantidad de dinero recibida
    dinero = salario * (puntuacion / 10)

    return nivel, dinero

#Se obtienen los datos del usuario
salario = float(input("Ingrese su salario mensual: "))
puntuacion = int(input("Ingrese su puntuación en la evaluación: "))

#Calcular nivel y dinero recibido
nivel, dinero_recibido = calcular_nivel_y_dinero(salario, puntuacion)

#Imprimir resultados
print("Cantidad de dinero recibido: ${:.2f}".format(dinero_recibido))
print(f"Nivel de rendimiento: {nivel}")