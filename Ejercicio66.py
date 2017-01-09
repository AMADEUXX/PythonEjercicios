oracion=raw_input("Ingrese una oracion:")
cantidad=0
x=0
while x<len(oracion):
    if oracion[x]==" ":
        cantidad=cantidad+1
    x=x+1
if cantidad==0:
    print("no hay ningun espacio")
else:
    print("La cantidad de espacios es: ")
    print(cantidad)