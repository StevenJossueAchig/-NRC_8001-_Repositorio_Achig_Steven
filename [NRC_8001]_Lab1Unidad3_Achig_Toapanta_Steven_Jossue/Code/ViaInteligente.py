#se importa el modulo funciones para poder utilizar sus funciones
import funciones

class Via_Inteligente:
    """
    Esta clase representa a una via inteligente la cual tiene un estado, una ubicacion, una llave y un costo, a traves de los cuales se puede desalojar o cerrar la via.
    Atributos:
        No posee atributos.
    Métodos:
        calcularCosto(self,ubicacion, estado, costo, llave, estadoObjetivo)
    """
    def calcularCosto(self,ubicacion, estado, costo, estadoObjetivo):
        """
        Este método define la ubicacion, el estado, el costo y la llave de la via inteligente, estos parametros serviran para realizar el análisis correspondiente para saber si se debe desalojar o no la via.

        Parametros:
            ubicacion (str): Indica la ubicacion de la via inteligente.
            estado (str): Indica el estado de la via inteligente.
            costo (int): Indica el costo de las acciones realizadas por la via inteligente.
            llave (str): Describe si la llave se encuentra dentro del rango de accion de la via inteligente.
            estadoObjetivo (diccionario): Proporciona el estado objetivo de las habitaciones evaluadas.
        Retorna:
            costo: Retorna el costo total de las acciones realizadas por la via inteligente.
        """
        # Se asigna el ubicación de la via.
        self.ubicacion = ubicacion
        # Se asigna el estado de la via.
        self.estado = estado
        # Se asigna el costo actual que sera usado para almacenar el valor de las acciones como despejar.
        self.costo = costo
        # Si el estado de la via inteligente es cerrada.
        if(estado == '1'):
            # Se llama a la función calcularEstadoUno() del modulo funciones como se sabe el estado uno quiere decir cerrado o congestionado.
            return funciones.calcularEstadoUno(ubicacion, estado, costo, estadoObjetivo)
        # Si el estado de la via inteligente es sin tráfico.
        else:
            # Se llama a la función calcularEstadoDos() del modulo funciones como se sabe el estado dos quiere decir abierto o sin tráfico.
            return funciones.calcularEstadoDos(ubicacion, estado, costo)
