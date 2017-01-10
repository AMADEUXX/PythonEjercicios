n=int(input("Cuantos valores ingresara"))
cantidad=0
for f in range(n):
	base=int(input("Ingresa la base: "))
	altura=int(input("Ingresa la altura: "))
	superficie=(base*altura)/2
	if superficie>12:
		cantidad=cantidad+1
	print("La base del triangulo es ",base)
	print("La altura del triangulo es ",altura)
	print("La superficie del triangulo es ",superficie)
	print("La cantidad de triangulos mayores a 12 es de ",cantidad)