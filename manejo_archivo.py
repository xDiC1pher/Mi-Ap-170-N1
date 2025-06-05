# with open("archivo.txt", "w") as archivo:
#     archivo.write("Este es el primer contenido del archivo\n")
#     archivo.write("Se puede agregar más líneas\n")

# mifile = open ("archivo.txt", "w", encoding= "utf-8")
# mifile.write("Este es el primer contenido del archivo\n")
# mifile.write("Se puede agregar más líneas\n")
# mifile.close()

# mifile = open ("archivo.txt", "w", encoding= "utf-8")
# input("Revisa el archivo.txt, está vacío?")

# mifile.write("nuevo contenido\n")

# input("Vuelve a revisar el archivo, ¿ya está escrito?")
# mifile.close()

# Leer el archivo
mifile = open("archivo.txt", "r", encoding= "utf-8")
contenido = mifile.read()
print( contenido )
mifile.close()