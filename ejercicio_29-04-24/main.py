import random

def mezclar_lista(lista):
    #Se crea una lista vacía para almacenar los elementos mezclados
    lista_mezclada = []

    #Mientras la lista original no se encuentre vacía se entra a este ciclo
    while lista:
        #Se selecciona un índice aleatorio dentro del rango de la lista
        indice = random.randint(0, len(lista) - 1)
        #Se añade el elemento en el índice seleccionado a la lista mezclada
        lista_mezclada.append(lista.pop(indice))

    return lista_mezclada

#Se imprime la lista original y la mezclada
numeros = [1, 2, 3, 4]
print(f"Lista original: {numeros}")

numeros_revueltos = mezclar_lista(numeros)
print(f"Lista mezclada: {numeros_revueltos}")
