"""
Ingresar un valor en libras y transformarlo a kilogramos y gramos
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


def transformarLibras():
    """
    Funcion para Transformar libras a kilogramos y gramos
    Recibe:
        No recibe parametros
    Retorna:
        No retorna parametros
    """
    #variable sigue para validar el ingreso de numeros
    sigue = True
    #mientras la variable sigue sea verdadera
    while sigue == True:
        #variable libras para almacenar el ingreso de libras
        libras = input("\nIngrese el valor en libras: ")
        #Si validar que las variables sean solo numeros
        if validarNumero(libras)==True:
            #variable libras a float
            libras = float(libras);
            #si numero es menor o igual a cero 
            if libras <= 0:
                #imprimir el numero es invalido debe ser mayor a cero
                print("\n\nNUMERO INVALIDO", "\nComprueba que el numero ingresado sea diferente de cero")
                sigue = True
            #si no
            else:
                #se transforma a kilogramos y gramos
                kilogramos = libras * 0.453592
                gramos = libras * 453.592
                sigue = False
        #Si no
        else:
            #imprime que solo se ingrese numeros enteros
            print("\n\nINGRESE SOLO NUMEROS POR FAVOR INTENTA DE NUEVO\n")
            #el bucle sigue
            sigue = True
    #se imprimen los datos con un mensaje
    print("\n\nEl valor en kilogramos es: ", kilogramos, "\nEl valor en gramos es: ", gramos)

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
            1. Transformar libras a kilogramos y gramos
        """
        #opcion es igual a la entrada que debemos a menu
        opcion = input(menu)
        #si la opcion es 1
        if opcion == "1":
            print("Transformar libras a kilogramos y gramos.")
            transformarLibras()
        #sino saldra del menu y finalizara todo
        

#Se hace llamado a la funcion main delimitando el main.
if __name__ == '__main__':
    mostrar_menu()