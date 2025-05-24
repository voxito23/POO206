while True:
    try:
        contrasena = input("Introduce una contraseña: ")
        if len(contrasena) < 8:
            resultado = "La contraseña es demasiado corta."
        elif not any(char.isdigit() for char in contrasena):
            resultado = "La contraseña debe contener al menos un número."
        elif not any(char.isupper() for char in contrasena):
            resultado = "La contraseña debe contener al menos una letra mayúscula."
        elif not any(char.islower() for char in contrasena):
            resultado = "La contraseña debe contener al menos una letra minúscula."
        else:
            resultado = "La contraseña es válida."
        print(resultado)
    except ValueError:
        print("Error: Se ingreso algo que no es un texto valido.")
        break