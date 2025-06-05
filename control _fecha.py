dia = int(input("dia : "))
mes = int(input("Mes : "))
aaaa = int(input("Año : "))

if mes >= 1 and mes <= 12: 
    #determinando maximo de dias por mes
    match mes: 
        case 4|6|9|11:
            dias = 30
        case 1|3|5|7|8|10|12:
            días = 31
        case _:   #o sea febrero
            # //es bisiesto
            if ((aaaa % 4) == 0 and (aaaa % 100) != 0) or (aaaa % 400) == 0: 
                dias = 29
            else:
                dias = 28
    if (dia <= dias):
        print("Fecha correcta")
    else:
        print("Fecha es inccorrecta")
        print(f"El mes {mes} tiene maximo {dias} dias")
else:
    print("El mes no es valido, use valor entre 1 y 12")

