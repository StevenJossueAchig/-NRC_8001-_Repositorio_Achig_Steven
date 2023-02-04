import big_o
import random

"""
Con el primer caracter de un arreglo de caracteres, reemplazar todos los caracteres iguales por un asterisco, menos el primer caracter

Autor:
Achig Toapanta Steven Jossue

Verisión:
VER.1.0
"""

def cambiarCaracterReptido(texto):
    """
    Funcion para cambiar el caracter repetido por un asterisco
    Recibe:
        texto: es un texto
    Retorna:
        texto: es el texto modificado
    """
    #varaible caracter que tomara el caracter de la posicion 0 que se quiera reemplazar
    caracter = texto[0]
    #se hace un recorrido por el texto
    for pivote in range(len(texto)):
        #si el caracter es igual al caracter que se quiere cambiar
        if texto[pivote] == caracter:
            #se cambia por un espacio
            texto = texto.replace(caracter, "*")
    #se retorna el texto
    return texto

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
            1. Ingresar un texto
            2. Calcular complejidad
        """
        #opcion es igual a la entrada que debemos a menu
        opcion = input(menu)
        #si la opcion es 1
        if opcion == "1":
            texto = input("Ingrese un texto: ")
            textoModificado = cambiarCaracterReptido(texto)
            print(textoModificado)
        #si la opcion es 2
        elif opcion == "2":
            print("Calcular complejidad")
            texto = input("Ingrese un texto: ")
            muestra = lambda n: texto
            best, others = big_o.big_o(cambiarCaracterReptido, muestra)
            print("La ocmplejidad es:")
            print(best) 

#Se hace llamado a la funcion main delimitando el main.
if __name__ == '__main__':
    mostrar_menu()