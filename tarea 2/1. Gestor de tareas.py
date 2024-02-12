class Tarea:
    def __init__(self, descripcion, fecha_limite=None, prioridad=None):
        self.descripcion = descripcion
        self.fecha_limite = fecha_limite
        self.prioridad = prioridad

class ListaDeTareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, tarea):
        self.tareas.append(tarea)

    def eliminar_tarea(self, indice):
        if 0 <= indice < len(self.tareas):
            del self.tareas[indice]

    def editar_tarea(self, indice, nueva_descripcion, nueva_fecha_limite=None, nueva_prioridad=None):
        if 0 <= indice < len(self.tareas):
            tarea = self.tareas[indice]
            tarea.descripcion = nueva_descripcion
            if nueva_fecha_limite:
                tarea.fecha_limite = nueva_fecha_limite
            if nueva_prioridad:
                tarea.prioridad = nueva_prioridad

    def mostrar_tareas(self):
        if not self.tareas:
            print("No hay tareas en la lista.")
        else:
            print("Tareas:")
            for i, tarea in enumerate(self.tareas):
                print(f"{i + 1}. {tarea.descripcion}")
                if tarea.fecha_limite:
                    print(f"   Fecha límite: {tarea.fecha_limite}")
                if tarea.prioridad:
                    print(f"   Prioridad: {tarea.prioridad}")
                print()

def main():
    lista_de_tareas = ListaDeTareas()

    while True:
        print("\nMenú de Lista de Tareas:")
        print("1. Agregar Tarea")
        print("2. Eliminar Tarea")
        print("3. Editar Tarea")
        print("4. Mostrar Tareas")
        print("5. Salir")

        opcion = input("Ingrese su opción: ")

        if opcion == '1':
            descripcion = input("Ingrese la descripción de la tarea: ")
            fecha_limite = input("Ingrese la fecha límite (opcional): ")
            prioridad = input("Ingrese la prioridad (opcional): ")
            tarea = Tarea(descripcion, fecha_limite, prioridad)
            lista_de_tareas.agregar_tarea(tarea)
            print("Tarea agregada.")

        elif opcion == '2':
            indice = int(input("Ingrese el número de la tarea a eliminar: ")) - 1
            lista_de_tareas.eliminar_tarea(indice)
            print("Tarea eliminada.")

        elif opcion == '3':
            indice = int(input("Ingrese el número de la tarea a editar: ")) - 1
            descripcion = input("Ingrese la nueva descripción de la tarea: ")
            fecha_limite = input("Ingrese la nueva fecha límite (opcional): ")
            prioridad = input("Ingrese la nueva prioridad (opcional): ")
            lista_de_tareas.editar_tarea(indice, descripcion, fecha_limite, prioridad)
            print("Tarea editada.")

        elif opcion == '4':
            lista_de_tareas.mostrar_tareas()

        elif opcion == '5':
            print("Saliendo...")
            break

        else:
            print("Opción inválida. Por favor ingrese un número entre 1 y 5.")

if __name__ == "__main__":
    main()
