import random

personajes = ["héroe", "princesa", "bruja", "mago", "caballero", "dragón"]
lugares = ["castillo", "bosque", "cueva", "ciudad", "montaña"]
eventos = ["rescatar", "derrotar", "encontrar", "explorar", "proteger"]

def generar_historia():
    personaje = random.choice(personajes)
    lugar = random.choice(lugares)
    evento = random.choice(eventos)

    historia = f"En un lejano reino, un valiente {personaje} se aventuró hacia el {lugar} para {evento} el tesoro perdido."
    return historia

def main():
    print("Generador de Historias Aleatorias")
    print("¿Qué tipo de historia deseas generar?")

    while True:
        opcion = input("Presiona Enter para generar una historia o E para salir: ").upper()

        if opcion == "E":
            print("Saliendo del generador de historias...")
            break
        else:
            historia = generar_historia()
            print("\n" + historia + "\n")

if __name__ == "__main__":
    main()
