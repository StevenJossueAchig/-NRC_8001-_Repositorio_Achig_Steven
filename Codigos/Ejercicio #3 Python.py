"""
Hallar el área de un trapezoide.

Autor:
Achig Toapanta Steven Jossue

Verisión:
VER.1.3
"""

#importamos la libreria randmos para numeros randomicos
import os

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
        
def preguntar():
    """
    Funcion para solicitar el numero de horas trabajadas, el coste por hora y la moneda en que cobra.
    Recibe:
        No recibe parametros
    Retorna:
        No retorna parametros
    """
    #variable sigue para validar el ingreso de numeros
    sigue = True
    #mientras la variable sigue sea verdadera
    while sigue == True:
        #definimos la variable HorasTrab para el valor de las horas trabajadas de una persona
        HorasTrab = input("\n\nIngrese el numero de horas trabajadas: ")
        #Definimos la variable CosteHora para almacenar el valor del costo por hora de una persona
        CosteHora = input("Ingrese el coste por hora: ")
        #Si validar numero es verdadero
        if validarNumero(HorasTrab)==True & validarNumero(CosteHora)==True:
            #HorasTrab y CosteHora se asigna como float
            HorasTrab = float(HorasTrab);
            CosteHora = float(CosteHora);
            #si numero es menor o igual a cero 
            if HorasTrab <= 0 or CosteHora <= 0:
                #imprimir el numero es invalido debe ser mayor a cero
                print("\n\nNUMERO INVALIDO", "\nComprueba que el numero ingresado sea mayor que cero")
                #el bucle sigue
                sigue = True
            #si no
            else:
                #el bucle se rompe
                sigue = False
        #Si no
        else:
            #imprime que solo se ingrese numeros enteros
            print("\n\nINGRESE SOLO NUMEROS POR FAVOR INTENTA DE NUEVO\n")
            #el bucle sigue
            sigue = True
    #Definimos la variable moneda para saber en que moneda se cobra el tiempo trabajado
    Moneda = input("Ingrese la moneda en que gana: ")
    #se imprimen los datos con un mensaje
    print("\n\nLas horas trabajadas son: ", HorasTrab, "horas")
    print("El costo por hora es: ", CosteHora, " ", Moneda)

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
            1. Calcular el área de un trapezoide
        """
        #opcion es igual a la entrada que debemos a menu
        opcion = input(menu)
        #si la opcion es 1
        if opcion == "1":
            print("Preguntar al usuario por el número de horas trabajadas y el coste por hora.")
            preguntar()
        #sino saldra del menu y finalizara todo
        elif opcion == "2":
            return
        

#Se hace llamado a la funcion main delimitando el main.
if __name__ == '__main__':
    mostrar_menu()