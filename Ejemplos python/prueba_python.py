
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
ciudad = input("Ingrese su Ciudad: ")
promedio = float(input("Ingrese su promedio: "))

if promedio > 10.1 or promedio < 0:
    cadena = "Promedio inválido"
else:
    if (promedio >= 9) and (promedio <=10):
        cadena = "Sobresaliente"
    else:
        if (promedio >= 7.0) and (promedio <=8.9):
            cadena = "Muy bueno"
        else:
            if (promedio >= 5.0) and (promedio <=6.9):
                cadena = "Bueno"
            else: cadena = "Malo"

mensaje = "Datos del estudiante\n\tNombre:%s\n\tApellido:%s\n\tCiudad:%s\n\tPromedio:%.2f "\
        "equivalente a %s\n" % (nombre, apellido, ciudad, promedio, cadena)

print(mensaje)
