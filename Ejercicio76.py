lista=[]
valor=int(input("Ingresar valor (0 para finalizar):"))
while valor!=0:
    lista.append(valor)
    valor=int(input("Ingresar valor (0 para finalizar):"))
print("La lista tiene los siguientes elementos")
print(lista)
print("Tamano de la lista:")
print(len(lista))