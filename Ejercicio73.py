lista=[7,3,2,7,5,8,9]
x=0
cantidad=0
while x<len(lista):
	if lista[x]>=7:
		print(lista[x])
		cantidad=cantidad+1
	x=x+1
print("La lista tiene los siguientes elementos: ")
print(lista)
print("La cantidad de numers mayores a 7 es de: ")
print(cantidad)