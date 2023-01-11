"""
Preguntar al usuario su nombre y saludarlo
Autor:
Achig Toapanta Steven Jossue

Verisión:
VER.1.3
"""


def preguntarNombre():
    """
    Funcion para Preguntar al usuario su nombre y saludarlo
    Recibe:
        No recibe parametros
    Retorna:
        No retorna parametros
    """
    nombre = input("Ingrese su nombre: ")
    print("hola como estas", nombre)

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
            1. Preguntar al usuario su nombre y saludarlo
        """
        #opcion es igual a la entrada que debemos a menu
        opcion = input(menu)
        #si la opcion es 1
        if opcion == "1":
            print("Preguntar al usuario su nombre y saludarlo")
            preguntarNombre()
        #sino saldra del menu y finalizara todo
        

#Se hace llamado a la funcion main delimitando el main.
if __name__ == '__main__':
    mostrar_menu()