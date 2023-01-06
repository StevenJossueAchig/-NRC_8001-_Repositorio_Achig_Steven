"""
Dadas dos longitudes ingresadas por el usuario que corresponden a los lados de un rectángulo,
calcular el perímetro y el área del mismo.

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
        

def calcularArea(base, altura):
    """
    Funcion para calcular el area recibiendo la base y la altura
    Recibe:
        Base
        Altura
    Retorna:
        Area
    """
    #Definimos que la variable area es igual a la base por la altura
    area = base*altura
    #Retornamos el area
    return area

def calcularPerimetro(base, altura):
    """
    Funcion para calcular el perimetro recibiendo la base y la altura
    Recibe:
        Base
        Altura
    Retorna:
        Perimetro
    """
    #Definimos al perimetro como la suma de los dobles de la base y la altura asi servira inlcusive para un cuadrado
    perimetro = 2*(base+altura)
    #retornamos el perimetro
    return perimetro

def pedirLongitudes():
    """
    Funcion para solicitar la dos longitudes de un rectangulo y calcular su area y su perimetro
    Recibe:
        No recibe parametros
    Retorna:
        No retorna parametros
    """
    #variable sigue para validar el ingreso de numeros
    sigue = True
    #mientras la variable sigue sea verdadera
    while sigue == True:
        #definimos la variable LongitudA para almacenar el valor de la primera longitud
        longitudA = input("\n\nIngrese la primera longitud: ")
        #definimos la variable LongitudB para almacenar el valor de la segunda longitud
        longitudB = input("Ingrese la segunda longitud: ")
        #Validamos que ambas longitudes sean numeros
        if validarNumero(longitudA)==True & validarNumero(longitudB)==True:
            #LongitudA y longitudB se asignan como  flotantes
            longitudA = float(longitudA);
            longitudB = float(longitudB);
            #si las variables son menores o igual a cero 
            if longitudA <= 0 or longitudB <= 0:
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
            #imprime que solo se ingrese numeros 
            print("\n\nINGRESE SOLO NUMEROS POR FAVOR INTENTA DE NUEVO\n")
            #el bucle sigue
            sigue = True
    #Se asigna la varible unidad para las longitudes preguntando al usuario
    unidad = input("En que unidades estan las longitudes (metros, kilometros, ...)")
    #Hacemos el llamado a la funcion area y enviamos los parametros longitudA y longitudB
    print("el area del rectangulo es",calcularArea(longitudA, longitudB), unidad, "^2")
    #hacemos el llamado ala funcion calcularPerimetro y enviamos los parametros longitudA y longitudB
    print("el perimetro del rectangulo es: ", calcularPerimetro(longitudA,longitudB), unidad)

def mostrar_menu():
    """
    Funcion para validar el ingreso de los numeros de los elementos
    Recibe:
        numero: es el numero de elementos debe ser un entero
    Retorna:
        verdadero o falso dependiendo de si es o no un numero entero
    """
    #Generamos una variable para almacenar la opcion
    opcion = ""
    #mientras la opcion sea diferente de 2
    while opcion != "0":
        #menu se ejcutara
        print("Escoja una opcion:\n\n")
        menu = """
            0. Salir
            1. Pedir dos longitudes
        """
        #opcion es igual a la entrada que debemos a menu
        opcion = input(menu)
        #si la opcion es 1
        if opcion == "1":
            print("Pedir dos longitudes al usuario.")
            pedirLongitudes();
        #sino saldra del menu y finalizara todo
        elif opcion == "2":
            return
        

#Se hace llamado a la funcion main delimitando el main.
if __name__ == '__main__':
    mostrar_menu()