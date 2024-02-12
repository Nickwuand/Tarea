class BancoDeDatos:
    def __init__(self):
        self.registros = {}

    def agregar_registro(self, clave, valor):
        self.registros[clave] = valor
        print("Registro agregado correctamente.")

    def actualizar_registro(self, clave, valor):
        if clave in self.registros:
            self.registros[clave] = valor
            print("Registro actualizado correctamente.")
        else:
            print("La clave proporcionada no existe.")

    def eliminar_registro(self, clave):
        if clave in self.registros:
            del self.registros[clave]
            print("Registro eliminado correctamente.")
        else:
            print("La clave proporcionada no existe.")

    def buscar_registro(self, clave):
        if clave in self.registros:
            print(f"Clave: {clave}, Valor: {self.registros[clave]}")
        else:
            print("La clave proporcionada no existe.")

    def mostrar_registros(self):
        if self.registros:
            print("Registros:")
            for clave, valor in self.registros.items():
                print(f"Clave: {clave}, Valor: {valor}")
        else:
            print("No hay registros en la base de datos.")


def main():
    banco_de_datos = BancoDeDatos()

    while True:
        print("\nMenú del Banco de Datos:")
        print("1. Agregar Registro")
        print("2. Actualizar Registro")
        print("3. Eliminar Registro")
        print("4. Buscar Registro")
        print("5. Mostrar Registros")
        print("6. Salir")

        opcion = input("Ingrese su opción: ")

        if opcion == '1':
            clave = input("Ingrese la clave del nuevo registro: ")
            valor = input("Ingrese el valor del nuevo registro: ")
            banco_de_datos.agregar_registro(clave, valor)

        elif opcion == '2':
            clave = input("Ingrese la clave del registro a actualizar: ")
            valor = input("Ingrese el nuevo valor del registro: ")
            banco_de_datos.actualizar_registro(clave, valor)

        elif opcion == '3':
            clave = input("Ingrese la clave del registro a eliminar: ")
            banco_de_datos.eliminar_registro(clave)

        elif opcion == '4':
            clave = input("Ingrese la clave del registro a buscar: ")
            banco_de_datos.buscar_registro(clave)

        elif opcion == '5':
            banco_de_datos.mostrar_registros()

        elif opcion == '6':
            print("Saliendo...")
            break

        else:
            print("Opción no válida. Por favor ingrese un número entre 1 y 6.")


if __name__ == "__main__":
    main()
