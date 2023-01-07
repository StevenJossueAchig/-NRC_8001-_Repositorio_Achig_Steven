"""
Encontrar el diametro, la circunferencia y el area del circulo
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


def calcularDatos():
    """
    Funcion para Encontrar el diametro, la circunferencia y el area del circulo
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
        radio = input("\n\nIngrese el radio de la circunferencia: ")
        #Si validar que las variables sean solo numeros
        if validarNumero(radio)==True:
            #catetos del circulo se convierte a flotante
            radio = float(radio);
            #si numero es menor o igual a cero 
            if radio <= 0:
                #imprimir el numero es invalido debe ser mayor a cero
                print("\n\nNUMERO INVALIDO", "\nComprueba que el numero ingresado sea mayor que cero")
                #el bucle sigue
                sigue = True
            #si no
            else:
                #calculamos el area del circulo
                circuferencia = 2*math.pi*radio
                area = math.pi*radio**2
                diametro = 2*radio
                #el bucle se rompe
                sigue = False
        #Si no
        else:
            #imprime que solo se ingrese numeros enteros
            print("\n\nINGRESE SOLO NUMEROS POR FAVOR INTENTA DE NUEVO\n")
            #el bucle sigue
            sigue = True
    #se imprimen los datos con un mensaje
    print("\nla circunferencia es: ", circuferencia)
    print("\nel area es: ", area)
    print("\nel diametro es: ", diametro)


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
            1. Encontrar el diametro, la circunferencia y el area del circulo
        """
        #opcion es igual a la entrada que debemos a menu
        opcion = input(menu)
        #si la opcion es 1
        if opcion == "1":
            print("Encontrar el diametro, la circunferencia y el area del circulo.")
            calcularDatos()
        #sino saldra del menu y finalizara todo
        

#Se hace llamado a la funcion main delimitando el main.
if __name__ == '__main__':
    mostrar_menu()