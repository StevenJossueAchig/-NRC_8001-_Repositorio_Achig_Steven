import os 

def busquedaGenerica(problema, estrategia):
    global graph,etiquetas
    #inicializaciones del arbol de busqueda
    solucion = []
    visitados = []
    candidatos = []
    falla = False
    #estado inicial del problema 
    nodo_inicial = graph.index(graph[0])
    nodo_actual = nodo_inicial
    solucion.append(0)
    #loop do
    while True: 
        #si no hay candidatos para expansion return falla
        #[0] -> ? 
        #[0] -> 1,2 tiene candidatos
        #[0] -> [] no tiene candidatos
        if len(graph[nodo_actual]) == 0:
            falla = True
            #terminar bucle
            break
        #se elige un nodo hoja de acuerdo al argumento estrategia
        nodo_hoja = estrategia(nodo_actual)
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
        "Tomar_Un_Bus_al_Trabajo_De_Mi_Madre" : "6",
        "Tomar_la_avenida_America" : "7",
        "Llegar_al_trabajo_de_mi_madre" : "8"
    }

# ESTRATEGIA 1 -> Seguridad -> Mi estrategia es llegar por el camino que tenga mayor seguridad
#mayor costo

def estrategia_Seguridad(nodo_actual):
    global graph,cost
    cost[(0, "Sacar_el_auto_del_garage")] = 8
    cost[(1, "Tomar_la_mariscal_sucre")] = 8
    cost[(4, "Tomar_la_avenida_America")] = 8
    cost[(7, "Llegar_al_trabajo_de_mi_madre")] = 8
    cost[(0, "Ir_a_la_parada_del_bus")] = 6
    cost[(3, "Tomar_Un_Bus_al_Trabajo_De_Mi_Madre")] = 3
    cost[(6, "Llegar_al_trabajo_de_mi_madre")] = 3
    cost[(0, "Ir_a_la_parada_de_taxis")] = 5
    cost[(2, "Tomar_Un_taxi_al_Trabajo_De_Mi_Madre")] = 5
    cost[(5, "Llegar_al_trabajo_de_mi_madre")] = 5
    
    mejor_nodo = ""
    print("NODO ACTUAL", nodo_actual)
    nodo_partida = graph[nodo_actual]
    costo_anterior = 0
    for nodo_hoja in nodo_partida:
        print("nodo_hoja",nodo_hoja)
        costo = cost[(nodo_actual,nodo_hoja)]
        print("COSTO ACTUAL", costo)
        print("comp", str(costo_anterior) + "<" + str(costo))
        if costo_anterior < costo:
            print("entro")
            mejor_nodo = nodo_hoja
            costo_anterior = costo

    print("mejor nodo",mejor_nodo)
    return mejor_nodo

def estrategia_Precio(nodo_actual):
    global cost
    cost[(0, "Sacar_el_auto_del_garage")] = 8
    cost[(1, "Tomar_la_mariscal_sucre")] = 6
    cost[(4, "Tomar_la_avenida_America")] = 6
    cost[(7, "Llegar_al_trabajo_de_mi_madre")] = 6
    cost[(0, "Ir_a_la_parada_del_bus")] = 1
    cost[(3, "Tomar_Un_Bus_al_Trabajo_De_Mi_Madre")] = 3
    cost[(6, "Llegar_al_trabajo_de_mi_madre")] = 3
    cost[(0, "Ir_a_la_parada_de_taxis")] = 3
    cost[(2, "Tomar_Un_taxi_al_Trabajo_De_Mi_Madre")] = 5
    cost[(5, "Llegar_al_trabajo_de_mi_madre")] = 5
    
    mejor_nodo = ""
    print("NODO ACTUAL", nodo_actual)
    nodo_partida = graph[nodo_actual]
    costo_anterior = 10**8
    for nodo_hoja in nodo_partida:
        print("nodo_hoja",nodo_hoja)
        costo = cost[(nodo_actual,nodo_hoja)]
        print("COSTO ACTUAL", costo)
        print("comp", str(costo_anterior) + ">" + str(costo))
        if costo_anterior > costo:
            print("entro")
            mejor_nodo = nodo_hoja
            costo_anterior = costo

    return mejor_nodo

def estrategia_Tiempo(nodo_actual):
    global cost
    cost[(0, "Sacar_el_auto_del_garage")] = 5
    cost[(1, "Tomar_la_mariscal_sucre")] = 3
    cost[(4, "Tomar_la_avenida_America")] = 3
    cost[(7, "Llegar_al_trabajo_de_mi_madre")] = 3
    cost[(0, "Ir_a_la_parada_del_bus")] = 6
    cost[(3, "Tomar_Un_Bus_al_Trabajo_De_Mi_Madre")] = 6
    cost[(6, "Llegar_al_trabajo_de_mi_madre")] = 6
    cost[(0, "Ir_a_la_parada_de_taxis")] = 4
    cost[(2, "Tomar_Un_taxi_al_Trabajo_De_Mi_Madre")] = 4
    cost[(5, "Llegar_al_trabajo_de_mi_madre")] = 5
    
    mejor_nodo = ""
    print("NODO ACTUAL", nodo_actual)
    nodo_partida = graph[nodo_actual]
    costo_anterior = 10**8
    for nodo_hoja in nodo_partida:
        print("nodo_hoja",nodo_hoja)
        costo = cost[(nodo_actual,nodo_hoja)]
        print("COSTO ACTUAL", costo)
        print("comp", str(costo_anterior) + ">" + str(costo))
        if costo_anterior > costo:
            print("entro")
            mejor_nodo = nodo_hoja
            costo_anterior = costo

    return mejor_nodo


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

    print(graph, "\n\n" ,cost)

    # set the goal
    problema = "Llegar_al_trabajo_de_mi_madre"

    # get the route
    #ruta = busquedaGenerica(problema, estrategia_Seguridad)
    #ruta = busquedaGenerica(problema, estrategia_Tiempo)
    ruta = busquedaGenerica(problema, estrategia_Precio)
    # print the answer
    #os.system("clear")
    print("MEJOR RUTA".center(60, "-"))

    contador = 1
    formato = "{numero_paso} : {ruta}"
    for paso in ruta:
        for key, value in etiquetas.items():
            if value == str(paso):
                print(formato.format(numero_paso = contador, ruta = key))
        contador += 1

