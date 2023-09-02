# #Desafio 2

#Importar librerias
import sys

#Abrir un archivo de texto
with open(sys.argv[1],'r') as file:
        texto=file.read()  #Guardar en una variable la lectura del archivo .txt 
        caracteres=len(set(texto))  #Contar los n° de caracteres distintos
        palabras=len(set(texto.split())) #Contar el n° de palabras distintas


#Imprimir resultado
print(f"""\nEl número de caracteres distintos es: {str(caracteres)}.
El número de palabras distintas es: {str(palabras)}\n""")


#python word_count.py lorem_ipsum.txt