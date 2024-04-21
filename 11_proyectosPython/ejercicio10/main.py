def cortadora_correo_electronico(correo):
    nombre_usuario, dominio = correo.split('@')

    dominios_populares = ['gmail.com', 'yahoo.com', 'hotmail.com', 'outlook.com']
    if dominio in dominios_populares:
        mensaje = f"Hey {nombre_usuario.title()}, veo que tu correo está registrado con {dominio}. ¡Eso es genial!"
    else:
        mensaje = f"Hey {nombre_usuario.title()}, parece que tienes tu propio dominio personalizado en {dominio}. ¡Impresionante!"
    return mensaje

correo = input("Por favor, ingresa tu dirección de correo electrónico: ")
mensaje = cortadora_correo_electronico(correo)
print(mensaje)