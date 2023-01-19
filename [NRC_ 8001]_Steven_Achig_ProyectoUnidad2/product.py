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
        validarStockFormatNumbre:
    """
    #constructor = __init__ de la clase Product
    def __init__(self, name, stock, price, expirationDate, description):
        #definimos las variables de los atributos para el constructor
        self.ID = random.randint(10001,99999)
        self.name = name
        self.stock = stock
        self.price = price
        self.expirationDate = expirationDate
        self.description = description

    def validateStockFormatNumber(self):
        if self.stock.isnumeric():
            self.stock = int(self.stock)
            return True
        else:
            print("\n¡La cantidad del producto no esta en formato numérico.!\n")
            return False

    def validatePriceFormatNumberDecimal(self):
        try:
            self.price = float(self.price)
            return True
        except ValueError:
            print("\n¡El precio del producto no esta en formato numérico decimal.!\n")
            return False

#Taladro;100;10.80;No aplica;De acero resistente incluido tuercas
#Pintura;100;35.10;01/01/2024;Pintuco de color blanco,1L

class HardwareStore:
    products = []
    earns = 0

    def __init__(self, name):
        self.name = name

    def sellProduct(self):
        self.listProducts()
        idProducto = input("Ingrese el ID del producto a vender:")
        existID = False
        for product in self.products:
            if product.ID == int(idProducto):
                product.stock -= 1
                self.earns += product.price
                existID = True
                print("\n¡Producto vendido exitosamente.!\n")
        if not existID:
            print("\n¡El ID ingresado no existe.!\n")

    def listEarns(self):
        print("Ganancias totales: $"+str(round(self.earns,2))+"\n")

    def addProduct(self):
        data = input("\nIngrese los datos del producto en el siguiente formato: (Nombre, Cantidad, Precio, Fecha de Caducidad, Descripción) separados por punto y coma ';'"+"\n")
        data = data.split(";")
        #color blanco, pintuco, 2L
        #controlar que el tamaño de la cadena sea de 5, [0,1,2,3,4]
        if len(data) == 5:
            print()
            name = data[0]
            stock = data[1]
            price = data[2]
            expirationDate = data[3]
            description = data[4]
            
            product = Product(name=name, stock= stock, price=price, expirationDate=expirationDate,description=description)

            #Variables booleanas del tipo bandera
            validProduct = True

            if not product.validateStockFormatNumber():
                validProduct = False
            if not product.validatePriceFormatNumberDecimal():
                validProduct = False

            if validProduct and not self.checkIsProductExistInList(name):
                self.products.append(product)
                line = name+","+stock+","+price+","+expirationDate+","+description+"\n"
                Utils.saveObjectsOnFile(filename="products.txt",line=line) 
                print("\n¡Producto agregado correctamente.!\n")
            else:
                print("\n¡El producto que desea ingresar ya existe.!\n")
        else:
            print("\n¡Ingrese los datos del producto en el formato correcto.!\n")

    def listProducts(self):
        # for element in elements
        print("\nLISTA DE PRODUCTOS:\n")
        if len(self.products) == 0:
            print("No existen productos agregados.\n")
        else:
            for product in self.products:
                self.printProduct(product=product)
           
    def checkIsProductExistInList(self,name):
        for product in self.products:
            if product.name.lower() == name.lower():
                return True
        return False

    def printProduct(self, product):
         print("ID: "+str(product.ID)+"\nNombre: " +product.name + "\nCantidad: " + str(product.stock)+ "\nPrecio: " + str(product.price)+ "\nFecha Expiración: " + product.expirationDate + "\nDescripción: " + product.description +"\n")

    def searchProduct(self):
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