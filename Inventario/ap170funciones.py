def valida_numero(mensaje="Valor : "):
    """
    valida_numero( parametro ): funcion que valida la elctura de un numero entero o flotante, 
            retorna el valor leido, o repite la pregunta hasta qe el usuario ingrese un valor numérico.
            El parametro de entrada es el mensaje a mostrar al preguntar por el nro.
    """
    validos = ["0","1","2","3","4","5","6","7","8","9","-","."]
    repite = True
    malochar = False  
    num = ""
    while repite:
        num = input(mensaje)
        largo = len ( num )
        # valida caracteres
        for i in range(largo):
            if not num[i] in validos:
                malochar = True
        #valida numero de guiones
        cont = 0
        for i in range(largo):
            if num[i] == "-":
                cont = cont + 1
        malog = cont > 1
        contp = 0
        for i in range(largo):
            if num[i] == ".":
                contp = contp + 1
        malop = contp > 1
        #valida posicion del guion
        malopos = False
        if cont == 1: #es decir, hay un guion
            if num[0] != "-":
                malopos = True # verdad que el guion está mal puesto 
        if malochar or malog or malopos or malop:
            repite = True
            malochar = False  
        else:
            repite = False
    if "." in num:
        numero = float(num)
    else:
        numero = int(num)
    return( num )
    #valida_numero


def fn_mostrar_producto(nombre, precio, cantidad):
    """
    Funcion para mostrar los 3 datos de un producto

    Parámetros:
    -----------
        - nombre: nombre del producto -> str
        - precio: precio del producto -> float
        - cantidad: stock del prodcuto -> int
    """
    print(f"Nombre  : {nombre}")
    print(f"Precio  : {precio}")
    print(f"Cantidad: {cantidad}")
    #fn_mostrar_producto

def fn_buscar_producto(productos, nom):
    largo = len( productos )
    esta = False
    i = 0
    while i < largo and not esta:
        if ( nom.lower() == productos[i].lower()):
            esta = True
        else:
            i = i + 1
    if esta:
        return(i)
    else:
        return( -1 )

def fn_agregar_producto(lnom, lpre, lsto):
        print("AGREGAR PRODUCTO")
        nom = input("Ingrese nombre  : ")
        pre = valida_numero("Ingrese Precio  : ")
        cant = valida_numero("Ingrese cantidad: ")
        lnom.append( nom )
        lpre.append( pre )    
        lsto.append( cant )    
        print(f"El producto {nom} se agregó correctamente.\n")

def fn_listar_producto(lnom, lpre, lsto):
    print("\nLISTAR PRODUCTOS\n")
    largo = len( lnom )
    if largo == 0:
        print("No hay productos en el inventario\n")
    else:
        for i in range( largo ):
            fn_mostrar_producto(lnom[i],lpre[i],lsto[i] )
            print("____________________________________\n")


def fn_buscar(lnom,lpre,lsto):
    print("\nBUSCAR PRODUCTOS\n")
    nom = input("Producto a buscar : ")
    pos = fn_buscar_producto(lnom, nom)
    if pos != -1:
        fn_mostrar_producto(lnom[pos],lpre[pos],lsto[pos] )
    else:
        print(f"El producto {nom} no está en el inventario")
    
def fn_modificar_producto(lnom,lpre,lsto):
    print("\nMODIFICAR PRODUCTO\n")
    nom = input("Producto a Modificar : ")
    pos = fn_buscar_producto(lnom, nom)
    if pos != -1:  # si lo encontró
        fn_mostrar_producto(lnom[pos],lpre[pos],lsto[pos] )
        resp = input("Seguro desea modificar [si/no]: ")
        if (resp.lower() == "si"): #para evitar SI Si sI...etc
            cant = valida_numero("Nueva Cantidad: ")
            lsto[pos] = int(cant)
            print("La cantidad cambió.")
        else:
            print("La cantidad no cambió.")
    else:
        print(f"El producto {nom} no está en el inventario")

def fn_eliminar_producto(lnom,lpre,lsto):
    print("\nELIMINAR PRODUCTO\n")
    nom = input("Producto a Eliminar : ")
    largo = len( lnom )
    esta = False
    i = 0
    while i < largo and not esta:
        if ( nom.lower() == lnom[i].lower()):
            fn_mostrar_producto(lnom[i],lpre[i],lsto[i] )
            esta = True
            resp = input("Seguro desea Eliminar [si/no]: ")
            if (resp.lower() == "si"): #para evitar SI Si sI...etc
                del lnom[i] #eliminando de cada lista , la misma posicion
                del lpre[i] 
                del lsto[i]
                print(f"El producto {nom} ha sido eliminado")
            else:
                print(f"El producto {nom} NO ha sido eliminado")
        i = i + 1
    if not esta:
        print(f"El producto {nom} no está en el inventario")