import big_o
import random

"""
Encontrar el primer elemento que se repite en una cadena de numeros
Calcular el total de la factura ingresando la hora de entrad y salida (HH:MM) con horas y minutos.

Autor:
Achig Toapanta Steven Jossue

Verisión:
VER.1.3
"""

def validarNumero(numero):
        """
        Funcion para validar el ingreso de solo numeros
        Recibe:
            numero: es un numero
        Retorna:
            verdadero o falso dependiendo de si es o no un numero
        """
        try:
           #la variable numero se asgina a un entero
           numero = int(numero)
           #se retorna falso porque ya no debe seguir el bucle
           return True;
        #excepsion
        except ValueError:
            #imprimir intente de nuevo
            print("\nAsegurate de ingresar solo numeros")
            #se retorna true porque el ciclo debe seguir
            return False;

def generarArreglo(tamanio):
    sigue = True
    while(sigue==True):
        if validarNumero(tamanio) == True:
            if int(tamanio) > 0:
                arreglo = []
                for i in range(int(tamanio)):
                    arreglo.append(random.randint(1, 10))
                    sigue = False
                    print(arreglo)
                    return arreglo
            else:
                print("\nEl tamaño del arreglo debe ser mayor a 0")
                sigue = True
        else:
            sigue = True


def encontrarRepetido(numero):
    numeros = generarArreglo(numero)
    if len(numeros) == len(set(numeros)):
        print("No hay elementos repetidos")
    else:
        for i in numeros:
            if numeros.count(i) > 1:
                print("El primer elemento repetido es: ", i)
                break

#Funcion menu para hacer el llamado las funciones preguntar
def mostrar_menu():
    """
    Funcion para mostrar un menu de opciones para salir o usar el programa
    Recibe:
        No recibe parametros
    Retorna:
        No retorna 
    """
    #Generamos una variable para almacenar la opcion
    opcion = ""
    #mientras la opcion sea diferente de 2
    while opcion != "0":
        #menu se ejcutara
        print("\nEscoja una opcion:")
        menu = """
            0. Salir
            1. Encontrar el repetido
            2. Calcular complejidad
        """
        #opcion es igual a la entrada que debemos a menu
        opcion = input(menu)
        #si la opcion es 1
        if opcion == "1":
            print("Primer elemento reptido")
            numero = input("Ingrese el tamaño del arreglo: ")
            if validarNumero(numero) == True:
                if int(numero) > 0:
                    encontrarRepetido(numero)
                else:
                    print("\nEl tamaño del arreglo debe ser mayor a 0")
        #si la opcion es 2
        elif opcion == "2":
            muestra = lambda n: 5
            best, others = big_o.big_o(encontrarRepetido(), muestra)
            print(best) 

#Se hace llamado a la funcion main delimitando el main.
if __name__ == '__main__':
    mostrar_menu()