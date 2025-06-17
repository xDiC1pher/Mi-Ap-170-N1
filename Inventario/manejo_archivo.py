# with open("archivo.txt", "w", encoding = "utf-8") as archivo:
#     archivo.write("Este es el primer contenido del archivo\n")
#     archivo.write("Se puede agregar más líneas\n")

mifile = open("archivo.docx", "w", encoding = "utf-8")
mifile.write("Este es el primer contenido del archivo\n")
mifile.write("Se puede agregar más líneas\n")
mifile.close()


#control de borrado y grabado
# mifile = open("archivo.txt", "w", encoding = "utf-8")
# input("revisa el archivo.txt, esta vacío?")
# mifile.write("nuevo contenido\n")
# input("vuelve a revisar el archivo, ¿ya está escrito ?")
# mifile.close()

# Leer el archivo
# mifile = open("archivo.txt", "r", encoding = "utf-8")
# contenido = mifile.read()
# print( contenido )
# mifile.close()
