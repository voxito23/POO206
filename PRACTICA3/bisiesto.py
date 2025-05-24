while True:
    entrada = input("Introduce un año 'v' para salir: ")
    if entrada.lower() == 'v':
        break
    try:
        año = int(entrada)
        if ((año % 400 == 0) or (año % 100 != 0) and (año % 4 == 0)):
            resultado = "El año es bisiesto."
        else:
            resultado = "El año no es bisiesto."
        print(resultado)
    except ValueError:
        raise ValueError("Favor de poner un año")
