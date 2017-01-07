num=int(input("Ingresa un numero de hasta 3 cifras: "))
if num<10:
	print("El numero ",num, "Tiene 1 digito")
else:
	if num>10 and num<100:
		print("El numero ",num, "Tiene 2 digitos")
	else:
		if num>100 and num<999:
			print("El numero ",num, "Tiene 3 digitos")
		else:
			print("Error, El numero tiene mas de 3 digitos")
