#import ap170funciones as f
from ap170funciones import *
import pickle

# Proyecto : Control de inventario de un almacen
# Autor: Manuel Sánchez Cárcamo
"""
Un método de versionamiento del codigo es el sgte
Version MAJOR.MINOR.PATCH

1.- MAJOR: (version mayor) se incrementa cuando se hacen ca,bios grandes o
        incompatibles con version anterior, p.e.: cambio a base de datos, 
        integracion de nuevas funciones/capacidades
    MINOR (version menor): Se incrementa cuando se agregan funcionalidades nuevas
        pero sin romper la compatibilidad
    PATCH (parche o revision): Se increment cuando se corrigen errores o se hacen 
        mejoras. p.e.: Agregan validaciones a la lectura de datos.
"""

# Historial
#   2025.04.17  : Inicio del proyecto (v1.0.0)
#   2025.04.22  : Agrega primeras opciones 1,2 y 3 (v1.1.0)
#   2025.04.29  : cambia paradigma de desarrollo y pasamos de prog. lineal a modular v2.0.0
#                 primera funcio validar_numero
#   2025.05.06  : Se reemplaza acciones repetidas por funciones v2.0.1
#   2025.06.03  : Se modulariza el código en funciones para c/opcion del menu v2.1.0
#                 Además se separan las funciones del programa principal.


def fn_guardar_inventario_txt(lnom, lpre, lsto):
    with open("inventario.txt", "w", encoding = "utf-8") as inventario:
        for i in range(len(lnom)):
            inventario.write(lnom[i]+"\n")
            inventario.write(str(lpre[i])+"\n")
            inventario.write(str(lsto[i])+"\n")            
            #inventario.write(lnom[i]+";"+str(lpre[i])+";"+str(lsto[i])+"\n")
        print("inventario guardado en inventario.txt")

def exportar_inventario_csv(lnom, lpre, lsto):
    with open("inventario.txt", "w", encoding = "utf-8") as inventario:
        inventario.write("PRODUCTO;PRECIO;CANTIDAD\n")
        for i in range(len(lnom)):
            inventario.write(lnom[i]) +";" + str(lpre[i]) +";" str(lsto[i])+"\n")            
            #inventario.write(lnom[i]+";"+str(lpre[i])+";"+str(lsto[i])+"\n")
        print("inventario exportado a inventario.csv")

def fn_cargar_inventario_txt(lnom, lpre, lsto):
    try:
        with open("inventario.txt", "r", encoding = "utf-8") as inventario:
            lineas = inventario.readlines()
            num_lin = len( lineas )
            for i in range (0, num_lin, 3):
                nom = lineas[i].strip()
                pre = float(lineas[i+1].strip())
                cant = int(lineas[i+2].strip())
                lnom.append(nom)
                lpre.append(pre)
                lsto.append(cant)
        print("Inventario cargado correctamente")
    except FileNotFoundError:
        print("No se encontró el archivo 'inventario.txt'. Inventario Vacío")
    except Exception as error:
        print("Error al cargar el inventario ",error)

def fn_guardar_inventario_bin (lnom, lpre, lsto):
    with open("inventario.bin", "wb") as archivo:
        pickle.dump((lnom, lpre, lsto), archivo)
    print("inventario guardado en inventario.bin")

def fn_cargar_inventario_bin(lnom, lpre, lsto):
    try:
        with open("inventario.bin", "rb") as archivo:
            datos = pickle.load(archivo)
            lnom.extend(datos[0])
            lpre.extend(datos[1])
            lsto.extend(datos[2])
        print("Inventario cargado correctamente")
    except FileNotFoundError:
        print("No se encontró el archivo 'inventario.bic'. Inventario Vacío")
    except Exception as error:
        print("Ups!, ocurrio el error: ", error)
    


#Programa Principal
version = "v2.1.0"
# lnombre = ['Plumon', 'Borrador', 'Pizarra']
# lprecio = [1850.0, 3500.0, 13500.0]
# lstock = [20, 5, 10]
lprecio = []
lnombre = []
lstock  = [] 

# fn_cargar_inventario_txt(lnombre, lprecio, lstock)
fn_cargar_inventario_bin(lnombre, lprecio, lstock)
salir = False
while (not salir):
    print(f"**** MENU {version} ****")
    print("[1] Agregar Producto")
    print("[2] Listar Productos")
    print("[3] Buscar Producto")
    print("[4] Modificar Stock")
    print("[5] Eliminar Producto")
    print("[7] Salir")
    op = input("Opción: ")

    # AGREGAR PRODUCTO *************
    if (op == "1"):
        fn_agregar_producto(lnombre, lprecio, lstock)
        fn_guardar_inventario_bin(lnombre, lprecio, lstock)
    # LISTAR PRODUCTO *************
    if (op == "2"):
        fn_listar_producto(lnombre, lprecio, lstock)
    # BUSCAR PRODUCTO *************
    if (op == "3"):
        fn_buscar(lnombre, lprecio, lstock)
    # MODIFICAR PRODUCTO *************
    if (op == "4"):
        fn_modificar_producto(lnombre, lprecio, lstock)
        fn_guardar_inventario_bin(lnombre, lprecio, lstock)
    # ELIMINAR PRODUCTO *************
    if (op == "5"):
        fn_eliminar_producto(lnombre, lprecio, lstock)
        fn_guardar_inventario_bin(lnombre, lprecio, lstock)
    # EXPORTAR INVENTARIO *************
    if (op == "6"):
        fn_eliminar_producto(lnombre, lprecio, lstock)
    # SALIR PRODUCTO *************
    if op == "7": 
        # fn_guardar_inventario_txt(lnombre, lprecio, lstock)
        fn_guardar_inventario_bin(lnombre, lprecio, lstock)
        salir = True
        print("Hasta luego")
    