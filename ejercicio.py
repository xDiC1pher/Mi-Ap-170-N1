import math

pi = math.pi

def area_circunferencia(radio):
    area = pi * radio ** 2
    return area

def volumen_esfera(radio):
    volumen = 4/3 * pi ** 3
    return volumen

def ejecutar_codigo():
    radio = float(input("Ingrese el radio de la circunferencia: "))
    print()
    area_circ = area_circunferencia(radio)
    print(f"Area = {area_circ}")
    print()
    volumen_circ = volumen_esfera(radio)
    print(f"Volumen = {volumen_circ}")
    print()

ejecutar_codigo()