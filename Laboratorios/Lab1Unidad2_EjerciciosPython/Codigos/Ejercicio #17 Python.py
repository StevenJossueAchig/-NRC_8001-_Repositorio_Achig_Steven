"""
ingresar calificaciones de cinco materias y cacular el total, el promedio y el porcentaje
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


def calcularPromedios():
    """
    Funcion para ingresar calificaciones de cinco materitotal, el promedio y el porcentaje
    Recibe:
        No recibe parametros
    Retorna:
        No retorna parametros
    """
    #variable sigue para validar el ingreso de numeros
    sigue = True
    #mientras la variable sigue sea verdadera
    nota1 = input("\n\nIngrese la nota de la primera materia: ")
    nota2 = input("\n\nIngrese la nota de la segunda materia: ")
    nota3 = input("\n\nIngrese la nota de la tercera materia: ")
    nota4 = input("\n\nIngrese la nota de la cuarta materia: ")
    nota5 = input("\n\nIngrese la nota de la quinta materia: ")
    #Si validar que las variables sean solo numeros
    if validarNumero(nota1)==True and validarNumero(nota2)==True and validarNumero(nota3)==True and validarNumero(nota4)==True and validarNumero(nota5)==True:
        #base y altura de un triangulo a float
        nota1 = float(nota1);
        nota2 = float(nota2);
        nota3 = float(nota3);
        nota4 = float(nota4);
        nota5 = float(nota5);
        #si numero es menor o igual a cero 
        if nota1 < 0 or nota2 < 0 or nota3 < 0 or nota4 < 0 or nota5 < 0:
            #imprimir el numero es invalido debe ser mayor a cero
            print("\n\nNUMERO INVALIDO", "\nComprueba que el numero ingresado sea mayor o igual que cero")
            #el bucle sigue
            sigue = True
        #si no
        else:
            #se calcula el promedio
            promedio = (nota1 + nota2 + nota3 + nota4 + nota5) / 5
            #se calcula el porcentaje
            porcentaje = (promedio * 100) / 20
            #se imprime el promedio y el porcentaje
            print("\n\nEl promedio es: ", promedio, "\nEl porcentaje es: ", porcentaje)
            #el bucle no sigue
            sigue = False


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
            1. ingresar calificaciones de cinco materitotal, el promedio y el porcentaje
        """
        #opcion es igual a la entrada que debemos a menu
        opcion = input(menu)
        #si la opcion es 1
        if opcion == "1":
            print("ingresar calificaciones de cinco materitotal, el promedio y el porcentaje.")
            calcularPromedios()
        #sino saldra del menu y finalizara todo
        

#Se hace llamado a la funcion main delimitando el main.
if __name__ == '__main__':
    mostrar_menu()