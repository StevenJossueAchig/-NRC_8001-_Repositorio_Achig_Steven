"""
Ingresar un valor en dolares y transformar a euros y yenes
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


def transformarDolares():
    """
    Funcion para Ingresar un valor en dolares y transformar a euros y yenes
    Recibe:
        No recibe parametros
    Retorna:
        No retorna parametros
    """
    #variable sigue para validar el ingreso de numeros
    sigue = True
    #mientras la variable sigue sea verdadera
    while sigue == True:
        #variable dolar para ingresar el valor en dolares
        dolar = input("\nIngrese el valor en dolares: ")
        #Si validar que las variables sean solo numeros
        if validarNumero(dolar)==True:
            #variable dolar a float
            dolar = float(dolar);
            #si numero es menor a cero 
            if dolar <= 0:
                #imprimir el numero es invalido debe ser mayor a cero
                print("\n\nNUMERO INVALIDO", "\nComprueba que el numero ingresado sea mayor de cero")
                sigue = True
            #si no
            else:
                euro = dolar * 0.9462
                yenes = dolar * 130.856
                sigue = False
        #Si no
        else:
            #imprime que solo se ingrese numeros enteros
            print("\n\nINGRESE SOLO NUMEROS POR FAVOR INTENTA DE NUEVO\n")
            #el bucle sigue
            sigue = True
    #se imprimen los datos con un mensaje
    print("\n\nEl valor en dolares es: ", dolar, "\nEl valor en euros es: ", euro, "\nEl valor en yenes es: ", yenes)

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
            1. Ingresar un valor en dolares y transformar a euros y yenes
        """
        #opcion es igual a la entrada que debemos a menu
        opcion = input(menu)
        #si la opcion es 1
        if opcion == "1":
            print("Ingresar un valor en dolares y transformar a euros y yenes")
            transformarDolares()
        #sino saldra del menu y finalizara todo
        

#Se hace llamado a la funcion main delimitando el main.
if __name__ == '__main__':
    mostrar_menu()