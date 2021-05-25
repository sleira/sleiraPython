def trabajarLista(lis):
	lis.insert(2,"Sandra")
	print(lis[:])
	lis.extend(["David","Maria","Lucia"])
	print(lis[:])
	lis.append("Hesslher")
	print(lis[:])
	lis.remove("Lucia")
	print(lis[:])

#llamada de la funcion
milista=["sharon","Carlos", "Jose Antonio", "Enrique"]
trabajarLista(milista)