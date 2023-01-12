import big_o

"""
Pedir la hora de ingreso y salida a un parqueadero donde la entrada cuest 2, la primera hora 3 y las siguientes horas cuesta 4 cada una.
Calcular el total de la factura ingresando la hora de entrad y salida (HH:MM) con horas y minutos.

Autor:
Achig Toapanta Steven Jossue

Verisión:
VER.1.3
"""

"""
x = lambda a: a + 10
print (x(5))

def myfunc(x):
    TOdo lo que se hace en la funcion
    return x + 10

muestra = lambda example: 13, 15, 16, 45
best, others = big_o.big_o(calcularFactura, muestra)
print(best)

x = lambda a, b: a * b
print(x(5, 6))
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

def imprimirFactura(pagoEntrada, primeraHora, horasPosteriores, total, totalHoras):
    """
        imprimir la factura y el numero de horas que estuvo en el parquedero
        Recibe:
            numero: es un numero
        Retorna:
            verdadero o falso dependiendo de si es o no un numero
        """
    #imprimir un formato de la factura total
    print("Estuvo durante: ", totalHoras, " horas")
    print("\n--------------------FACTURA----------------")
    print("Pago de entrada es: ", pagoEntrada)
    print("Pago de la primera hora es: ", primeraHora)
    print("Pago de las horas posteriores es: ", horasPosteriores)
    print("El total de la factura es: ", total)



def calcularFactura(horaEntrada, minutoEntrada, horaSalida, minutoSalida):
    """
        Funcion para validar el ingreso de solo numeros
        Recibe:
            horaEntrada: horas de entrada 
            minutoEntrada:minutos de entrada
            horaSalida: hora de salida 
            ninutosSalida: minutos de salida
        Retorna:
            No retorina parametros
        """
    print("\n--------------------CALCULAR FACTURA----------------")
    #variable para el costo de entrada 
    pagoEntrada = 2
    #variable para el costo de la primera hora
    primeraHora = 3
    #variable para el costo de 2 horas en adelante c/d
    horasPosteriores = 4
    #si las horas de entrada son iguales que las de salida
    if horaEntrada == horaSalida:
        #el total es igual solo a la entrada + el pago de la primera hora
        total = pagoEntrada + primeraHora
        #total de horas permanecidas en el parqueadero
        totalHoras = horaSalida - horaEntrada
        #llamado la funcion imprimir factura
        imprimirFactura(pagoEntrada, primeraHora, horasPosteriores, total, totalHoras)
    else:
        #si los minutos de entrada son menores que los de salida
        if minutoEntrada < minutoSalida:
            #total de horas permanecidas en el parqueadero
            totalHoras = horaSalida - horaEntrada + 1
            #el total es igual a la entrada + la primera hora + las horas posteriores
            total = pagoEntrada + primeraHora + (horaSalida - horaEntrada) * horasPosteriores
            #llamado la funcion imprimir factura
            imprimirFactura(pagoEntrada, primeraHora, horasPosteriores, total, totalHoras)
        #si los minutos de entrada son mayores que los de salida
        elif minutoEntrada > minutoSalida:
            #el total es igual a la entrada + la primera hora + las horas posteriores
            total = pagoEntrada + primeraHora + (horaSalida - horaEntrada - 1) * horasPosteriores
            #total de horas permanecidas en el parqueadero
            totalHoras = horaSalida - horaEntrada
            #llamado la funcion imprimir factura
            imprimirFactura(pagoEntrada, primeraHora, horasPosteriores, total, totalHoras)
        #si los minutos de entrada son iguales que los de salida
        elif minutoEntrada == minutoSalida:
            #si la diferencia de horas es igual a 1
            if horaSalida - horaEntrada == 1:
                #el total es igual solo a la entrada + el pago de la primera hora
                total = pagoEntrada + primeraHora
            #si la diferencia de horas es mayor a 1
            else:
                #el total es igual a la entrada + la primera hora + las horas posteriores
                total = pagoEntrada + primeraHora + (horaSalida - horaEntrada - 1) * horasPosteriores
            #total de horas permanecidas en el parqueadero
            totalHoras = horaSalida - horaEntrada
            #llamado la funcion imprimir factura
            imprimirFactura(pagoEntrada, primeraHora, horasPosteriores, total, totalHoras)


def ingreso():
    """
        Funcion para el ingreso de las horas y minutos de salida y entrada
        Recibe:
            No recibe parametros
        Retorna:
            No retorna 
        """
    #variable para repetir mientras sea verdadero
    repetir = True
    #mientras repetir sea verdadero
    while(repetir == True):
        #variable para alamcenar la hora de entrada
        horaEntrada = input("\nIngrese la hora de entrada: ")
        #variable para alamcenar los minutos de entrada
        minutoEntrada = input("Ingrese los minutos de entrada: ")
        #variable para alamcenar la hora de salida
        horaSalida = input("\nIngrese la hora de salida: ")
        #variable para alamcenar los minutos de salida
        minutoSalida = input("Ingrese los minutos de salida: ") 
        #se valida que los datos ingresados sean numeros
        if validarNumero(horaEntrada) == True and validarNumero(minutoEntrada) == True and validarNumero(horaSalida) == True and validarNumero(minutoSalida) == True:
            #se convierten los datos ingresados a enteros
            horaEntrada = int(horaEntrada)
            minutoEntrada = int(minutoEntrada)
            horaSalida = int(horaSalida)
            minutoSalida = int(minutoSalida)
            #se valida que las horas y minutos esten dentro del rango de horas y minutos (0 a 23 y 0 a 59)
            if horaEntrada >= 0 and horaEntrada <= 23 and horaSalida >= 0 and horaSalida <= 23 and minutoEntrada >= 0 and minutoEntrada <= 59 and minutoSalida >= 0 and minutoSalida <= 59:
                #se valida que la hora de entrada sea menor que la hora de salida
                if horaEntrada <= horaSalida:
                    #se llama a la funcion calcularFactura
                    calcularFactura(horaEntrada, minutoEntrada, horaSalida, minutoSalida)
                    #se cambia el valor de repetir a falso para salir del ciclo
                    repetir = False
                #si la hora de entrada es mayor que la hora de salida
                else:
                    #se imprime el mensaje
                    print("\nLa hora de entrada debe ser menor que la hora de salida")
                    #se cambia el valor de repetir a verdadero para seguir en el ciclo
                    repetir = True
            #si las horas o minutos no estan dentro del rango
            else:
                #se imprime el mensaje
                print("\nrecuerde que las horas van de 0 a 23 y los minutos de 0 a 59")
                #se cambia el valor de repetir a verdadero para seguir en el ciclo
                repetir = True


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
            1. Calcular Factura
            2. Calcular complejidad
        """
        #opcion es igual a la entrada que debemos a menu
        opcion = input(menu)
        #si la opcion es 1
        if opcion == "1":
            print("Calcular Factura")
            #hacemos la llamada a la variable ingreso
            ingreso()
        #si la opcion es 2
        elif opcion == "2":
            muestra = lambda a, b, c, d: 14, 15, 16 , 17
            best, others = big_o.big_o(calcularFactura, muestra)
            print(best) 

#Se hace llamado a la funcion main delimitando el main.
if __name__ == '__main__':
    mostrar_menu()
    
    