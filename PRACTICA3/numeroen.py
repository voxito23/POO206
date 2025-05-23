while True:
    entrada = input("Introduce un numero o 'v' para salir: ")
    if entrada.lower() == 'v':
        raise Exception("Programa terminado por el usuario.")
    try:
        numero = int(entrada)
        if numero % 2 == 0:
            resultado = "El numero es par"
        else:
            resultado = "El numero es impar"
        print(resultado)
    except ValueError:
        print("Error: Se ingreso algo que no es un numero entero.")