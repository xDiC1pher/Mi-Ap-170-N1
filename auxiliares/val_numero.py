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