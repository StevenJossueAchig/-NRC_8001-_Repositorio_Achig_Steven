import big_o
import random

"""
Pedir el numero de tamanio para un arreglo el cual cuando se requiera consultar se sumaran todos sus elementos los numeros seran ingresados de manera randomic

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

def consulta():
    sigue = True
    while(sigue==True):
        tamanio = input("Ingrese el tamaño del arreglo: ")
        if validarNumero(tamanio) == True:
            if int(tamanio) > 0:
                arreglo = []
                for i in range(int(tamanio)):
                    arreglo.append(random.randint(1, 100))
                print(arreglo)
                suma = 0
                for i in range(len(arreglo)):
                    suma += arreglo[i]
                print("La suma de todos los elementos del arreglo es: ", suma)
                sigue = False
            else:
                print("\nEl tamaño del arreglo debe ser mayor a 0")
                sigue = True
        else:
            sigue = True


#Se hace llamado a la funcion main delimitando el main.
if __name__ == '__main__':
    consulta()

    