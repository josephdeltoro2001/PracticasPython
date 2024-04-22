def calcular_capital(cantidad, interes_anual, años):
    capital = cantidad
    for i in range(1, años + 1):
        capital += capital * (interes_anual / 100)
        print("Capital tras {} año(s): ${:.2f}".format(i, capital))

#Solicitud de datos al usuario
cantidad = float(input("¿Cantidad a invertir?: "))
interes_anual = float(input("¿Interés porcentual anual?: "))
años = int(input("¿Años?: "))

#Se caLcula y se muestra el capital obtenido cada año
calcular_capital(cantidad, interes_anual, años)
