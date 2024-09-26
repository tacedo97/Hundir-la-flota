import utils

def jugar_hundir_la_flota():
    print("Empieza el juego de hundir la flota. El juego consiste en hundir todos los barcos de tu contrincante antes que él")
    print("Ambos contáis con los siguientes barcos:")
    print("Tres barcos con eslora dos \nDos barcos con eslora tres \nUn barco con eslora cuatro")
    print("Tanto tu contrincante como tú, los tendréis dispuestos a lo largo del tablero de forma aleatoria.")
    print("Introduce el tamaño del tablero con el que quieres jugar: ")
    tamaño = input()
    if type(int(tamaño)) != int or int(tamaño) < 4 :
        raise TypeError("Reinicia el juego e introduce un tamaño adecuado para que entren todos los barcos (para ello, el tamaño debe ser siempre mayor o igual que 4)")
    else:
        print("Así pues, tienes el siguiente tablero para jugar:")
        tamaño = int(tamaño)
        tablero_vacío = utils.crear_tablero(tamaño)
        print(tablero_vacío)
        
        barcos_usuario = []
        barcos_contrincante = []
