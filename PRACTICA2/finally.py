try:
    print("try")
    x = 10/0
except ZeroDivisionError:
    print("No se puede dividir entre 0")
finally:
    print("Ejecutando finally")