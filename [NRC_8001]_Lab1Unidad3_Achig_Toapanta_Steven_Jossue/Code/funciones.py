import os
import time
from ViaInteligente import Via_Inteligente

def ingresarEstado(ubicacion):
    """
    Función para ingresar el estado de una vía si esta despejada o congestionada.
    Parametros:
        ubicacion (str): Indica la ubicacion de la via inteligente.
    Retorna:
        estado (str): Indica el estado de la via inteligente.
    """
    #variable bandera para saber si seguimos con el bucle o no.
    sigue = True
    #mientras la bandera sea verdadera seguimos con el bucle.
    while(sigue==True):
        #se imprime un mensaje informativo sobre las opciones que se pueden ingresar.
        print("\nPorfavor Ingrese '0' (para indicar que esta desalojada) o '1' (Para indicar que esta llena)") 
        # Se solicita el ingreso del estado de la vía.
        estado = input("Por favor ingrese el estado de la via " + ubicacion + ": ")
        #se realiza un cambio de todo el estado a mayusculas y se eliminan los espacios en blanco.
        estado = estado.upper().strip().replace(" ", "")
        # Si el estado ingresado es salir.
        if estado == 'SALIR':
            #se rompe el bucle.
            sigue=False
            #se retorna el estado.
            return estado
        #si el estado ingresado es defierente de 0 o 1.
        elif estado != '0' and estado != '1':
            # Se imprime un mensaje de error.
            print("\nEl estado no es correcto, Por favor intente de nuevo\n")
            #se espera un segundo para que el usuario pueda leer el mensaje.
            time.sleep(0.1)
            #se limpia la pantalla.
            os.system ("cls")
            #se vuelve a imprimir el menu de opciones.
            sigue=True
        #si el estado ingresado es 0 o 1.
        else:
            #se rompe el bucle.
            sigue=False
            #se retorna el estado.
            return estado

def IngresarUbicacion():
    """
    Función para ingresar la ubicación, en que vía se encuntra.
    Parametros:
        No recibe parametros.
    Retorna:
        ubicacion (str): Indica la ubicacion de la via inteligente.
    """
    #variable bandera para saber si seguimos con el bucle o no.
    sigue = True
    #mientras la bandera sea verdadera seguimos con el bucle.
    while(sigue==True):
        # Se imprime el menu de opciones.
        print("Vías disponibles: Chilibulo, Colonche, Pelileo, Carapungo")
        #se imprime la opcion de salir
        print("Si desea salir del pograma ingrese en cualquier momento la palabra 'salir'\n")
        # Se pide la ubicacion de la via inteligente.
        ubicacionSinFormato = input("\nPor favor ingrese en que via se encuentra: ")
        # Se cambia la ubicacion a mayusculas y se eliminan los espacios en blanco.
        ubicacion = ubicacionSinFormato.upper().strip().replace(" ", "")
        # Si la ubicacion ingresada es igual a la palabra 'SALIR'.
        if ubicacion == 'SALIR':
            # Se termina el bucle para el ingreso de una ubicación valida.
            sigue=False
            #se retorna la ubicacion con el valor de salir para que el programa se cierre.
            return ubicacion
        # Si la ubicacion ingresada se encuentra fuera del rango de las ubicaciones disponibles.
        elif  ubicacion != 'CHILIBULO' and ubicacion != 'COLONCHE' and ubicacion != 'PELILEO' and ubicacion != 'CARAPUNGO' and ubicacion != 'SALIR':
            # Se imprime un mensaje de error.
            print("\nLa ubicación no es correcta, Por favor intente de nuevo\n")
            #el bucle continua
            sigue = True
            #se espera un segundo para que el usuario pueda leer el mensaje.
            time.sleep(0.1)
            #se limpia la pantalla.
            os.system ("cls")
        # Si la ubicacion ingresada se encuentra dentro del rango de las ubicaciones disponibles.
        else:
            # Se termina el bucle para el ingreso de una ubicación valida.
            sigue=False
            #se retorna la ubicacion.
            return ubicacion

def moverLaVía(ubicacion):
    """
    Función para moverse a otra vía en caso de que esta necesite ser desalojada.
    Parametros:
        ubicacion (str): Indica la ubicacion de la via inteligente.
    Retorna:
        retorna el costo de moverse a la via que es 1.
    """
    #se imprime un divisor para mejor visaulización.
    print("\n" + "V".center(100,"-"))
    # Se imprime un mensaje indicando que la vía está congestionada.
    print("La vía " + ubicacion + " está congestionada")
    # Se imprime un mensaje indicando que se está moviendo a otra vía.
    print("Moviendose a la vía: " + ubicacion + "........")
    #se imprime un mensaje sobre el costo de moverse a la via.
    print("El costo por moverse a la via " + ubicacion + " es de: 1")
    # Imprime la vía en la que se encuentra
    print("Se encuentra en la vía", ubicacion)
    # Se retorna el costo de moverse a la via.
    return 1

def analizarVias():
    """
    Función para analizar las vias y sus estados y tomar la desición de desalojar o no las vías segun las recorramos.
    Parametros:
        No recibe parametros
    Retorna:
        No retorna nada.
    """
    # Se crea el diccionario de la ubicacion de las vías.
    estadoObjetivo = {'CHILIBULO': '0', 'COLONCHE': '0', 'PELILEO': '0','CARAPUNGO': '0'}
    # Se crea una instancia de la clase viaInteligente.
    via = Via_Inteligente()
    # Se inicializa el costo
    costo = 0
    #se imprime unos saltos de linea para mejor visualización.
    print("\n\n")
    #se almacena la bienvenida y se usa la funcion center para hacer una bienvenida mas agradable a la vista
    bienvenida = "Bienvenido al sistema de control de vias inteligentes".upper().center(100,"-")
    #imprimimos la bienvenida
    print(bienvenida)
    #se alamacea la ubicacion de la via inteligente tomado de la funcion ingresarUbicacion.
    ubicacion = IngresarUbicacion()
    # Si la ubicacion ingresada es igual a la palabra 'SALIR'.
    if ubicacion == 'SALIR':
        # Se imprime un mensaje de despedida se termina el bucle.
        print("Gracias por usar el sistema")
    # Si la ubicacion ingresada es correcta.
    else:
        #Se ingresa el estado de la vía haciendo uso de la función ingresarEstado.
        estado = ingresarEstado(ubicacion)
        # Si el estado ingresado es igual a la palabra 'SALIR'.
        if estado == 'SALIR':
            # Se imprime un mensaje de despedida y se termina el sistema.
            print("Gracias por usar el sistema")
        # Si el estado ingresado es correcto.
        else:
            # Se imprime un divisor para mejor visualización.
            print("\n" + "V".center(100,"-"))
            # Se realiza las acciones correspondientes para la ubicacion y estado ingresados por el usuario se almacena el costo.
            costo = int(via.calcularCosto(ubicacion, estado, costo, estadoObjetivo))
            # se imprime un divisor para mejor visualización.
            print("\n" + "V".center(100,"-"))
            #para cada ubicacionSiguiente en el diccionario de estadoObjetivo.
            for ubicacionSiguiente in estadoObjetivo.keys():
                # Si la ubicacion obtenida en el bucle es diferente a la ingresada por el usuario.
                if ubicacionSiguiente != ubicacion:
                    # Se imprime la ubicación que sigue
                    print("\nLa siguiente vía es:", ubicacionSiguiente)
                    # Se ingresa el estado de la vía haciendo uso de la función ingresarEstado.
                    estado = ingresarEstado(ubicacionSiguiente)
                    # Si el estado ingresado es igual a la palabra 'SALIR'.
                    if estado == 'SALIR':
                        # Se imprime un mensaje de despedida.
                        print("Gracias por usar el sistema")
                        # Se termina el bucle para el ingreso de una ubicación valida.
                        break
                    # Si el estado ingresado es correcto pero es 1.
                    elif estado == '1':
                        #se agrega un costo adicional por moverse a la vía con tráfico.
                        costoAdicional = moverLaVía(ubicacionSiguiente)
                        #se suma el costo adicional al costo totla.
                        costo += costoAdicional
                        # Se realiza las acciones correspondientes para la ubicacion y estado indicados en el bucle.
                        costo = int(via.calcularCosto(ubicacionSiguiente, estado, costo, estadoObjetivo))
                    # Si el estado ingresado es correcto pero es 0.
                    else:
                        # Se realiza las acciones correspondientes para la ubicacion y estado indicados en el bucle.
                        costo = int(via.calcularCosto(ubicacionSiguiente, estado, costo, estadoObjetivo))
    # Se imprime el costo total.    
    print("\nEl costo total por el desalojo de todas las vías con tráfico es: ", costo, " \n")
    # Se imprime un mensaje informativo.
    print("Estados de las vías: \n")
    # Se imprime el estado objetivo de la via en cada ubicación.
    print(estadoObjetivo)
    #se imprime unos saltos de linea para mejor visualización.
    print("\n\n")
    # Se termina el bucle para el ingreso de una llave valida.

def calcularEstadoUno(ubicacion, estado, costoTotal, estadoObjetivo):
    """
    Función para determinar que hacer cuando el estado de la vía es 1.
    Parametros:
        ubicacion (str): Indica la ubicacion de la via inteligente.
        estado (str): Indica el estado de la via inteligente.
        costo (int): Indica el costo de las acciones realizadas por la via inteligente.
        llave (str): Describe si la llave se encuentra dentro del rango de accion de la via inteligente.
        estadoObjetivo (diccionario): Proporciona el estado objetivo de las habitaciones evaluadas.
    Retorna:
        costo (int): Indica el costo de las acciones realizadas por la via inteligente.
    """
    # Se asigna el nuevo estado a la via de la ubicación correspondiente.
    estadoObjetivo[ubicacion] = '0'
    # Se incrementa el costo en 1
    costoTotal += 1
    # Se imprime el estado de la via.
    print("la vía ", ubicacion, " se encuentra cerrada", "(estado ", estado, ")")
    #imprimir un mensaje que diga que se esta despejando la vía
    print("Se está despejando la vía ", ubicacion,".......")
    # Se imprime el nuevo estado de la via inteligente.
    print("El transito en la vía", ubicacion, "ha sido despejado")
    #imprimir un mensaje de cuanto cuesta despejar la via
    print("El costo por despejar la vía es de 1")
    # Se imprime el nuevo costo de la via inteligente.
    print("El costo actual es: ", costoTotal)
    print("\n" + "V".center(100,"-"))
    # Se retorna el costo actual de las acciones realizadas por la via inteligente.
    return costoTotal

def calcularEstadoDos(ubicacion, estado, costoTotal):
    """
    Función para determinar que hacer cuando el estado de la vía es 0.
    Parametros:
        ubicacion (str): Indica la ubicacion de la via inteligente.
        estado (str): Indica el estado de la via inteligente.
        costo (int): Indica el costo de las acciones realizadas por la via inteligente.
        llave (str): Describe si la llave se encuentra dentro del rango de accion de la via inteligente.
    Retorna:
        costo (int): Indica el costo de las acciones realizadas por la via inteligente.
    """
    print("\n" + "V".center(100,"-"))
    # Imprime el estado de la via.
    print("\nLa via ", ubicacion, " no presenta tráfico", "(estado ", estado, ")")
    # Se muestra un mensaje informativo de las acciones realizadas por la via inteligente.
    print("No se realiza ninguna acción por lo tanto el costo es 0")
    #Se imprime el costo actual de la via inteligente.
    print("El costo actual es: ", costoTotal)
    # Se retorna el costo actual de las acciones realizadas por la via inteligente.
    print("\n" + "V".center(100,"-"))
    return costoTotal