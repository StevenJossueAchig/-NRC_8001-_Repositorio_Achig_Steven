import big_o
import math

"""
Pedir un numero y encontrar la mayor potencia de 2 a la que se pueda dividir de manera exacta ese numero ingresado

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

def ingreso():
    """
        Funcion para ingresar el numero que se quiere analizar
        Recibe:
            No recibe
        Retorna:
            Numero: retorna el numero para analizar
        """
    #varaible repetir para repetir el bucle
    repetir = True
    #mientras la variable repetir sea verdadero
    while(repetir==True):
        #ingresamos el numero en la variable numero
        numero =input("Ingrese el numero: ")
        #si se valida y es un numero entonces
        if validarNumero(numero)==True:
            #numero se asigna como entero
            numero = int(numero)
            #Ahora si el nuero es par
            if numero%2 == 0:
                #salimos del bucle
                repetir = False
                #retornamos el numero
                return numero
            #si no es par
            else:
                #imprimir mensaje 
                print("\nEl numero debe ser par")
                #regresamos la bucle
                repetir = True
        #si no es un numero
        else:
            #mensaje de error
            ("\nIngrese solo numeros")
            #regresamos la bucle
            repetir = True

def encontrarPotencia(numero):
    """
        Funcion para encontrar la potencia, 
        Recibe:
            no recibe 
        Retorna:
            No retorna
    """
    #designamos la variable exponente como un entero que empieza en cero
    exponente = 0
    #mientras el residuo de la division entre el numero y 2 elevado a el exponente sea igual a cero
    while((numero%pow(2,exponente))==0):
        #el exponente se incrementa
        exponente = exponente+1
    #hasta que el residuo sea diferente de cero
    #y se imprime el exponente restado 1
    print(("\nLa mayor potencia de 2 es: "),exponente-1, ("es decir (2^"), exponente-1, (") "))

#@profile
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
            1. Buscar el mayor exponente de 2
            2. Calcular complejidad
        """
        #opcion es igual a la entrada que debemos a menu
        opcion = input(menu)
        #si la opcion es 1
        if opcion == "1":
            print("Encuentra el mayor exponente de 2 a la que un numero par se puede dividir de manera exacta")
            #ingresamos nuestro numero para el analisis haciendo llamado a la funcion ingreso para validar el ingreso
            numero = ingreso()
            encontrarPotencia(numero)
        #si la opcion es 2
        elif opcion == "2":
            muestra = lambda example: 26
            best, others = big_o.big_o(encontrarPotencia, muestra)
            print(best)


#Se hace llamado a la funcion main delimitando el main.
if __name__ == '__main__':
    mostrar_menu()