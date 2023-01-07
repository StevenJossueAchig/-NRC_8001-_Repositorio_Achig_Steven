"""
Ingresar la longitud en cm y convertirla en metro y kilometro
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


def transformarUnidades():
    """
    Funcion para Ingresar la longitud en cm y convertirla en metro y kilometro
    Recibe:
        No recibe parametros
    Retorna:
        No retorna parametros
    """
    #variable sigue para validar el ingreso de numeros
    sigue = True
    #mientras la variable sigue sea verdadera
    while sigue == True:
        #variable catetoUno para almacenar el cateto uno
        centimetro = input("\n\nIngrese la longitud en centimetros: ")
        #Si validar que las variables sean solo numeros
        if validarNumero(centimetro)==True:
            #variable centimetro para almacenar float
            centimetro = float(centimetro);
            #si numero es menor o igual a cero 
            if centimetro == 0:
                #imprimir el numero es invalido debe ser mayor a cero
                print("\n\nNUMERO INVALIDO", "\nComprueba que el numero ingresado sea diferente de cero")
                sigue = True
            #si no
            else:
                #transformar centimetro a metro
                metro = centimetro / 100
                #transformar centimetro a kilometro
                kilometro = centimetro / 100000
                #el bucle se rompe
                sigue = False
        #Si no
        else:
            #imprime que solo se ingrese numeros enteros
            print("\n\nINGRESE SOLO NUMEROS POR FAVOR INTENTA DE NUEVO\n")
            #el bucle sigue
            sigue = True
    #se imprimen los datos con un mensaje
    print("\n\nEl valor ingresado en centimetros pasados a metros es: ", metro)
    print("\n\nEl valor ingresado en centimetros pasados a kilometros es: ", kilometro)


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
            1. Ingresar la longitud en cm y convertirla en metro y kilometro.
        """
        #opcion es igual a la entrada que debemos a menu
        opcion = input(menu)
        #si la opcion es 1
        if opcion == "1":
            print("Ingresar la longitud en cm y convertirla en metro y kilometro.")
            transformarUnidades()
        #sino saldra del menu y finalizara todo
        

#Se hace llamado a la funcion main delimitando el main.
if __name__ == '__main__':
    mostrar_menu()