import numpy as np
import random

def crear_tablero(tamaño):
    tablero = np.full((tamaño,tamaño), "_")
    return tablero

def crear_barco_dentro(eslora):
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

    for x,y in barco:
        if x>9 or y>9:
            barco = crear_barco_dentro(eslora)
    return barco

def colocar_barco(barco, tablero):
    for casilla in barco:
        tablero[casilla] = "O"
    return tablero


def disparar(casilla, tablero):
    if tablero[casilla] == "O":
        tablero[casilla] = "X"
    else:
        tablero[casilla] = "A"
    return tablero