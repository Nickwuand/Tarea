class JuegoPreguntas:
    def __init__(self):
        self.preguntas = {
            "Matematicas": [
                {"pregunta": "¿Cuánto es 2 + 2?", "respuesta": "4"},
                {"pregunta": "¿Cuánto es 3 * 5?", "respuesta": "15"},
                {"pregunta": "¿Cuánto es 8 / 2?", "respuesta": "4"}
            ],
            "Ciencia": [
                {"pregunta": "¿Cuál es el símbolo químico del agua?", "respuesta": "H2O"},
                {"pregunta": "¿Qué planeta es conocido como el planeta rojo?", "respuesta": "Marte"},
                {"pregunta": "¿Quién descubrió la gravedad?", "respuesta": "Isaac Newton"}
            ],
            "Historia": [
                {"pregunta": "¿En qué año ocurrió la Revolución Francesa?", "respuesta": "1789"},
                {"pregunta": "¿Quién fue el primer presidente de los Estados Unidos?", "respuesta": "George Washington"},
                {"pregunta": "¿Qué evento marcó el fin de la Segunda Guerra Mundial?", "respuesta": "La rendición de Japón"}
            ]
        }

    def seleccionar_categoria(self):
        print("Categorías disponibles:")
        for categoria in self.preguntas.keys():
            print("- " + categoria)
        seleccion = input("Selecciona una categoría: ")
        return seleccion

    def jugar(self):
        print("¡Bienvenido al Juego de Preguntas y Respuestas!")
        while True:
            categoria = self.seleccionar_categoria()
            if categoria in self.preguntas:
                print(f"\nCategoria: {categoria}")
                for pregunta in self.preguntas[categoria]:
                    respuesta = input(pregunta["pregunta"] + "\nRespuesta: ").strip().lower()
                    if respuesta == pregunta["respuesta"].lower():
                        print("¡Respuesta correcta!\n")
                    else:
                        print(f"Respuesta incorrecta. La respuesta correcta es: {pregunta['respuesta']}\n")
                jugar_nuevamente = input("¿Deseas jugar de nuevo? (s/n): ").lower()
                if jugar_nuevamente != 's':
                    break
            else:
                print("Categoría no válida. Inténtalo de nuevo.")

def main():
    juego = JuegoPreguntas()
    juego.jugar()

if __name__ == "__main__":
    main()
