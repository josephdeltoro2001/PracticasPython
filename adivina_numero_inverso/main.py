import random

print("Piensa en un número entre 1 y 50, yo intentaré adivinarlo.")
input("Presiona Enter cuando estés listo para comenzar...")
print("¡Genial! Empecemos.")

limite_inferior = 1
limite_superior = 50
intentos = 0

while True:
    intento = random.randint(limite_inferior, limite_superior)
    print("¿Es {} tu número?".format(intento))
    respuesta = input("Ingresa 'menor', 'mayor' si tu número es menor o mayor, o 'correcto' si logré adivinar: ").lower()

    if respuesta == "correcto":
        print("¡Adiviné tu número en {} intentos!".format(intentos))
        break

    elif respuesta == "menor":
        limite_superior = intento - 1

    elif respuesta == "mayor":
        limite_inferior = intento + 1
        
    else:
        print("Por favor, ingresa 'menor', 'mayor' o 'correcto'.")

    intentos += 1