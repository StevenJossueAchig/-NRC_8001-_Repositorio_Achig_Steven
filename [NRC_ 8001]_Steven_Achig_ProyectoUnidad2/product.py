#Declaración de clase
#Componentes abreviaturas claves: def, __init__, self
#En todos los metodos, tiene que tener como arg el self (primero)
import random

class Product:
    """
    Clase Producto para la implementacion de los productos
    Atributos:
        name: nombre del producto
        ID: id del producto para la venta
        stock: cantidad del producto presente
        price: precio del producto
        expirationDate: fecha de expiracion
        description: breve descripcion del sistema
    Metodos:
        constructor:
        validarStockFormatNumbre:
        validatePriceFormatNumberDecimal: 
    """
    #constructor = __init__ de la clase Product
    def __init__(self, name, stock, price, expirationDate, description):
        """
        Constructor para inicializa la clase ferreteria
        Recibe:
            self = clase producto, un objeto
            name = nombre de la ferreteria
        Retorna:
            no retorna
        """
        #definimos las variables de los atributos para el constructor
        self.ID = random.randint(10001,99999)
        self.name = name
        self.stock = stock
        self.price = price
        self.expirationDate = expirationDate
        self.description = description

    def validateStockFormatNumber(self):
        """
        Funcion para validar si el stock es un numero, perteneciente a la clase product
        Recibe:
            self = classe producto, un objeto
        Retorna:
            verdadero o falso dependiendo de si es o no un numero
        """
        #si el stock del obejto self es numerico
        if self.stock.isnumeric():
            #transformamos el stock de self en entero
            self.stock = int(self.stock)
            #retornamos verdadero
            return True
        #si el stock ingresado no es numerico
        else:
            #se imprime un mensaje que diga que la cantidad no esta en el formato numerico
            print("\n¡La cantidad del producto no esta en formato numérico.!\n")
            #retorna un falso
            return False

    def validatePriceFormatNumberDecimal(self):
        """
        Funcion para validar si el precio es un numero, perteneciente a la clase product
        Recibe:
            self = classe producto, un objeto
        Retorna:
            verdadero o falso dependiendo de si es o no un numero
        """
        #try condicion para validar un numero decimal
        try:
            #usando el precio del objeto enviado analizar si es flotante
            self.price = float(self.price)
            #retorna verdadero si es un decimal
            return True
        #excepcion para el valor erroneo
        except ValueError:
            #imprimir que el precio no esta en formato decimal
            print("\n¡El precio del producto no esta en formato numérico decimal.!\n")
            #retorna falso
            return False

#Taladro;100;10.80;No aplica;De acero resistente incluido tuercas
#Pintura;100;35.10;01/01/2024;Pintuco de color blanco,1L

class HardwareStore:
    """
    Clase Hardwarstore o Ferreteria para la composicion de productos
    Atributos:
        name = nombre de la ferreteria
    Metodos:
        sellProduct:
    """
    #arreglo productos para almacenar los productos
    products = []
    #variable para las ganancias
    earns = 0

    def __init__(self, name):
        """
        Constructor para inicializa la clase ferreteria
        Recibe:
            self = clase producto, un objeto
            name = nombre de la ferreteria
        Retorna:
            no retorna
        """
        self.name = name

    def sellProduct(self):
        """
        Funcion para vender un producto
        Recibe:
            self = clase producto, un objeto
        Retorna:
            no retorna
        """
        #hacemos el llamado a la funcion listar productos para ver los productos que existen
        self.listProducts()
        #declaramos la variable idProducto para que se ingrese el id del producto que se escoja para vender
        idProducto = input("Ingrese el ID del producto a vender:")
        #variable existID para preguntar si el ID existe o no lo inicializamos con falso
        existID = False
        #para un producto en el arreglo de productos
        for product in self.products:
            #si el producto del ID es un entero y es encontrado
            if product.ID == int(idProducto):
                #el stock del objeto producto se reduce en 1 es decir que se ha vendido
                product.stock -= 1
                #y las ganancias se suman el precio del producto que se vendio
                self.earns += product.price
                #la variable bandera existe ID se asgina como verdadera
                existID = True
                #y se immprime que el producto a sido existosamente vendido
                print("\n¡Producto vendido exitosamente.!\n")
        #si el ID ingresado no existe es decir no es valido
        if not existID:
            #se imprime que el ID ingresado no existe
            print("\n¡El ID ingresado no existe.!\n")

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

    def addProduct(self):
        """
        Funcion para agregar un producto
        Recibe:
            self = clase producto, un objeto
        Retorna:
            no retorna
        """
        #definimos una variable data para el ingreso de los datos del objeto producto, que estaran en un formato separado por ";"
        data = input("\nIngrese los datos del producto en el siguiente formato: (Nombre; Cantidad; Precio; Fecha de Caducidad; Descripción) separados por punto y coma ';'"+"\n")
        #se realizara una division a la variable data con el split y la llave sera el punto y coma
        data = data.split(";")
        #color blanco, pintuco, 2L
        #controlar que el tamaño de la cadena sea de 5, [0,1,2,3,4]
        #si el tamanio de la variable data es de 5 elementos
        if len(data) == 5:
            #asignamos el elemento cero de la data a una variable nombre
            name = data[0]
            #asignamos el elemento uno de la data a una variable stock
            stock = data[1]
            #asignamos el elemento dos de la data a una variable price
            price = data[2]
            #asignamos el elemento tres de la data a una variable fecha de expiracion
            expirationDate = data[3]
            #asignamos el elemento cuatro de la data a una variable descripcion
            description = data[4]
            #Enviamos al constructor de la clase producto los parametros propios de el, de cada elemento ingresado
            product = Product(name=name, stock= stock, price=price, expirationDate=expirationDate,description=description)

            #Variables booleanas del tipo bandera
            validProduct = True
            #hacemos el llamado a la validacion del formato de numero en el stock si no es valido
            if not product.validateStockFormatNumber():
                #entonces el producto valido es falso
                validProduct = False
            # o si el precio no es valido no es decimal
            if not product.validatePriceFormatNumberDecimal():
                #el producto no es valido
                validProduct = False
            #si el prodcuto es valido y el producto agregado no existe ya en la lista de prodcutos enviando su nombre
            if validProduct and not self.checkIsProductExistInList(name):
                #agregamos el producto a la lista de productos
                self.products.append(product)
                #variable linea asignada con todos los datos ingresados se concatenan para formar una sola cadena de caracteres separada por comas
                line = name+","+stock+","+price+","+expirationDate+","+description+"\n"
                #usamos la clase utils para ingresar el producto en un archivo de texto
                Utils.saveObjectsOnFile(filename="products.txt",line=line) 
                #imprimimos que el producto ha sido agregado correctamente
                print("\n¡Producto agregado correctamente.!\n")
            #si el producto ya existe
            else:
                #se imprime que el producto ingresado ya existe
                print("\n¡El producto que desea ingresar ya existe.!\n")
        #si el formato de la data no es el correcto
        else:
            #se imprime que el ingreso no es el formato correcto
            print("\n¡Ingrese los datos del producto en el formato correcto.!\n")

    def listProducts(self):
        """
        Funcion para listar los productos
        Recibe:
            self = clase producto, un objeto
        Retorna:
            no retorna
        """
        # irmprimos el titulo lista de productos
        print("\nLISTA DE PRODUCTOS:\n")
        #si el tamanio de los productos es igual a cero entonces se envia el mensaje de que no existen productos
        if len(self.products) == 0:
            #se imprime que no existen productos agregados
            print("No existen productos agregados.\n")
        #si el tamanio no es cero
        else:
            #para los productos en la lista de productos
            for product in self.products:
                #hacemos el llamado a la funcion imprimir productos y enviamos el producto a imprimir
                self.printProduct(product=product)
           
    def checkIsProductExistInList(self,name):
        """
        Funcion para analizar si el producto ya ha sido agregado
        Recibe:
            self = clase producto, un objeto
            name = nombre del producto
        Retorna:
            no retorna
        """
        #para un producto en el arreglo de productos
        for product in self.products:
            #si el nombre del producto transformado en minusculas es igual al nombre que recibio como parametro igual transformado en minusculas
            if product.name.lower() == name.lower():
                #retorna verdadero
                return True
        #si no existe retorna falso
        return False

    def printProduct(self, product):
        """
        Funcion para imprimir el prodcto
        Recibe:
            self = clase producto, un objeto
            product = el producto que se va a imprimir
        Retorna:
            no retorna
        """
        #imprimimos el producto
        print("ID: "+str(product.ID)+"\nNombre: " +product.name + "\nCantidad: " + str(product.stock)+ "\nPrecio: " + str(product.price)+ "\nFecha Expiración: " + product.expirationDate + "\nDescripción: " + product.description +"\n")

    def searchProduct(self):
        """
        Funcion para buscar un producto
        Recibe:
            self = clase producto, un objeto
        Retorna:
            no retorna
        """
        #inicializamos a la variable existe producto como falsa
        existProduct = False
        #imprimios el tipo de busqueda que quiera realizar
        print("\nEscoja el tipo de busqueda que desea realizar\n")
        #opcion 1 por nombre
        print("1: Por nombre")
        #opcion 2 por ID
        print("2: Por ID")
        #uso de try para una excepcion
        try:
            #opcion de busqueda para ingresar con que se quiere buscar el producto
            opciondeBusqueda = int(input("Ingrese el número de la opción de busqueda deseada:"))
            #si la opcion de busqueda es por nombre
            if opciondeBusqueda == 1:
                #Pedimos el ingreso del nombre a buscar
                nombreProducto = input("Ingrese el nombre del producto que desea buscar:")
                #para un producto en la lista de productos
                for product in self.products:
                    #Pintura, pintura
                    #produc.name.lower() = Pintura = pintura
                    #produc.name.upper() = Pintura = PINTURA
                    #si el nombre del producto transformado a minusculas es igual al nombre de uno de los elementos igual transformado a minusculas
                    if product.name.lower() == nombreProducto.lower():
                        #imprimos que el producto ha sido encontrado
                        print("\nProducto encontrado.\n")
                        #y llamamaos a la funcion imprimir producto
                        self.printProduct(product=product)
                        #y la existencia del prodcuto pasa a ser verdadera
                        existProduct = True
            #Si en cambio la opcion de busqueda es por el ID
            elif opciondeBusqueda == 2:
                #se solicita el ID que se quiera buscar
                idProducto = int(input("Ingrese el ID del producto que desea buscar:"))
                #se realiza nuevamente la busqueda como en el anterior caso pero ahora con el ID
                for product in self.products:
                    #si el ID es igual al ID de algun producto 
                    if product.ID == idProducto:
                        #se muestra que el producto ha sido encontrado
                        print("\nProducto encontrado.\n")
                        #se llama a la funcion imprimir producto y se le envia el producto a imprimir
                        self.printProduct(product=product)
                        #la existencia del prodcuto cambia a verdadera
                        existProduct = True
            #si el producto no existe
            if not existProduct:
                #se muestra un mensaje de producto no encontrado
                print("Producto no encontrado.\n")
        #si se ingresa una opcion incorrecta
        except:
            #se imprime que la opcion ingresada no ha sido correcta
            print("Ingrese una opción correcta.\n")

    def loadProducts(self):
        """
        Funcion para cargar los productos del documento de texto
        Recibe:
            self = clase producto, un objeto
        Retorna:
            no retorna
        """
        #en una variable line_list cargamos la funcion de cargar objetos de un archivo enviamos el nombre del archivo
        line_list = Utils.loadObjectsFromFile(filename="products.txt")
        #par una linea en el arreglo line_list
        for line in line_list:
            #separamos las palabras que esten igresadas con la llave siendo una coma
            line = line.split(",")
            #su el producto existe en el archivo
            if not self.checkIsProductExistInList(line[0]):
                #asignamos cada dato a cada posicion del arreglo
                product = Product(name=line[0], stock= int(line[1]), price=float(line[2]), expirationDate=line[3],description=line[4])
                #y en la clase productos agregamos cada producto para cargarlos en memeoria
                self.products.append(product)
        #demostramos que la carga ha sido exitosa
        print("\n¡Productos cargados desde txt exitosamente.!\n")
    
class Utils:
    """
        Clase utils para el manejo de un archivo txt
        atributos:
            
        metodos:
            sabeObjectsOnfile = guarda texto en el archivo
            loadObjectsFromFile = carga el texto del archivo
    """
    def saveObjectsOnFile(filename,line):
        """
        Funcion para guardar los objetos en un archivo de texto
        Recibe:
            filename = nombre del archivo de texto
            line = el texto a guardar
        Retorna:
            lines = lineas con el texto del documento
        r = solo lectura
        w = solo escritura (sobreescribe totalmente el archivo)
        a = agregación al final del archivo
        r+ = leer y escribir
        """
        #abirmos el archivo
        file = open(filename,"a")
        #escribimos en el archivo el texto enviado
        file.write(line)
        #cerramos el archivo
        file.close()

    def loadObjectsFromFile(filename):
        """
        Funcion para cargar los objetos de un archivo de texto
        Recibe:
            filename = nombre del archivo de texto
        Retorna:
            lines = lineas con el texto del documento
        """
        #abrimos el archivo
        file = open(filename,"r")
        #leemos el archivo
        lines = file.readlines()
        #cerramos el archivo
        file.close()
        #retornamos las lineas almancenas despues de la lectura
        return lines

def menu():
    """
        Funcion para mostrar el menu
        Recibe:
            no recibe
        Retorna:
            option = a la option que el usuario escoga
    """ 
    #se imprime cada una de las opciones que puede ecoger
    print("\nEscoja un número del menú:\n")
    #el caso 1 para cargar productos
    print("1: Cargar Productos")
    #el caso 2 para vender productos
    print("2: Vender Producto")
    #el caso 3 para agregar un producto
    print("3: Agregar Producto")
    #el caso 4 para listar los productos
    print("4: Listar Productos")
    #el caso 5 para buscar los productos
    print("5: Buscar Productos")
    #el caso 6 para ver las ganancias
    print("6: Ver ganancias")
    #el casos 7 para salir
    print("7: Salir")
    #se solicita la opcion y se almacena en option
    option = input("Escriba el número y presione enter...")
    #se retorna la opcion
    return option

def executeOptionFromMenu(option, hardwareStore):
    """
        Funcion para hacer el llamado de las funciones
        Recibe:
            option = opcion escogida por el usuario
            hardwarstore = objeto de tipo ferreteria
        Retorna:
            No retorna 
    """ 
    #si la opcion 1
    if option == 1:
        #hacemos el llamado a la funcion de la ferreteria de cargar productos
        hardwareStore.loadProducts()
    #si la opcion es 2
    elif option == 2:
        #hacemos el llamado a la funcion de la ferreteria para vender un producto
        hardwareStore.sellProduct()
    #si la opcion es igual a 3
    elif option == 3:
        #hacemos el llamado a la funcion de la ferreteria para añadir un producto
        hardwareStore.addProduct()
    #si la ocion es igual a 4
    elif option == 4:
        #hacemos el llamado a la funcion de la ferreteria para listar los productos
        hardwareStore.listProducts()
    #si la opcion es igual a 5
    elif option == 5:
        #hacemos el llamado a la funcion de la ferreteria para buscar un producto 
        hardwareStore.searchProduct()
    #si la opcion es igual a 6
    elif option == 6:
        #hacemos el llamado a la funcion de la ferreteria para ver las ganancias
        hardwareStore.listEarns()
    #si la opcion es igual a 7
    elif option == 7:
        #salimos
        exit()
    else:
        executeOptionFromMenu(option=menu(), hardwareStore = hardwareStore)

#if __name__ == "__main__": se inicializa el codigo desde esta linea (main)
if __name__ == "__main__":
    """
        Funcion usar el menu
        Recibe:
            No recibe
        Retorna:
            No retorna 
    """ 
    #imprimir una bienvenida al sistema
    print("\n¡Bienvenido al sistema de gestión de venta de productos!\n")
    #instancia de la clase ferreteria enviando el nombre
    hardwareStore = HardwareStore(name="Ferreteria Popular")
    #variable para seguir mientras es verdadera
    loop = True
    #mientras lopp sea vedadero
    while(loop):
        #try para cpaturar la opcion del menu sea un entero
        try:
            #opcion como entero
            option=int(menu())
        #excepcion
        except:
            #option None
            option = None
            #imprimir que se ha seleccionado una opcion erroena
            print("\n¡Se ha seleccionado una opción que no existe.!\n")
        #si la opcion es diferente de none
        if option != None:
            #hacemos el llamado a la funcion para ejecutra el menu mandamos el objeto ferreteria y la opcion
            executeOptionFromMenu(option, hardwareStore=hardwareStore)
            #si la opcion es igual a 7
            if option == 7:
                #exit()
                #loop = False
                #se imprime un adios
                print("Adios\n")
                #se rompe el bucle
                break