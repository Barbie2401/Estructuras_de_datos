#Desafio 3

#Crear lista con fechas importantes
list_fechas=[['2021-01-01', "11:00", "Levantarse y ejercitar"],
 ['2021-05-01', "15:00", "No trabajar"],
 ['2021-07-15', "13:00", "No hacer nada es feriado"],
 ['2021-09-18', "16:00", "Ramadas"],
 ['2021-12-25', "00:00", "Navidad"]]
 
#Imprimir lista creada
# print (list_fechas)

#Agregar nueva fecha a la lista
list_fechas.append(['2021-02-02','06:00','Empezar el año'])

#Imprimir lista nueva
# print(list_fechas)

#Editar una fecha de la lista
list_fechas[2][0]='2021-07-16'

#Imprimir lista nueva y verificamos el cambio
# print(list_fechas)

#Eliminar el evento del día del trabajo
list_fechas.remove(['2021-05-01', "15:00", "No trabajar"])

#Imprimir lista nueva y verificamos el cambio
# print(list_fechas)

#Agregar fechas: Navidad y año nuevo, ambas a las 22 hrs.
list_fechas.append(['2021-12-24','22:00','Cena de Navidad'])
list_fechas.append(['2021-12-31','22:00','Cena de Año Nuevo'])

#Imprimir lista nueva y verificamos el cambio
# print(list_fechas)

#Ordenamos la lista por orden de menor a mayor
list_fechas.sort()

# #Imprimos el resultado final
print(list_fechas)
