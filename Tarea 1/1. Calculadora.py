def calculadora():
    num1 = float(input("Ingrese el primer número: "))  # Corregido aquí
    num2 = float(input("Ingrese el segundo número: "))  # Corregido aquí
    operacion = input("Ingrese la operación (+, -, *, /): ")

    if operacion == '+':
        resultado = num1 + num2  # Corregido aquí
    elif operacion == '-':
        resultado = num1 - num2  # Corregido aquí
    elif operacion == '*':
        resultado = num1 * num2  # Corregido aquí
    elif operacion == '/':
        resultado = num1 / num2  # Corregido aquí
    else:
        resultado = "Operación no válida"

    print("Resultado:", resultado)  # Corregido aquí

calculadora()  # Corregido aquí
