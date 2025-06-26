import pwinput
import bcrypt

def fn_crear_usuario(users):
    cuenta = input("Cuenta: ")
    if cuenta in users:
        print("El usuario ya existe.\n")
    else:
        clave = pwinput.pwinput("Contraseña: ")
        clave_byte = clave.encode()
        clave_hash = bcrypt.hashpw(clave_byte, bcrypt.gensalt())
        users[cuenta] = clave_hash
        print(f"Se creó el usuario [{cuenta}]\n")


#pp
usuarios = {}
salir = False
while not salir:
    print("MENU DE USUARIOS")
    print("(1) Crear usuario")
    print("(2) Cambiar constraseña")
    print("(3) Eliminar usuario")
    print("(4) Listar usuario")
    print("(5) Salir")
    op = input("Opción: ")

    if op == "1":
        fn_crear_usuario( usuarios )

    if op == "5":
        salir = True
print("Hasta luego.")