n = int(input("Ingrese un número: "))
if n > 0:
    cadena = "es un número positivo"
else:
    if n<0:
        cadena = "es un número negativo"
if n%2 == 0:
    cadena2 = "y par"
else:
    if n%2 != 0:
        cadena2 = "e impar"
mensaje = "%s %s %s" % (n, cadena, cadena2)

print (mensaje)