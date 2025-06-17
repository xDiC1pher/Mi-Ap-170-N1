import hashlib

#md5 de un texto
# texto = input("Texto: ")
# texto_byte = texto.encode()
# hash_md5 = hashlib.md5(texto_byte)
# print(hash_md5.hexdigest())


#md5 de un archivo

def calcula_md5_archivo(ruta)
    hash_md5 = hashlib.md5()
    with open(ruta, "rb") as f:
        bloque = f.read(4096)
        while bloque != b"":
            hash_md5.update(bloque)
            bloque = f.read(4096)
    return hash_md5.hexdigest()

#pp
camino = 