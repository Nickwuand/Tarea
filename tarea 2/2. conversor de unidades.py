def longitud():
    print("\nConversor de Longitud")
    print("1. Metros a Pies")
    print("2. Pies a Metros")
    print("3. Kilómetros a Millas")
    print("4. Millas a Kilómetros")
    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        metros = float(input("Ingrese la longitud en metros: "))
        pies = metros * 3.281
        print(f"{metros} metros son {pies} pies.")
    elif opcion == '2':
        pies = float(input("Ingrese la longitud en pies: "))
        metros = pies / 3.281
        print(f"{pies} pies son {metros} metros.")
    elif opcion == '3':
        kilometros = float(input("Ingrese la longitud en kilómetros: "))
        millas = kilometros / 1.609
        print(f"{kilometros} kilómetros son {millas} millas.")
    elif opcion == '4':
        millas = float(input("Ingrese la longitud en millas: "))
        kilometros = millas * 1.609
        print(f"{millas} millas son {kilometros} kilómetros.")
    else:
        print("Opción no válida.")

def masa():
    print("\nConversor de Masa")
    print("1. Kilogramos a Libras")
    print("2. Libras a Kilogramos")
    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        kilogramos = float(input("Ingrese la masa en kilogramos: "))
        libras = kilogramos * 2.205
        print(f"{kilogramos} kilogramos son {libras} libras.")
    elif opcion == '2':
        libras = float(input("Ingrese la masa en libras: "))
        kilogramos = libras / 2.205
        print(f"{libras} libras son {kilogramos} kilogramos.")
    else:
        print("Opción no válida.")

def temperatura():
    print("\nConversor de Temperatura")
    print("1. Celsius a Fahrenheit")
    print("2. Fahrenheit a Celsius")
    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        celsius = float(input("Ingrese la temperatura en grados Celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius} grados Celsius son {fahrenheit} grados Fahrenheit.")
    elif opcion == '2':
        fahrenheit = float(input("Ingrese la temperatura en grados Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5/9
        print(f"{fahrenheit} grados Fahrenheit son {celsius} grados Celsius.")
    else:
        print("Opción no válida.")

def main():
    while True:
        print("\nConversor de Unidades")
        print("1. Longitud")
        print("2. Masa")
        print("3. Temperatura")
        print("4. Salir")
        opcion = input("Seleccione el tipo de conversión o 4 para salir: ")

        if opcion == '1':
            longitud()
        elif opcion == '2':
            masa()
        elif opcion == '3':
            temperatura()
        elif opcion == '4':
            print("Saliendo...")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
