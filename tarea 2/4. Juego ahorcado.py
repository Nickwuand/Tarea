import random

def obtener_palabra():
    palabras = ["python", "programacion", "computadora", "desarrollo", "inteligencia", "openai", "algoritmo", "aprendizaje", "datos", "tecnologia"]
    return random.choice(palabras)

def mostrar_tablero(palabra_oculta, letras_adivinadas):
    for letra in palabra_oculta:
        if letra in letras_adivinadas:
            print(letra, end=" ")
        else:
            print("_", end=" ")
    print()

def jugar_ahorcado():
    palabra_oculta = obtener_palabra()
    letras_adivinadas = []
    intentos_restantes = 6

    print("¡Bienvenido al Juego del Ahorcado!")
    print("Adivina la palabra. Tienes 6 intentos.")

    while intentos_restantes > 0:
        mostrar_tablero(palabra_oculta, letras_adivinadas)
        letra = input("Ingresa una letra: ").lower()

        if letra in letras_adivinadas:
            print("Ya has ingresado esa letra. ¡Intenta con otra!")
        elif letra in palabra_oculta:
            letras_adivinadas.append(letra)
            print("¡Bien hecho! Has adivinado una letra.")
        else:
            intentos_restantes -= 1
            print("Letra incorrecta. Pierdes un intento.")

        if len(set(palabra_oculta)) == len(letras_adivinadas):
            print("¡Felicidades! ¡Has adivinado la palabra correctamente!")
            break

        print(f"Intentos restantes: {intentos_restantes}")

    else:
        print("¡Oh no! Te has quedado sin intentos. La palabra correcta era:", palabra_oculta)

if __name__ == "__main__":
    jugar_ahorcado()
