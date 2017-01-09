lista=["amadeo","daniela","diana","pepe","luis"]
x=0
cantidad=0
while x<len(lista):
	if len(lista[x])>=5:
		cantidad=cantidad+1
	x=x+1
print("La lista tiene los siguientes elementos: ")
print(lista)
print("La cantidad de nombres con mas de 5 letras es de: ")
print(cantidad)