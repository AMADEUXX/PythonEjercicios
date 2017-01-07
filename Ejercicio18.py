cantpreg=int(input("Cantidad de preguntas totales: "))
correctas=int(input("Cantidad de preguntas correctas: "))
porcentaje=(correctas*100)/cantpreg
if porcentaje>=90:
	print("Tuvo un nivel Maximo")
else:
	if porcentaje>=75 and porcentaje<90:
		print("Tuvo un nivel Medio")
	else:
		if porcentaje>=50 and porcentaje<75:
			print("Tuvo un nivel Regular")
		else:
			if porcentaje<50:
				print("Fuera de Nivel")
				