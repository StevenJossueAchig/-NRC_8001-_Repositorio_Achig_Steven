"""
Hallar la ptencia de un numero cualquiera
Autor:
Achig Toapanta Steven Jossue

Verisión:
VER.1.3
"""

#importamos la libreria randmos para numeros randomicos
import os
import math

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
           numero = float(numero)
           #se retorna falso porque ya no debe seguir el bucle
           return True;
        #excepsion
        except ValueError:
            #se retorna true porque el ciclo debe seguir
            return False;


def calcularPotencia():
    """
    Funcion para Calcular un numero elevado a una potencia
    Recibe:
        No recibe parametros
    Retorna:
        No retorna parametros
    """
    #variable sigue para validar el ingreso de numeros
    sigue = True
    #mientras la variable sigue sea verdadera
    while sigue == True:
        #variable numero para almacenar el numero ingresado
        numero = input("\nIngrese el numero: ")
        #variable grado para almacenar el grado de potencia
        grado = input("\nIngrese el grado de potencia: ")
        #Si validar que las variables sean solo numeros
        if validarNumero(numero)==True and validarNumero(grado)==True:
            #variable numero y grado a float
            numero = float(numero);
            grado = float(grado);
            #se calcula la potencia de un numero
            potencia = math.pow(numero, grado)
            sigue = False
        #Si no
        else:
            #imprime que solo se ingrese numeros enteros
            print("\n\nINGRESE SOLO NUMEROS POR FAVOR INTENTA DE NUEVO\n")
            #el bucle sigue
            sigue = True
    #se imprimen los datos con un mensaje
    print("\n\nEl numero", numero, "elevado a la potencia", grado, "es igual a", potencia)

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
        print("Escoja una opcion:")
        menu = """
            0. Salir
            1. Calcular la potencia de un numero.
        """
        #opcion es igual a la entrada que debemos a menu
        opcion = input(menu)
        #si la opcion es 1
        if opcion == "1":
            print("Calcular la potencia de un numero.")
            calcularPotencia()
        #sino saldra del menu y finalizara todo
        

#Se hace llamado a la funcion main delimitando el main.
if __name__ == '__main__':
    mostrar_menu()