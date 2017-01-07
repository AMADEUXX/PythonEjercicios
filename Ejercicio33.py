x=1
suma=0
n=int(input("Cuantas alturas calcularas: "))
while x<=n:
    altura=int(input("Ingrese altura:"))
    suma=suma+altura
    x=x+1
prom=suma/n
print("La suma de las alturas es")
print(suma)
print("El promedio de las alturas es")
print(prom)