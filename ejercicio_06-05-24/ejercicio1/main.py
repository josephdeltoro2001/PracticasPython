#Se solicita al usuario la altura del triángulo
altura = int(input("Ingrese la altura: "))  

#Iterar sobre cada fila del triángulo hasta la altura especificada
for i in range(1, altura + 1):
    # Imprimir '*' i veces en cada fila
    print("*" * i)