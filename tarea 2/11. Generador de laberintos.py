import random

class Laberinto:
    def __init__(self, filas, columnas):
        self.filas = filas
        self.columnas = columnas
        self.grid = [['#' for _ in range(columnas)] for _ in range(filas)]

    def generar_laberinto(self, fila_actual, columna_actual):
        self.grid[fila_actual][columna_actual] = ' '

        direcciones = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        random.shuffle(direcciones)

        for direccion in direcciones:
            nueva_fila = fila_actual + direccion[0] * 2
            nueva_columna = columna_actual + direccion[1] * 2

            if 0 <= nueva_fila < self.filas and 0 <= nueva_columna < self.columnas and self.grid[nueva_fila][nueva_columna] == '#':
                pared_fila = fila_actual + direccion[0]
                pared_columna = columna_actual + direccion[1]
                self.grid[pared_fila][pared_columna] = ' '
                self.generar_laberinto(nueva_fila, nueva_columna)

    def imprimir_laberinto(self):
        for fila in self.grid:
            print(' '.join(fila))
    
    def resolver_laberinto(self, fila, columna):
        if fila < 0 or fila >= self.filas or columna < 0 or columna >= self.columnas or self.grid[fila][columna] == '#' or self.grid[fila][columna] == 'X':
            return False
        
        if fila == self.filas - 1 and columna == self.columnas - 1:
            self.grid[fila][columna] = 'X'
            return True
        
        self.grid[fila][columna] = 'X'
        
        if self.resolver_laberinto(fila + 1, columna) or self.resolver_laberinto(fila - 1, columna) or self.resolver_laberinto(fila, columna + 1) or self.resolver_laberinto(fila, columna - 1):
            return True
        
        self.grid[fila][columna] = ' '
        return False

def main():
    filas = int(input("Ingrese el número de filas del laberinto: "))
    columnas = int(input("Ingrese el número de columnas del laberinto: "))

    laberinto = Laberinto(filas, columnas)
    laberinto.generar_laberinto(0, 0)
    laberinto.grid[0][0] = ' '
    laberinto.grid[filas - 1][columnas - 1] = ' '

    print("\nLaberinto generado:")
    laberinto.imprimir_laberinto()

    fila_inicio = 0
    columna_inicio = 0

    print("\nResolviendo laberinto...")
    if laberinto.resolver_laberinto(fila_inicio, columna_inicio):
        print("\nLaberinto resuelto:")
        laberinto.imprimir_laberinto()
    else:
        print("\nNo se encontró solución para el laberinto.")

if __name__ == "__main__":
    main()
