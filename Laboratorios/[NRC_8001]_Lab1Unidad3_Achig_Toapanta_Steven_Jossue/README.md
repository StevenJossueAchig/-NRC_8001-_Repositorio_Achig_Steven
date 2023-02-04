# Laboratorio Desarollo de un agente inteligente
PEAS y tablas de estado

Sistema que mediante el análisis, la definición de un agente inteligente, su PEAS y su tabla de estados, simula el comportamiento de una via inteligente que será capaz de anlizar diferentes vías dependiendo de eso, está despejará la via e incrementará el costo en 1 o si la via no presenta tráfico entonces no realizara ninguna acción y tampoco subirá el costo, así analizará las demás vías para saber si debe moverse o no a descongestionar las vías, por esa acción de moverse a otra via para descongestionar se aumenta el costo en 1, caso contario no se hace nada y tampoco se aumenta el costo. 


## Requisitos

Se requieren las siguientes bibliotecas:

* [os](https://pypi.org/project/memory-profiler/)

* [time](https://pyinstaller.org/en/stable/)

Si desea usar [@profile](https://pypi.org/project/memory-profiler/), ejecutar el programa desde una terminal, buscando el archivo .py y porterior ejeceutar el comando [python -m memory_profiler product.py](https://pypi.org/project/memory-profiler/), posterior haga uso del programa al momento de finalizar el programa automaticamente se capturara la complejidad de espacio de cada una de las funciones a las que se les ha agregado [@profile](https://pypi.org/project/memory-profiler/).

## Uso

```
usage: product.py [option] [datos]

C:\Users\legio\OneDrive\Escritorio\Sistema_De_Ventas_Ferretieria\code>
C:\Users\legio\OneDrive\Escritorio\Sistema_De_Ventas_Ferretieria\code>python -m memory_profiler product.py

Sistema de ventas Ferreteria: Manejo de un inventario y el proceso para ventas de una ferreteria.

Arguments:
  -datos   datos de un producto.
```

### Formato de los datos de entrada

**Nombre:** El nombre del producto solo debe hacer referencia al producto, no más especificaciones eso se ingresará en la descripción del producto.

**Fecha de caducidad:** La manera de ingresar la fecha será en el formato: **DD-MM-AA**. Examples: **24-04-2023**, **19-09-2023**

**Precio:** El precio debe ser ingresado en un formato decimal para que el precio pueda ser correctamente agregado caso contrario no se lo permitirá Ejemplos: **12.30, 56.89, 12.00**

**Cantidad:** La cantidad debe ser ingresada en el formato de un número entero, caso contrario no se lo permitirá Ejemplos: **25, 30, 100**

**Descripción:** En la descripción debe ser ingresada caracteristicas como marca, tamaño, color, entre otros aspectos relevantes para el ingreso del producto. Ejemplos: **Pintura negra Pintuco, Martillo de goma para valdosa, Destornillador punta estrella.**

En caso de usar [@profile](https://pypi.org/project/memory-profiler/) agregar en cada función encima de donde se define, para poder ejecutar el comando python -m memory_profiler product.py, caso contrario no funcionará.


## Ejemplo

```
@profile
    def listEarns(self):
        """
        Funcion para listar las ganancias
        Recibe:
            self = clase producto, un objeto
        Retorna:
            no retorna
        """
        #se imprime las ganancias totales y se redondea las ganancias a dos decimales
        print("Ganancias totales: $"+str(round(self.earns,2))+"\n")
```

```
Pintura,40,23.89,25/03/2023,Puntura color blanco marca Pintuco
```

## Licencia

Este proyecto está autorizado bajo la Licencia MIT; consulte el archivo de [Licencia](Licencia) para mas detalles.
