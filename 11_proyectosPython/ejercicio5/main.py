def obtener_acronimo(frase):
    acronimo = ''.join(word[0].upper() for word in frase.split())
    return acronimo

frase_completa = input("Ingresa el significado completo de un concepto: ")
acronimo = obtener_acronimo(frase_completa)
print("El acrónimo para", frase_completa, "es:", acronimo)