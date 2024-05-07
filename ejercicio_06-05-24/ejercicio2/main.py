#Se le solicita un número al usuario
numero = int(input("Ingrese un número: "))

#Este ciclo itera desde 1 hasta el numero ingresado por el usuario en pasos de 2
for i in range(1, numero + 1, 2):
    #Este ciclo itera desde i hasta 0 en pasos de -2
    for j in range(i, 0, -2):
        #Los números se imprimen en la misma línea
        print(j, end=" ")
    #Salto a la siguiente línea
    print()