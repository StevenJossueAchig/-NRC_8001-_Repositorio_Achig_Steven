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
        existProduct = False
        print("\nEscoja el tipo de busqueda que desea realizar\n")
        print("1: Por nombre")
        print("2: Por ID")
        try:
            opciondeBusqueda = int(input("Ingrese el número de la opción de busqueda deseada:"))
            if opciondeBusqueda == 1:
                nombreProducto = input("Ingrese el nombre del producto que desea buscar:")
                for product in self.products:
                    #Pintura, pintura
                    #produc.name.lower() = Pintura = pintura
                    #produc.name.upper() = Pintura = PINTURA
                    if product.name.lower() == nombreProducto.lower():
                        print("\nProducto encontrado.\n")
                        self.printProduct(product=product)
                        existProduct = True
        
            elif opciondeBusqueda == 2:
                idProducto = int(input("Ingrese el ID del producto que desea buscar:"))
                for product in self.products:
                    if product.ID == idProducto:
                        print("\nProducto encontrado.\n")
                        self.printProduct(product=product)
                        existProduct = True
    
            if not existProduct:
                print("Producto no encontrado.\n")

        except:
            print("Ingrese una opción correcta.\n")

    def loadProducts(self):
        line_list = Utils.loadObjectsFromFile(filename="products.txt")
        for line in line_list:
            line = line.split(",")

            if not self.checkIsProductExistInList(line[0]):
                product = Product(name=line[0], stock= int(line[1]), price=float(line[2]), expirationDate=line[3],description=line[4])
                self.products.append(product)

        print("\n¡Productos cargados desde txt exitosamente.!\n")
    
class Utils:
    def saveObjectsOnFile(filename,line):
        """
        r = solo lectura
        w = solo escritura (sobreescribe totalmente el archivo)
        a = agregación al final del archivo
        r+ = leer y escribir
        """
        file = open(filename,"a")
        file.write(line)
        file.close()

    def loadObjectsFromFile(filename):
        file = open(filename,"r")
        lines = file.readlines()
        file.close()
        return lines



def menu():
    print("\nEscoja un número del menú:\n")
    print("1: Cargar Productos")
    print("2: Vender Producto")
    print("3: Agregar Producto")
    print("4: Listar Productos")
    print("5: Buscar Productos")
    print("6: Ver ganancias")
    print("7: Salir")
    option = input("Escriba el número y presione enter...")
    return option

def executeOptionFromMenu(option, hardwareStore):
    if option == 1:
        hardwareStore.loadProducts()
    elif option == 2:
        hardwareStore.sellProduct()
    elif option == 3:
        hardwareStore.addProduct()
    elif option == 4:
        hardwareStore.listProducts()
    elif option == 5:
        hardwareStore.searchProduct()
    elif option == 6:
        hardwareStore.listEarns()
    elif option == 7:
        exit()
    else:
        executeOptionFromMenu(option=menu(), hardwareStore = hardwareStore)

#if __name__ == "__main__": se inicializa el codigo desde esta linea (main)
if __name__ == "__main__":
    print("\n¡Bienvenido al sistema de gestión de venta de productos!\n")

    hardwareStore = HardwareStore(name="Ferreteria Popular")
    #option = menu()

    loop = True
    while(loop):
        try:
            option=int(menu())
        except:
            option = None
            print("\n¡Se ha seleccionado una opción que no existe.!\n")

        if option != None:
            executeOptionFromMenu(option, hardwareStore=hardwareStore)
            if option == 7:
                #exit()
                #loop = False
                print("Adios\n")
                break