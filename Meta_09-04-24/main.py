#Capturar datos del usuario
nombre = input("Ingrese su nombre: ")
edad = input("Ingrese su edad: ")
correo = input("Ingrese su correo electrónico: ")

#Imprimir mensaje con colores diferentes
print("\033[1;32mMi nombre es {}\033[0m, \033[1;34mtengo {} años\033[0m y \033[1;35mmi correo electrónico es {}\033[0m.".format(nombre, edad, correo))

#\033[1;32m, \033[1;34m, y \033[1;35m son secuencias de escape que cambian el color de la salida en la consola de Python. \033[0m se usa para restablecer el color a su valor predeterminado.