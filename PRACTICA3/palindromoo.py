while True:
    texto = input("Introduce un texto: ")
    if not texto.isalpha():
        print("Error: Solo se permiten letras.")
        continue
    if texto.endswith('v'):
        break
    if texto == texto[::-1]:
        resultado = "El texto es un palindromo."
    else:
        resultado = "El texto no es un palindromo."
    print(resultado)