"""
Hallar el área de un cilindro

Autor:
Achig Toapanta Steven Jossue

Verisión:
VER.1.3
"""
import math
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
        
def calcularArea():
    """
    Funcion para solicitar el radio y la altura de un cilindro
    Recibe:
        No recibe parametros
    Retorna:
        No retorna parametros
    """
    #variable sigue para validar el ingreso de numeros
    sigue = True
    #mientras la variable sigue sea verdadera
    while sigue == True:
        #Definimos la variable baseB para la base menor
        radio = input("Ingrese el radio del cilindro: ")
        #definimos la variable altura para 
        altura = input("\n\nIngrese la altura del cilindro: ")
        #Si validar que las variables sean solo numeros
        if validarNumero(radio)==True & validarNumero(altura)==True:
            #HorasTrab y CosteHora se asigna como float
            radio = float(radio);
            altura = float(altura);
            #si numero es menor o igual a cero 
            if radio <= 0 or altura <= 0 or altura<= 0:
                #imprimir el numero es invalido debe ser mayor a cero
                print("\n\nNUMERO INVALIDO", "\nComprueba que el numero ingresado sea mayor que cero")
                #el bucle sigue
                sigue = True
            #si no
            else:
                #calculamos el area
                area = 2*math.pi*radio*altura + 2*math.pi*radio**2
                #el bucle se rompe
                sigue = False
        #Si no
        else:
            #imprime que solo se ingrese numeros enteros
            print("\n\nINGRESE SOLO NUMEROS POR FAVOR INTENTA DE NUEVO\n")
            #el bucle sigue
            sigue = True
    #se imprimen los datos con un mensaje
    print("\n\nEl area de un cilindro es: ", area, "Unidades^2")

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
            1. Calcular el área de un cilindro
        """
        #opcion es igual a la entrada que debemos a menu
        opcion = input(menu)
        #si la opcion es 1
        if opcion == "1":
            print("Calcular el área de un cilindro.")
            calcularArea()
        #sino saldra del menu y finalizara todo
        elif opcion == "2":
            return
        

#Se hace llamado a la funcion main delimitando el main.
if __name__ == '__main__':
    mostrar_menu()