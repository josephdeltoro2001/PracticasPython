while True:
        try:
            numero = int(input("Introduce un número entre 1 y 1000: "))
            
            if 1 <= numero <= 1000:
                if numero % 2 == 0:
                    print(f"El número {numero} es par")

                else:
                    print(f"Es número {numero} es impar")

                respuesta = input("¿Deseas probar con otro número? (Sí/No): ")
                if respuesta.lower() != 'si':
                    break
            else:
                print("Por favor, introduce un número válido entre 1 y 1000.")
                
        except ValueError:
            print("Por favor, introduce un número entero válido.")
