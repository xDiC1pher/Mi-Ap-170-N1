#Ingrese 5 notas, de 1.0 a 7.0, obtenga:
# * nota mayor
# * nota menor
# * promedio
# Lanzar una excepción cuando ocurra una nota fuera de rango
try:
    notas = []
    for i in range(5):
        n = float(input(f"Ingrese nota [{i+1}]: "))
        if not 1 <= n <= 7:
            raise ValueError("Nota fuera de rango")
        notas.append( n )

    print("Nota Mayor: " , max(notas))
    print("Nota Menor: " , min(notas))
    print("Promedio: ", sum(notas)/len(notas))
except ValueError as mensaje:
    print("Error::::", mensaje)