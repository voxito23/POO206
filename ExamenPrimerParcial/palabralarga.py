while True:
    entrada = input("Introduce una palabra o 'v' para salir: ")
    if entrada.lower() == 'v':
        print("Programa terminado por el usuario.")
        break
    try:
        palabra1 = entrada.strip().split()
        p1 = len (palabra1)
        if len(palabra1) == 1:
            palabra = palabra1[0]
            for i, letra in enumerate(palabra, 1):
                print(f"letra {i}: {letra}")
        else:
            print("Por favor introduce solo una palabra")
    except ValueError:
        print("Por favor introduce una palabra")