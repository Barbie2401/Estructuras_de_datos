#Convertidor de Divisas

#importación de librerias
import sys

#Variables que se guardarán en orden indicado [] //El primer elemento es el nombre del archivo = sys.argv[0]
soles_peruanos = float(sys.argv[1])
pesos_argentinos = float(sys.argv[2])
dolar_americano = float(sys.argv[3])
pesos_chilenos =int(sys.argv[4])

#Verificar el tipo de dato entregado
# print(type(sys.argv))
# print(type(pesos_chilenos))

#Calcular nueva divisa
soles_peruanos = soles_peruanos * pesos_chilenos
pesos_argentinos = pesos_argentinos * pesos_chilenos
dolar_americano = dolar_americano * pesos_chilenos


#Diccionario con divisas
divisas={soles_peruanos:'Soles', pesos_argentinos: 'Pesos Argentinos', dolar_americano:'Dólares'}

#imprimir el enunciado de la respuesta
print(f"\nLos ${pesos_chilenos} equivalen a:")

#Crear un bucle con los componentes del diccionario e imprimirlos.
for clave, valor in divisas.items(): 
    print ("%s %s" % (clave, valor))



#python conversiones_5.py 0.0046 0.093 0.0013 10000