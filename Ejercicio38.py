n=int(input("Cuantos numeros vas a cargar"))
x=1
y=0
z=0
while x<=n:
	numero=int(input("Ingresa un numero"))
	if numero%2==0:
		y=y+1
	else:
		z=z+1
	x=x+1
print("La cantidad de numeros pares es: ")
print(y)
print("La cantidad de numeros impares es: ")
print(z)