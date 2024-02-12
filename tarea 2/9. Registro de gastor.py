class RegistroGastos:
    def __init__(self):
        self.gastos = {}

    def agregar_gasto(self, categoria, monto):
        if categoria in self.gastos:
            self.gastos[categoria] += monto
        else:
            self.gastos[categoria] = monto

    def calcular_total(self):
        return sum(self.gastos.values())

    def generar_informe(self):
        print("Informe de Gastos:")
        for categoria, monto in self.gastos.items():
            print(f"{categoria}: ${monto:.2f}")
        total = self.calcular_total()
        print(f"\nTotal: ${total:.2f}")

    def establecer_presupuesto(self, categoria, presupuesto):
        if categoria in self.gastos:
            print(f"Presupuesto actual para '{categoria}': ${self.gastos[categoria]:.2f}")
            print(f"Presupuesto nuevo establecido para '{categoria}': ${presupuesto:.2f}")
            self.gastos[categoria] = presupuesto
        else:
            print(f"No se encontraron gastos para la categoría '{categoria}'. Presupuesto establecido en ${presupuesto:.2f}")

def main():
    registro = RegistroGastos()

    while True:
        print("\nSistema de Registro de Gastos")
        print("1. Agregar Gasto")
        print("2. Generar Informe")
        print("3. Establecer Presupuesto")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            categoria = input("Ingrese la categoría del gasto: ")
            monto = float(input("Ingrese el monto del gasto: "))
            registro.agregar_gasto(categoria, monto)
            print("Gasto agregado correctamente.")
        elif opcion == '2':
            registro.generar_informe()
        elif opcion == '3':
            categoria = input("Ingrese la categoría para establecer el presupuesto: ")
            presupuesto = float(input("Ingrese el presupuesto: "))
            registro.establecer_presupuesto(categoria, presupuesto)
        elif opcion == '4':
            print("Saliendo del sistema de registro de gastos...")
            break
        else:
            print("Opción no válida. Por favor ingrese 1, 2, 3 o 4.")

if __name__ == "__main__":
    main()
