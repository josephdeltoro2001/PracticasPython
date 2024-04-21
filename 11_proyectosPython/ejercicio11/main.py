canciones = {

    "Bohemian Rhapsody": "Mama, just killed a man \nPut a gun against his head \nPulled my trigger, now he's dead Mama, life had just begun \nBut now I've gone and thrown it all away",
    "Radio Ga Ga": "All we hear is radio ga ga \nRadio goo goo Radio ga ga \nAll we hear is radio ga ga \nRadio blah blah",
    "I Want To Break Free": "I want to break free \nI want to break free \nI want to break free from your lies \nYou're so self satisfied, I don't need you \nI've got to break free \nGod knows, God knows I want to break free",
    "Crazy Little Thing Called Love": "This thing called love \nI just can't handle it \nThis thing called love \nI must get round to it \nI ain't ready \nCrazy little thing called love",
    "Love Of My Life": "Love of my life, you've hurt me \nYou've broken my heart \nAnd now you leave me",
    "Don't Stop Me Now": "Don't stop me now \nI'm having such a good time \nI'm having a ball \nDon't stop me now \nIf you wanna have a good time, just give me a call \nDon't stop me now ('cause I'm havin' a good time) \nDon't stop me now (yes, I'm havin' a good time) \nI don't wanna stop at all",
    "We Will Rock You": "Singing \nWe will, we will rock you \nWe will, we will rock you",
    "We Are The Champions": "We are the champions, my friends \nAnd we'll keep on fighting till the end \nWe are the champions \nWe are the champions \nNo time for losers \n'Cause we are the champions of the world",
    "Another One Bites The Dust": "Another one bites the dust \nAnother one bites the dust \nAnd another one gone, and another one gone \nAnother one bites the dust \nHey, I'm gonna get you too \nAnother one bites the dust",
    "The Show Must Go On": "The show must go on, yeah \nThe show must go on \nI'll face it with a grin \nI'm never giving in \nOn with the show",
}

def generador_letras():
    print("Seleccione una canción de este top:\n")

    # Mostrar las opciones de canciones al usuario
    for i, cancion in enumerate(canciones.keys(), 1):
        print(f"{i}. {cancion}")

    while True:
        # Solicitar al usuario que seleccione una canción
        seleccion = input("\nIngrese el número de la canción que le gustaría ver la letra: ")

        if seleccion == "*":
            continue  # Si el usuario quiere seleccionar otra canción, vuelve al inicio del bucle
        elif seleccion.isdigit() and 1 <= int(seleccion) <= len(canciones):
            # Obtener la canción seleccionada por el usuario
            cancion_seleccionada = list(canciones.keys())[int(seleccion) - 1]
            print(f"\n------- {cancion_seleccionada} ------------")
            print(canciones[cancion_seleccionada])
            break
        else:
            print("Entrada inválida. Por favor ingrese un número entre 1 y", len(canciones))

generador_letras()