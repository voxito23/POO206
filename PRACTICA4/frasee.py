while True:
    entrada = input("Introduce una frase y una letra o 'v' para salir: ")
    if entrada.lower() == 'v':
        print("Programa terminado por el usuario.")
    break
try:
    frase = input("Introduce una frase: ")
    letra = input("Introduce una letra: ")
    contador = frase.count(letra)
    print(f"La letra '{letra}' aparece {contador} veces en la frase.")
except ValueError:
    print("Error: Se ingreso algo que no es una letra o frase valida.")
        