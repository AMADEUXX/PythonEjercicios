lista=[1000,2000,100,50,30,800,200,700]
x=0
cantidad=0
while x<len(lista):
	if lista[x]>100:
		cantidad=cantidad+1
	x=x+1
print("La lista tiene los siguientes elementos: ")
print(lista)
print("La cantidad de numers mayores a 100 es de: ")
print(cantidad)