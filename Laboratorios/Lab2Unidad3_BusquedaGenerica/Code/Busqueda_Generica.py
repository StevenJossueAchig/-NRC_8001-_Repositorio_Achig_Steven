import os 
import time

"""
Pseudocódigo:

funcion Busqueda-General(problema, estrategia)
						returns solución, o falla
1. inicializar el arbol de búsqueda empelando el estado inicial 
								del problema
2. loop do
3. if no hay candidatos para expansion then return falla
4. elegir un nodo hoja para expansion de acuerdo a la estrategia
5. if el nodo contiene un estado objetivo
6. 	then return la solución
7. else expandir el nodo y adicionar los nodos resultantes al arbol de búsqueda
8. end

"""


def busquedaGenerica(problema, estrategia):
    """
    Función para la búsqueda genérica para buscar la mejor ruta dependiendo de la estrategia ingresada
    Parametros:
        problema: estado final o destino al que se requiere llegar
        estretegia: función para saber según que directriz se busca la mejor ruta
    Retorna:
        solución: la solución que ha sido encontrada dependiendo de la estrategia
    """
    #definimos variables globales un grado y una etiquetas
    global graph,etiquetas
    #inicializaciones del arbol de busqueda
    solucion = []
    #lista de nodos visitados
    visitados = []
    #lista de gráfos candidatos
    candidatos = []
    #variable falla inicilizada como falsa
    falla = False
    #estado inicial del problema 
    nodo_inicial = graph.index(graph[0])
    #nodo acutal igual al noto incial
    nodo_actual = nodo_inicial
    #agregamos a la lista solución un cero.
    solucion.append(0)
    #mientras 
    while True: 
        #si no hay candidatos para expansion return falla
        #[0] -> ? 
        #[0] -> 1,2 tiene candidatos
        #[0] -> [] no tiene candidatos
        if len(graph[nodo_actual]) == 0:
            #falla ahora es veradera
            falla = True
            #terminar bucle
            break
        #se elige un nodo hoja de acuerdo al argumento estrategia
        nodo_hoja = estrategia(nodo_actual)
        #imprimimos el nodo hoja
        print(nodo_hoja)
        #se agrega el nodo escogido a la solución 
        solucion.append(int(etiquetas[nodo_hoja]))
        #se agrega el nodo a la lista de visitados
        visitados.append(int(etiquetas[nodo_hoja]))

        #si el nodo contiene el estado objetivo
        if nodo_hoja == problema:
            #terminar bucle y return solucion
            break 
        else:
            #se agrega el nodo hoja a los siguientes candidatos a visitar
            candidatos.insert(0, int(etiquetas[nodo_hoja]))
            #se expande el nodo y se adiciona los nodos hoja / hijos
            for nodo_hoja in graph[nodo_actual]:
                #se comprueba que los nodos hoja a agregar en la lista candidatos no sean visitados o sea ya un candidato
                if int(etiquetas[nodo_hoja]) not in visitados and candidatos:
                    candidatos.append(int(etiquetas[nodo_hoja]))
        #reverse de la lista candidatos para que el primer candidato siguiente pase al ultimo y poder hacer un pop de la lista
        candidatos.reverse()
        print("candidatos",candidatos)
        #pop del mayor posible candidato
        candidato = candidatos.pop()
        print("candidato", candidato)
        #el nodo actual ahora es el siguiente candidato
        nodo_actual = candidato
        #se repite el bucle
    
    #si no existio falla se retorna la solucion
    return solucion if not falla else "Solución no encontrada"

#definicion etiquetas
etiquetas = {
        "Estar_en_casa": "0",
        "Sacar_el_auto_del_garage" : "1",
        "Ir_a_la_parada_de_taxis" : "2",
        "Ir_a_la_parada_del_bus" : "3",
        "Tomar_la_mariscal_sucre" : "4",
        "Tomar_Un_taxi_al_Trabajo_De_Mi_Madre" : "5",
        #"Tomar_Un_Bus_al_Trabajo_De_Mi_Madre" : "6",
        "Tomar_la_avenida_America" : "7",
        "Llegar_al_trabajo_de_mi_madre" : "8"
    }

# ESTRATEGIA 1 -> Seguridad -> Mi estrategia es llegar por el camino que tenga mayor seguridad
#mayor costo

def estrategia_Seguridad(nodo_actual):
    """
    Función para definir la estragia de mayor seguridad
    Parametros:
        nodo actual: es el nodo en el que nos encontremos
    Retorna:
        mejor nodo: es el mejor camino que se escojera dependiendo la estraregia 
    """
    #definimos variables globales para el grafo y el costo
    global graph,cost
    #definimos los costos de las aristas este es el costo por sacar el auto del garage
    cost[(0, "Sacar_el_auto_del_garage")] = 8
    #definimos el costo de tomar la mariscal sucre
    cost[(1, "Tomar_la_mariscal_sucre")] = 8
    #definimos el costo de tomar la avenida america
    cost[(4, "Tomar_la_avenida_America")] = 8
    #definimos el costo de tomar el bus
    cost[(7, "Llegar_al_trabajo_de_mi_madre")] = 8
    #definimos el costo de ir a la parada del bus
    cost[(0, "Ir_a_la_parada_del_bus")] = 6
    #definimos el costo de tomar el bus
    cost[(3, "Tomar_Un_Bus_al_Trabajo_De_Mi_Madre")] = 3
    #definimos el costo de ir a la parada de taxis
    cost[(6, "Llegar_al_trabajo_de_mi_madre")] = 3
    #definimos el costo de ir a la parada de taxis
    cost[(0, "Ir_a_la_parada_de_taxis")] = 5
    #definimos el costo de tomar el taxi
    cost[(2, "Tomar_Un_taxi_al_Trabajo_De_Mi_Madre")] = 5
    #definimos el costo de llegar al trabajo de mi madre
    cost[(5, "Llegar_al_trabajo_de_mi_madre")] = 5
    #definimos la variable del mejor nodo como un string vacio
    mejor_nodo = ""
    #imprimimos el nodo actual en el que nos encontramos
    print("NODO ACTUAL", nodo_actual)
    #el nodo de partida sera el nodo actual tomado del grafo
    nodo_partida = graph[nodo_actual]
    #definimos el costo anterior como 0
    costo_anterior = 0
    #recorremos el nodo de partida
    for nodo_hoja in nodo_partida:
        #imprimimos el nodo hoja
        print("nodo_hoja",nodo_hoja)
        #definimos el costo como el costo del nodo actual y el nodo hoja
        costo = cost[(nodo_actual,nodo_hoja)]
        #imprimimos el costo
        print("COSTO ACTUAL", costo)
        #Imprimimos como comparamos el costo anterior con el costo del nodo
        print("comp", str(costo_anterior) + "<" + str(costo))
        #si el costo anterior es menor al costo actual
        if costo_anterior < costo:
            #imprimimos que entro
            print("entro")
            #definimos el mejor nodo como el nodo hoja
            mejor_nodo = nodo_hoja
            #definimos el costo anterior como el costo actual
            costo_anterior = costo
    #imprimimos el mejor nodo
    print("mejor nodo",mejor_nodo)
    #retornamos el mejor nodo
    return mejor_nodo

def estrategia_Precio(nodo_actual):
    """
    Función para definir la estragia de menor precio
    Parametros:
        nodo actual: es el nodo en el que nos encontremos
    Retorna:
        mejor nodo: es el mejor camino que se escojera dependiendo la estraregia 
    """
    #definimos variables globales para el grafo y el costo
    global cost
    #definimos los costos de las aristas este es el costo por sacar el auto del garage
    cost[(0, "Sacar_el_auto_del_garage")] = 8
    #definimos el costo de tomar la mariscal sucre
    cost[(1, "Tomar_la_mariscal_sucre")] = 6
    #definimos el costo de tomar la avenida america
    cost[(4, "Tomar_la_avenida_America")] = 6
    #definimos el costo de tomar el bus
    cost[(7, "Llegar_al_trabajo_de_mi_madre")] = 6
    #definimos el costo de ir a la parada del bus
    cost[(0, "Ir_a_la_parada_del_bus")] = 1
    #definimos el costo de tomar el bus
    cost[(3, "Tomar_Un_Bus_al_Trabajo_De_Mi_Madre")] = 3
    #definimos el costo de ir a la parada de taxis
    cost[(6, "Llegar_al_trabajo_de_mi_madre")] = 3
    #definimos el costo de ir a la parada de taxis
    cost[(0, "Ir_a_la_parada_de_taxis")] = 3
    #definimos el costo de tomar el taxi
    cost[(2, "Tomar_Un_taxi_al_Trabajo_De_Mi_Madre")] = 5
    #definimos el costo de llegar al trabajo de mi madre
    cost[(5, "Llegar_al_trabajo_de_mi_madre")] = 5
    #definimos la variable del mejor nodo como un string vacio
    mejor_nodo = ""
    #imprimimos el nodo actual en el que nos encontramos
    print("NODO ACTUAL", nodo_actual)
    #el nodo de partida sera el nodo actual tomado del grafo
    nodo_partida = graph[nodo_actual]
    #definimos el costo anterior como 0
    costo_anterior = 10**8
    #recorremos el nodo de partida
    for nodo_hoja in nodo_partida:
        #imprimimos el nodo hoja
        print("nodo_hoja",nodo_hoja)
        #definimos el costo como el costo del nodo actual y el nodo hoja
        costo = cost[(nodo_actual,nodo_hoja)]
        #imprimimos el costo
        print("COSTO ACTUAL", costo)
        #Imprimimos como comparamos el costo anterior con el costo del nodo
        print("comp", str(costo_anterior) + ">" + str(costo))
        #si el costo anterior es menor al costo actual
        if costo_anterior > costo:
            #imprimimos que entro
            print("entro")
            #definimos el mejor nodo como el nodo hoja
            mejor_nodo = nodo_hoja
            #definimos el costo anterior como el costo actual
            costo_anterior = costo
    #retornamos el mejor nodo
    return mejor_nodo

def estrategia_Tiempo(nodo_actual):
    """
    Función para definir la estragia de menor tiempo
    Parametros:
        nodo actual: es el nodo en el que nos encontremos
    Retorna:
        mejor nodo: es el mejor camino que se escojera dependiendo la estraregia 
    """
    #definimos variables globales para el grafo y el costo
    global cost
    #definimos los costos de las aristas este es el costo por sacar el auto del garage
    cost[(0, "Sacar_el_auto_del_garage")] = 5
    #definimos el costo de tomar la mariscal sucre
    cost[(1, "Tomar_la_mariscal_sucre")] = 3
    #definimos el costo de tomar la avenida america
    cost[(4, "Tomar_la_avenida_America")] = 3
    #definimos el costo de tomar el bus
    cost[(7, "Llegar_al_trabajo_de_mi_madre")] = 3
    #definimos el costo de ir a la parada del bus
    cost[(0, "Ir_a_la_parada_del_bus")] = 6
    #definimos el costo de tomar el bus
    cost[(3, "Tomar_Un_Bus_al_Trabajo_De_Mi_Madre")] = 6
    #definimos el costo de ir a la parada de taxis
    cost[(6, "Llegar_al_trabajo_de_mi_madre")] = 6
    #definimos el costo de ir a la parada de taxis
    cost[(0, "Ir_a_la_parada_de_taxis")] = 4
    #definimos el costo de tomar el taxi
    cost[(2, "Tomar_Un_taxi_al_Trabajo_De_Mi_Madre")] = 4
    #definimos el costo de llegar al trabajo de mi madre
    cost[(5, "Llegar_al_trabajo_de_mi_madre")] = 5
    #definimos la variable del mejor nodo como un string vacio
    mejor_nodo = ""
    #imprimimos el nodo actual en el que nos encontramos
    print("NODO ACTUAL", nodo_actual)
    #el nodo de partida sera el nodo actual tomado del grafo
    nodo_partida = graph[nodo_actual]
    #definimos el costo anterior como 0
    costo_anterior = 10**8
    #recorremos el nodo de partida
    for nodo_hoja in nodo_partida:
        #imprimimos el nodo hoja
        print("nodo_hoja",nodo_hoja)
        #definimos el costo como el costo del nodo actual y el nodo hoja
        costo = cost[(nodo_actual,nodo_hoja)]
        #imprimimos el costo
        print("COSTO ACTUAL", costo)
        #Imprimimos como comparamos el costo anterior con el costo del nodo
        print("comp", str(costo_anterior) + ">" + str(costo))
        #si el costo anterior es menor al costo actual
        if costo_anterior > costo:
            #imprimimos que entro
            print("entro")
            #definimos el mejor nodo como el nodo hoja
            mejor_nodo = nodo_hoja
            #definimos el costo anterior como el costo actual
            costo_anterior = costo
    #retornamos el mejor nodo
    return mejor_nodo

def menu():
    print("Menu:")
    print("1. Menor precio")
    print("2. Menor tiempo")
    print("3. Mayor Sguridad")
    print("4. Salir")


# main function
if __name__ == '__main__':
    # create the graph
    # edges = 9
    graph,cost = [[] for i in range(9)],{}
    # graph is a list of lists. Each element of the outer list corresponds to a node 
    # and the respective inner list holds the neighboring nodes

    # definicion grafo
    graph[0].append("Sacar_el_auto_del_garage")
    graph[0].append("Ir_a_la_parada_de_taxis")
    graph[0].append("Ir_a_la_parada_del_bus")
    graph[1].append("Tomar_la_mariscal_sucre")
    graph[2].append("Tomar_Un_taxi_al_Trabajo_De_Mi_Madre")
    graph[3].append("Tomar_Un_Bus_al_Trabajo_De_Mi_Madre")
    graph[4].append("Tomar_la_avenida_America")
    graph[5].append("Llegar_al_trabajo_de_mi_madre")
    graph[6].append("Llegar_al_trabajo_de_mi_madre")
    graph[7].append("Llegar_al_trabajo_de_mi_madre")

    # cost is a dictionary
    print(graph, cost)
    #imprimel grafo y el costo
    print(graph, "\n\n" ,cost)

    # set the goal
    problema = "Llegar_al_trabajo_de_mi_madre"

    # Inicializa la variable opción con 0
    opcion = 0

    # Ejecuta el ciclo mientras la opción sea diferente a 4
    while opcion != '4':
        # Llama a la función para imprimir el menú
        menu()
        # Lee la opción ingresada por el usuario
        opcion = input("Ingrese una opción: ")
        # Verifica si la opción es 1 y muestra un mensaje correspondiente
        if opcion == '1':
            # get the route
            #ruta = busquedaGenerica(problema, estrategia_Seguridad)
            #ruta = busquedaGenerica(problema, estrategia_Tiempo)
            ruta = busquedaGenerica(problema, estrategia_Precio)
            # print the answer
            #os.system("clear")
            print("MEJOR RUTA".center(60, "-"))
            #definimos un contador inicializado en 1
            contador = 1
            #definimos un diccionario con las etiquetas
            formato = "{numero_paso} : {ruta}"
            #para un paso en la ruta
            for paso in ruta:
                #Para una llave con su valor en las etiquetas de los items
                for key, value in etiquetas.items():
                    #si el valor es igual al paso
                    if value == str(paso):
                        #imprimimos el contador y la llave
                        print(formato.format(numero_paso = contador, ruta = key))
                #aumentamos el contador
                contador += 1
        # Verifica si la opción es 2 y muestra un mensaje correspondiente
        elif opcion == '2':
            # get the route
            #ruta = busquedaGenerica(problema, estrategia_Seguridad)
            #ruta = busquedaGenerica(problema, estrategia_Tiempo)
            ruta = busquedaGenerica(problema, estrategia_Tiempo)
            # print the answer
            #os.system("clear")
            print("MEJOR RUTA".center(60, "-"))
            #definimos un contador inicializado en 1
            contador = 1
            #definimos un diccionario con las etiquetas
            formato = "{numero_paso} : {ruta}"
            #para un paso en la ruta
            for paso in ruta:
                #Para una llave con su valor en las etiquetas de los items
                for key, value in etiquetas.items():
                    #si el valor es igual al paso
                    if value == str(paso):
                        #imprimimos el contador y la llave
                        print(formato.format(numero_paso = contador, ruta = key))
                #aumentamos el contador
                contador += 1
        # Verifica si la opción es 3 y muestra un mensaje correspondiente
        elif opcion == '3':
            # get the route
            #ruta = busquedaGenerica(problema, estrategia_Seguridad)
            #ruta = busquedaGenerica(problema, estrategia_Tiempo)
            ruta = busquedaGenerica(problema, estrategia_Seguridad)
            # print the answer
            #os.system("clear")
            print("MEJOR RUTA".center(60, "-"))
            #definimos un contador inicializado en 1
            contador = 1
            #definimos un diccionario con las etiquetas
            formato = "{numero_paso} : {ruta}"
            #para un paso en la ruta
            for paso in ruta:
                #Para una llave con su valor en las etiquetas de los items
                for key, value in etiquetas.items():
                    #si el valor es igual al paso
                    if value == str(paso):
                        #imprimimos el contador y la llave
                        print(formato.format(numero_paso = contador, ruta = key))
                #aumentamos el contador
                contador += 1
        # Verifica si la opción es 4 y muestra un mensaje correspondiente
        elif opcion == '4':
            print("Ha seleccionado la opción Salir")
        # Si la opción es diferente a 1, 2, 3 o 4, muestra un mensaje de error
        else:
            print("Opción incorrecta, por favor ingrese una opción válida")
            #se espera un segundo para que el usuario pueda leer el mensaje.
            time.sleep(0.1)
            #se limpia la pantalla.
            os.system ("cls")
            #se vuelve a imprimir el menu de opciones.

