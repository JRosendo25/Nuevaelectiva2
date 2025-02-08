
estacionamiento = [
    [' ', ' ', ' ', ' ', ' ', ' '],
    [' ', 'C', 'C', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', 'C', ' '],
    [' ', ' ', 'C', ' ', 'C', ' '],
    [' ', ' ', 'C', ' ', ' ', ' '],
    ['R', ' ', ' ', ' ', ' ', ' ']
]

def imprimir_estacionamiento():
    print("+-----+")
    for fila in estacionamiento:
        print("|" + "".join(fila) + "|")
    print("+-----+")


def mover_coche(direccion):

    for i, fila in enumerate(estacionamiento):
        if 'R' in fila:
            fila_idx, col_idx = i, fila.index('R')
            break

    if direccion == 'arriba' and fila_idx > 0 and estacionamiento[fila_idx - 1][col_idx] == ' ':
        estacionamiento[fila_idx][col_idx] = ' '
        estacionamiento[fila_idx - 1][col_idx] = 'R'
    elif direccion == 'abajo' and fila_idx < 5 and estacionamiento[fila_idx + 1][col_idx] == ' ':
        estacionamiento[fila_idx][col_idx] = ' '
        estacionamiento[fila_idx + 1][col_idx] = 'R'
    elif direccion == 'izquierda' and col_idx > 0 and estacionamiento[fila_idx][col_idx - 1] == ' ':
        estacionamiento[fila_idx][col_idx] = ' '
        estacionamiento[fila_idx][col_idx - 1] = 'R'
    elif direccion == 'derecha' and col_idx < 5 and estacionamiento[fila_idx][col_idx + 1] == ' ':
        estacionamiento[fila_idx][col_idx] = ' '
        estacionamiento[fila_idx][col_idx + 1] = 'R'


def main():
    while True:
        imprimir_estacionamiento()
        if estacionamiento[0][5] == 'R':  
            print("ganaste")
            break
        direccion = input("Mueve el coche (Escribir: arriba, abajo, izquierda, derecha): ")
        if direccion in ['arriba', 'abajo', 'izquierda', 'derecha']:
            mover_coche(direccion)
        else:
            print("Dirección no válida.")

if __name__ == "__main__":
    main()