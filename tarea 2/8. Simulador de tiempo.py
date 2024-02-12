import random

def obtener_temperatura():
    return round(random.uniform(10, 30), 2)  # Simula la temperatura en grados Celsius

def obtener_estado_tiempo():
    estados = ["Despejado", "Parcialmente nublado", "Nublado", "Lluvioso", "Neblinoso", "Tormenta"]
    return random.choice(estados)

def obtener_viento():
    return round(random.uniform(0, 30), 2)  # Simula la velocidad del viento en km/h

def obtener_humedad():
    return round(random.uniform(30, 80), 2)  # Simula el porcentaje de humedad

def obtener_pronostico(tiempo_actual):
    pronostico = {
        "Temperatura": obtener_temperatura(),
        "Estado del Tiempo": obtener_estado_tiempo(),
        "Viento": obtener_viento(),
        "Humedad": obtener_humedad()
    }
    return pronostico

def main():
    print("Simulador de Tiempo Meteorológico\n")
    ubicacion = input("Ingrese la ubicación para obtener el pronóstico del tiempo: ")

    tiempo_actual = obtener_pronostico(ubicacion)

    print("\nPronóstico del Tiempo:")
    print(f"Ubicación: {ubicacion}")
    print(f"Temperatura: {tiempo_actual['Temperatura']} °C")
    print(f"Estado del Tiempo: {tiempo_actual['Estado del Tiempo']}")
    print(f"Viento: {tiempo_actual['Viento']} km/h")
    print(f"Humedad: {tiempo_actual['Humedad']}%")

if __name__ == "__main__":
    main()
