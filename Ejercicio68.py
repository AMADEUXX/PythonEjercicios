clave=raw_input("Ingrese una clave:")
cantidad=len(clave)
if cantidad>=10 and cantidad<=20:
    print("La clave es correcta: ")
    print(cantidad)
    print("Su clave es: ")
    print(clave)
else:
	print("La clave excede el parametro de 10 a 20 caracteres")
	print(cantidad)