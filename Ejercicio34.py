n=int(input("Cuantos empleados son: "))
x=1
y=0
z=0
gastos=0
while x<=n:
	sueldo=float(input("Ingresa el sueldo del empleado: "))
	if sueldo<=300:
		y=y+1
	else:
		z=z+1
	gastos=gastos+sueldo
	x=x+1
print("Cantidad de empleados que ganan entre 100 y 300 ")
print(y)
print("Cantidad de empleados que ganan mas de 300 ")
print(z)
print("El importe de gastos es de")
print(gastos)