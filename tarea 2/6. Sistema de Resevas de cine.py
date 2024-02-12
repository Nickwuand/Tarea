class Cine:
    def __init__(self, filas, columnas):
        self.filas = filas
        self.columnas = columnas
        self.asientos_disponibles = {}
        self.reservas_realizadas = {}

        for fila in range(1, self.filas + 1):
            for columna in range(1, self.columnas + 1):
                self.asientos_disponibles[(fila, columna)] = "Disponible"

    def mostrar_disponibilidad(self):
        for fila in range(1, self.filas + 1):
            for columna in range(1, self.columnas + 1):
                estado = self.asientos_disponibles[(fila, columna)]
                print(f"Fila {fila}, Asiento {columna}: {estado}")
            print()

    def reservar_asiento(self, fila, columna):
        if (fila, columna) in self.asientos_disponibles:
            if self.asientos_disponibles[(fila, columna)] == "Disponible":
                self.asientos_disponibles[(fila, columna)] = "Reservado"
                print("¡Asiento reservado exitosamente!")
                self.reservas_realizadas[(fila, columna)] = "Reservado"
            else:
                print("Lo siento, este asiento ya está reservado.")
        else:
            print("Asiento inválido.")

def main():
    cine = Cine(filas=5, columnas=10)

    while True:
        print("\nSistema de Reservas de Cine")
        print("1. Mostrar disponibilidad de asientos")
        print("2. Reservar un asiento")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            cine.mostrar_disponibilidad()
        elif opcion == '2':
            fila = int(input("Ingrese el número de fila: "))
            columna = int(input("Ingrese el número de asiento: "))
            cine.reservar_asiento(fila, columna)
        elif opcion == '3':
            print("Saliendo del sistema de reservas de cine...")
            break
        else:
            print("Opción no válida. Por favor ingrese 1, 2 o 3.")

if __name__ == "__main__":
    main()
