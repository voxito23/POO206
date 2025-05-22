def verificar_numero(numero):
    if numero>10:
        raise ValueError("El numero es mayor que 10")
    print("Numero correcto:", numero)
try:
    verificar_numero(21)
except Exception as e:
    print("Error:", e)