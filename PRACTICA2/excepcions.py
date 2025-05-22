try:
    numero = int(input("Introduce un numero: "))
    resultado = 100 / numero
    
    print("Resultado:", resultado)
    
except ValueError:
    print("Error: No se pueden meter otra cosa que no sea un numero.")
except ZeroDivisionError:
    print("Error: no se puede dividir entre 0.")