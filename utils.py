import numpy as np
import random



def crear_tablero(tamaño):
    tablero = np.full((tamaño,tamaño), "_")
    return tablero



def colocar_barco(barco, tablero):
    for casilla in barco:
        tablero[casilla] = "O"
    return tablero



def disparar(casilla, tablero):
    if tablero[casilla] == "O":
        print("Tocado")
        tablero[casilla] = "X"
    else:
        print("Agua")
        tablero[casilla] = "A"
    return tablero




def crear_barco(eslora):
    casilla_0 = (random.randint(0,9), random.randint(0,9))
    orientacion = random.choice(["Vertical", "Horizontal"])

    barco = [casilla_0]
    casilla = casilla_0
    while len(barco) < eslora:
        if orientacion == "Vertical":
            casilla = (casilla[0]+1, casilla[1])
            barco.append(casilla) # Vertical
        else:
            casilla = (casilla[0], casilla[1]+1)
            barco.append(casilla) # Horizontal

    return barco


#def colocar_barcos(tablero):