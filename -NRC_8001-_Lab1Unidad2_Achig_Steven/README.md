# Laboratorio ejercicios en Python
Ejercicios en Python

Sistema para el manejo de inventario y venta los precios y cantidad de cada producto son numeros decimales y enteros respectivamente, en el caso de los demas ademas datos son cadenas de caracteres, para el ingreso de texto, cada opción lleva a una funcionalidad diferente que solventa las necesidades de una ferreteria, como la venta de productos, agregación de productos, busqueda de un producto entre otros. El esquema de negocio ha sido tomado de https://www.100plandenegocios.com/plan-de-negocios-de-una-ferreteria#descripcion


## Requisitos

Se requieren las siguientes bibliotecas:

* [memory_profiler](https://pypi.org/project/memory-profiler/)

* [PyInstaller](https://pyinstaller.org/en/stable/)

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
