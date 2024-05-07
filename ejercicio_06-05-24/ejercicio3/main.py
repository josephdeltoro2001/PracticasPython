#Se le solicita una palabra al usuario
palabra = input("Ingrese una palabra: ")

#Reverso de la palabra ingresada
reverso_palabra = palabra[::-1]

#Verificar si la palabra ingresada es un palíndromo
if palabra == reverso_palabra:
    print("La palabra si es un palíndromo")
else:
    print("La palabra no es un palíndromo")