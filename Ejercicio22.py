num1=int(input("Ingresa primer valor: "))
num2=int(input("Ingresa segundo valor: "))
num3=int(input("Ingresa tercer valor: "))
if num1==num2 and num2==num3 and num3==num1:
	suma=num1+num2
	resultado=suma*num3
	print("Todos son iguales")
	print(resultado)
else:
	print("Ninguno es igual")
	
