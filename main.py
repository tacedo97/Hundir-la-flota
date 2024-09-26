import utils

#Creamos un tablero vacío para el contrincante y otro para el usuario que juega
tablero_contrincante = utils.crear_tablero(10)
tablero_usuario = utils.crear_tablero(10)

#Tamaños de los barcos necesarios para ambos jugadores
esloras = [4, 3, 3, 2, 2, 2]

#Vamos a generar el listado de barcos del contricante
listado_barcos_contrincante = [] #Primero vacío y, a medida que vemos que se cumplen las condiciones de estar dentro y no superponerse entre ellos, los vamos añadiendo
posiciones_barcos_contricante = [posicion for posicion in listado_barcos_contrincante]

for eslora in esloras:
    barco_correcto = False
    while not barco_correcto:
        barco_contricante = utils.crear_barco_dentro(eslora)
        barco_correcto = True
        for posicion in barco_contricante:
            if posicion in posiciones_barcos_contricante:
                barco_valido = False 
                break
        if barco_correcto:
            listado_barcos_contrincante.append(barco_contricante)
            posiciones_barcos_contricante = [posicion for posicion in listado_barcos_contrincante]


#Vamos a generar el listado de nuestros barcos
listado_barcos_usuario = [] #Primero vacío y, a medida que vemos que se cumplen las condiciones de estar dentro y no superponerse entre ellos, los vamos añadiendo
posiciones_barcos_usuario= [posicion for posicion in listado_barcos_usuario]

for eslora in esloras:
    barco_correcto = False
    while not barco_correcto:
        barco_usuario = utils.crear_barco_dentro(eslora)
        barco_correcto = True
        for posicion in barco_usuario:
            if posicion in posiciones_barcos_usuario:
                barco_valido = False 
                break
        if barco_correcto:
            listado_barcos_usuario.append(barco_usuario)
            posiciones_barcos_usuario = [posicion for posicion in listado_barcos_usuario]
    

#Vamos a definir los tableros iniciales con sus respectivos barcos aleatorios (el del contrincante y el nuestro)
for barco_correcto_contrincante in listado_barcos_contrincante:
    tablero_contrincante = utils.colocar_barco(barco_correcto_contrincante, tablero_contrincante)

for barco_correcto_usuario in listado_barcos_usuario:
    tablero_usuario = utils.colocar_barco(barco_correcto_usuario, tablero_usuario)


#print temporal para ver qué pasa cuando acertamos el disparo
print("El tablero del contrincante con los barcos colocados -->", listado_barcos_contrincante)
print("\nNuestro tablero con los barcos colocados -->", listado_barcos_usuario)

'''REVISADO HASTA AQUÍ: hacia abajo solo funciona el bucle si el usuario (nosotros) acierta, si no, da fallos'''

#Vamos a definir los tableros ocultos:
tablero_contrincante_oculto = utils.crear_tablero(10)
tablero_usuario_oculto = utils.crear_tablero(10)

#Inicialmente, tenemos que nos faltan por disparar a todas las posiciones de los barcos
disparos_faltantes_contrincante = sum(esloras)
disparos_faltantes_usuario = sum(esloras)



#Mientras haya disparos por tirar, se debe seguir jugando pues no hay un ganador
while disparos_faltantes_usuario > 0 and disparos_faltantes_contrincante > 0:
    #La partida se inicializa con el usuario introduciendo la casilla de disparo (supongamos que el input siempre va a ser correcto)
    print("A continuación, vas a introducir las posiciones de la casilla. Para ello, introducirás números enteros entre el 0 y el 9, ambos incluidos")
    fila_usuario = int(input("Fila "))
    col_usuario = int(input("Columna "))
    disparo_usuario = (fila_usuario, col_usuario)
    #Actualizamos cómo queda el tablero del contrincate con ese disparo
    tablero_contrincante = utils.disparar(disparo_usuario, tablero_contrincante) 
    print(disparo_usuario) #Imprimimos la casilla del disparo introducido

    if tablero_contrincante[disparo_usuario] not in ["_", "A"]:
        print("Has acertado")
        #Seguimos jugando
        #Se pide de nuevo como input un disparo
        disparos_faltantes_usuario = disparos_faltantes_usuario-1
        tablero_contrincante_oculto = utils.disparar(disparo_usuario, tablero_contrincante_oculto)
        print("El tablero del contrincante tiene el siguiente aspecto \n", tablero_contrincante_oculto)
        
    else:
        print("Has fallado")
        tablero_contrincante_oculto = utils.disparar(disparo_usuario, tablero_contrincante_oculto)
        print("El tablero del contrincante tiene el siguiente aspecto \n", tablero_contrincante_oculto)
        #Juega el contrincante
        #disparo_contrincante = (utils_Tamara.random.randint(0,9), utils_Tamara.random.randint(0,9))
        d = True
        while d:
            disparo_contrincante = (utils.random.randint(0,9), utils.random.randint(0,9))
            print("Como has fallado, juega el contricante. Su disparo es", disparo_contrincante)
            tablero_usuario_oculto = utils.disparar(disparo_contrincante, tablero_usuario_oculto)
            if tablero_usuario[disparo_contrincante] not in ["_", "A"]:
                print("El contrincante ha acertado, sigue")
                #El contrincante sigue jugando
                #Se pide de nuevo como input un disparo
                disparos_faltantes_contrincante = disparos_faltantes_contrincante-1
                tablero_usuario_oculto = utils.disparar(disparo_contrincante, tablero_usuario_oculto)
            else:
                d = False
                print("El contrincante no ha acertado, te toca")
            break
    

else:
    if disparos_faltantes_usuario == 0:
        print("Has ganado")
    else:
        print("El contrincante te ha ganado")