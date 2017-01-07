x=int(input("Ingresa la coordenada para x: "))
y=int(input("Ingresa la coordenada para y: "))
if x>0 and y>0:
	print("Estan en el 1er Cuadrante")
else:
	if x<0 and y>0:
		print("Estan en el 2do Cuadrante")
	else:
		if x<0 and y<0:
			print("Estan en el 3er Cuadrante")
		else:
			print("Estan en el 4to Cuadrante")