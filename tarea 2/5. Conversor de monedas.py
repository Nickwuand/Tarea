def convertir_moneda(monto, tasa_cambio):
    return monto * tasa_cambio

def main():
    print("Bienvenido al Conversor de Monedas")

    moneda_origen = input("Ingrese la moneda de origen: ")
    moneda_destino = input("Ingrese la moneda de destino: ")
    monto = float(input(f"Ingrese el monto en {moneda_origen}: "))

    if moneda_origen == "USD" and moneda_destino == "EUR":
        tasa_cambio = 0.88  # Tasa de cambio actual de USD a EUR
    elif moneda_origen == "EUR" and moneda_destino == "USD":
        tasa_cambio = 1.14  # Tasa de cambio actual de EUR a USD
    elif moneda_origen == "USD" and moneda_destino == "GBP":
        tasa_cambio = 0.76  # Tasa de cambio actual de USD a GBP
    elif moneda_origen == "GBP" and moneda_destino == "USD":
        tasa_cambio = 1.32  # Tasa de cambio actual de GBP a USD
    else:
        tasa_cambio = float(input(f"Ingrese la tasa de cambio de {moneda_origen} a {moneda_destino}: "))

    monto_convertido = convertir_moneda(monto, tasa_cambio)
    print(f"{monto} {moneda_origen} equivale a {monto_convertido} {moneda_destino}")

if __name__ == "__main__":
    main()
