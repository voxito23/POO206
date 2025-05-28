while True:
    entrada = input("Introduce un numero o 'v' para salir: ")
    if entrada.lower() == 'v':
        print("Programa terminado por el usuario.")
        break
    try:
        numero = int(entrada)
        if numero <= 10:
            print("El numero debe ser mayor de 10.")
            continue
        if numero < 0:
            print("El numero debe ser positivo.")
            continue
        impares = [str(i) for i in range(2, numero + 1, 2)]
        print(", ".join(impares))
    except ValueError:
        print("Por favor, introduce un numero entero valido.")
            
     

