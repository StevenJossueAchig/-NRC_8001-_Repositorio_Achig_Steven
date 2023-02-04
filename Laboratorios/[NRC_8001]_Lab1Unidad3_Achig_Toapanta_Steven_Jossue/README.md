# Laboratorio Desarollo de un agente inteligente
PEAS y tablas de estado

Sistema que mediante el análisis, la definición de un agente inteligente, su PEAS y su tabla de estados, simula el comportamiento de una via inteligente que será capaz de anlizar diferentes vías dependiendo de eso, está despejará la via e incrementará el costo en 1 o si la via no presenta tráfico entonces no realizara ninguna acción y tampoco subirá el costo, así analizará las demás vías para saber si debe moverse o no a descongestionar las vías, por esa acción de moverse a otra via para descongestionar se aumenta el costo en 1, caso contario no se hace nada y tampoco se aumenta el costo. 


## Requisitos

Se requieren las siguientes bibliotecas:

* [os](https://docs.python.org/es/3.10/library/os.html)

* [time](https://docs.python.org/es/3.10/library/time.html?highlight=time#module-time)

Simplemente se importan las librerias ya que vienen por defecto instaladas en Python, realizar un import y el nombre de las bibliotecas.

## Uso

```
import os
import time

# Se imprime un mensaje de error.
print("\nEl estado no es correcto, Por favor intente de nuevo\n")
#se espera un segundo para que el usuario pueda leer el mensaje.
time.sleep(0.1)
#se limpia la pantalla.
os.system ("cls")
#se vuelve a imprimir el menu de opciones.
sigue=True

Arguments:
  no tiene
```

### Formato de los datos de entrada

**Ubicación:** El nombre de la via en la que se encuentra el usuario al inicio del programa **Chilibulo, Colonche, Carapungo, Pelileo**.

**Estado:** Estado de la vía en la que se encuentra, congestionada o no **0 o 1**

## Ejemplo

```
# Se imprime el menu de opciones.
print("Vías disponibles: Chilibulo, Colonche, Pelileo, Carapungo")
#se imprime la opcion de salir
print("Si desea salir del pograma ingrese en cualquier momento la palabra 'salir'\n")
# Se pide la ubicacion de la via inteligente.
ubicacionSinFormato = input("\nPor favor ingrese en que via se encuentra: ")
# Se cambia la ubicacion a mayusculas y se eliminan los espacios en blanco.
ubicacion = ubicacionSinFormato.upper().strip().replace(" ", "")
# Si la ubicacion ingresada es igual a la palabra 'SALIR'.
if ubicacion == 'SALIR':
    # Se termina el bucle para el ingreso de una ubicación valida.
    sigue=False
    #se retorna la ubicacion con el valor de salir para que el programa se cierre.
    return ubicacion
```

## Licencia

Este proyecto está autorizado bajo la Licencia MIT; consulte el archivo de [Licencia](Licencia) para mas detalles.
