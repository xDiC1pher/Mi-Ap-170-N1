import getpass
import pwinput
import bcrypt

# usuario = input("Usuario: ")
clave = input("Clave: ")
#aqui esta laclave en texto plano o texto llano
print(f"clave {clave}")

#ahora vamos a encriptar
#pasamos a byte
clave_byte = clave.encode("utf-8")
#generar el hash
salero =  bcrypt.gensalt() 
clave_hash = bcrypt.hashpw(clave_byte, salero)
print(clave_hash)

otra = input("Clave: ")
otra_byte = otra.encode("utf-8")
print("Coincide :", bcrypt.checkpw(otra_byte,clave_hash ))
#generar el hash
# otra_hash = bcrypt.hashpw(otra_byte, salero )
# print(otra_hash)

