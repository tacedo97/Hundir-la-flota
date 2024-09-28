import numpy as np
import random

#Creamos el tablero a partir del tamaño que lo queremos
def crear_tablero(tamaño):
    tablero = np.full((tamaño,tamaño), "_")
    return tablero

#Creamos un barco de largo=eslora y cerciorándos de que está dentro del tablero de tamañoxtamaño casillas (que vamos a hacerlo de momento para tamaño=10)
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

#Creamos un listado de barcos de modo que no estén superpuestos entre sí
#Creamos un listado de barcos de modo que no estén superpuestos entre sí 
# ¡¡¡¡¡¡¡¡¡CORREGIRRRRRRRRRRRRRRRRRR!!!!!!! El list comprehension está mal, no nos da una lista de posiciones sino una lista de listas!!!!!!!!!!!
def flota_dentro_no_superpuesta(esloras):
    flota = []
    posiciones_flota = [posicion for posicion in flota]
    for eslora in esloras:
        barco_correcto = False
        while not barco_correcto:
            barco_tentativo = crear_barco_dentro(eslora)
            barco_correcto = True
            for posicion in barco_tentativo:
                if posicion in posiciones_flota:
                    barco_valido = False 
                    break
            if barco_correcto:
                flota.append(barco_tentativo)
                posiciones_flota = [posicion for posicion in flota]
    return flota

#Colocamos un barco dentro de un tablero
def colocar_barco(barco, tablero):
    for casilla in barco:
        tablero[casilla] = "O"
    return tablero


#Dada una casilla y un tablero, si la casilla aplica a un barco, ponemos una X (tocado), y si no, una A (agua)
def disparar(casilla, tablero):
    if tablero[casilla] == "O":
        tablero[casilla] = "X"
    else:
        tablero[casilla] = "A"
    return tablero


#Colocamos la flota dentro del tablero no superpuesta
def colocar_barcos_dentro_nosuperpuestos(tablero, flota):
    for barco in flota:
        tablero = colocar_barco(barco, tablero)
    return tablero



def jugar_hlf(): #ME QUEDA POR CONTROLAR SI ALGÚN USUARIO REPITE DISPARO!
    nombre_usuario = input("Nombre del jugador: ")
    print(nombre_usuario + ", ¡bienvenido al juego de 'Hundir la flota'!")
    '''
    print("Tanto tú como tu contrincante disponéis de un tablero de 10x10 casillas en el que poder colocar un total de 6 barcos, \
          (tres de largo 2, dos de largo 3 y uno de largo 4).")
    print("El juego finaliza cuando uno de los dos consigue hundir toda la flota del otro.")
    print("Por turnos, cada uno de vosotros iréis realizando disparos sobre el tablero del oponente, de modo que si tocáis alguno de sus \
          barcos, seguiréis jugando y si por el contrario, falláis, el turno pasará al contricante.")
    '''

    #Creamos dos tableros para el rival (inicialmente vacíos)
    tablero_rival = crear_tablero(10) #En este, se colocarán los barcos del rival
    tablero_rival_oculto = crear_tablero(10) #Este es el tablero del rival que nosotros veremos cada vez que disparemos
    
    #Creamos el tablero en el que colocaremos nuestros barcos (inicialmente vacío)
    tablero_usuario = crear_tablero(10)
    
    #Esloras de los barcos del juego
    esloras_hlf = [4, 3, 3, 2, 2, 2]

    #Generamos la flota aleatoria del contrincante = listado de barcos del rival
    flota_rival = flota_dentro_no_superpuesta(esloras_hlf)

    #Generamos nuestra flota aleatoria = nuestro listado de barcos EN UN FUTURO SE OFRECERÁ LA POSIBILIDAD DE GENERAR LA FLOTA ALEATORIA O LA QUE EL USUARIO QUIERA
    flota_usuario = flota_dentro_no_superpuesta(esloras_hlf)

    #Colocamos la flota aleatoria del rival en su tablero
    tablero_rival = colocar_barcos_dentro_nosuperpuestos(tablero_rival, flota_rival)
    
    #Colocamos nuestra flota aleatoria en nuestro tablero
    tablero_usuario = colocar_barcos_dentro_nosuperpuestos(tablero_usuario, flota_usuario)

    #print temporal para ver qué pasa cuando acertamos el disparo
    print("\nPrints temporales para hacer pruebas de distintos tiros y comprobar si se ejecuta bien")
    print("\nEl tablero del contrincante con los barcos colocados -->", flota_rival)
    print("\nNuestro tablero con los barcos colocados -->", flota_usuario, "\n\n")

    #Contabilizamos los disparos que tienen que acertar los jugadores, de modo que se reste uno por cada disparo acertado
    disparos_acertados_rival = sum(esloras_hlf)
    disparos_acertados_usuario = sum(esloras_hlf)

    #Empieza el bucle de disparos (empezamos nosotros)
    while disparos_acertados_rival > 0 and disparos_acertados_usuario > 0:
        #La partida se inicializa con el usuario introduciendo la casilla de disparo (supongamos que el input siempre va a ser correcto) 
        #EN UN FUTURO, IMPLEMENTAREMOS LA FUNCIONALIDAD DE QUE SI EL USUARIO METE ALGO QUE NO SE UN Nº ENTRE EL 0 Y EL 9, NO FALLE Y SE TENGA QUE VOLVER A 
        #EMPEZAR SINO QUE LE VUELVA A PEDIR INTRODUCIRLO
        print("*"*50 + "  TURNO DEL USUARIO  " + "*"*50)
        print("A continuación, vas a introducir las posiciones del disparo. Para ello, introducirás números enteros entre el 0 y el 9, ambos incluidos\n")
        
        fila_usuario = int(input("Fila "))
        col_usuario = int(input("Columna "))
        disparo_usuario = (int(fila_usuario), int(col_usuario))
        #Actualizamos cómo queda el tablero del contrincante con el disparo
        tablero_rival = disparar(disparo_usuario, tablero_rival)
        print("\nTu disparo es", disparo_usuario) #Imprimimos la casilla del disparo introducido

        #Si disparamos a un barco
        if tablero_rival[disparo_usuario] not in ["_", "A"]: 
            print("\nHas acertado\n")
            #Seguimos jugando
            #Se pide de nuevo como input un disparo
            tablero_rival_oculto[disparo_usuario] = tablero_rival[disparo_usuario]
            disparos_acertados_usuario = disparos_acertados_usuario-1
            print(tablero_rival_oculto)
            print("\nTe quedan ", disparos_acertados_usuario, "disparos por acertar.")
                    
        #Si disparamos al agua
        else:
            print("\n\nHas fallado, el tablero del rival queda así:\n")
            tablero_rival_oculto[disparo_usuario] = tablero_rival[disparo_usuario]
            print(tablero_rival_oculto, "\n")
            print("*"*50 + "  TURNO DEL RIVAL  " + "*"*50)
            #Juega el contrincante
            d = True
            while d:
                disparo_contrincante = (random.randint(0,9), random.randint(0,9)) #Disparo aleatorio del rival
                print("\nSu disparo es", disparo_contrincante)
                tablero_usuario = disparar(disparo_contrincante, tablero_usuario)
                if tablero_usuario[disparo_contrincante] not in ["_", "A"]:
                    disparos_acertados_rival = disparos_acertados_rival-1
                    print("\nEl contrincante ha acertado, quedándole así", disparos_acertados_rival, "disparos por acertar")
                else:
                    d = False
                    print("\nEl contrincante no ha acertado, te toca\n")
                    break
            
    else:
        if disparos_acertados_usuario == 0:
            print("\n¡Enhorabuena,", nombre_usuario ,"has ganado!")
        else:
            print("\nEl contrincante te ha ganado")