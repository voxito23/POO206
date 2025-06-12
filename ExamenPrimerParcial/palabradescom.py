while True:
    entrada = input("Introduce 2 palabras o 'v' para salir: ")
    if entrada.lower() == 'v':
        print("Programa terminado por el usuario.")
        break
    try:
        palabra1, palabra2 = entrada.strip().split()
        p1 = len(palabra1)
        p2 = len(palabra2)
        if p1 > p2:
            print(f"{palabra1} es mas larga que {palabra2} por {p1 - p2} letras")
        elif p2 > p1:
            print(f"{palabra2} es mas larga que {palabra1} por {p2 - p1} letras")
        else:
            print("Ambas palabras tienen la misma longitud")
    except ValueError:
        print("Por favor introduce exactamente 2 palabras")