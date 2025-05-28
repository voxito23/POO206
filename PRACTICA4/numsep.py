while True:
    entrada = input("Introduce un numero + o 'v' para salir: ")
    if entrada.lower() == 'v':
        print("Programa terminado por el usuario.")
        break
    try:
        n = int(entrada)
        if n < 0:
            print("El numero debe ser +.")
        else:
            atras= [str(i) for i in range(n, -1, -1)]
            print(", ".join(atras))
    except ValueError:
        print("Por favor, introduce un numero entero valido.")
        