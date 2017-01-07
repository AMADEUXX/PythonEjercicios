sueldo=int(input("Ingresa tu sueldo: "))
antiguo=int(input("Ingresa los anios de antiguedad: "))
if sueldo<500 and antiguo>=10:
	subtotal=sueldo*.2
	total=sueldo+subtotal
	print("Se otorgo aumento del 20%, el total a pagar es: ")
	print(total)
else:
	if sueldo<500 and antiguo<10:
		subtotal=sueldo*.05
		total=sueldo+subtotal
		print("Se otorgo aumento del 5%, el total a pagar es: ")
		print(total)
	else:
		if sueldo>=500:
			print("No se otorgo aumento")
			print(sueldo)