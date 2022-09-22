myString = "Hola Mundo"
#Los strings tienen indexacion. Cada caracter del string tiene asignado un indice, comienza desde 0.

print(myString[0])
print(myString[1])
print(myString[2])
print(myString[3])
print(myString[4])
#Tambien se pueden cortar partes de un string, selecionando el inicio y el final con los indices, el caracter del final no estará incluido en el nuevo string
print(myString[2:8]) #del 2 al 8
print(myString[2:]) # del 2 hasta el ultimo
print(myString[:8]) # del primero hasta el 8
print(myString[:]) # del principio al final
print(myString[2:8:2]) # del 2 al 8 con paso 2 (de 2 en 2)

##Conocer algunos metodos de string
#print(dir(myString))
print(myString.upper()) #todo a mayúsculas
print(myString.lower()) #todo a minúsculas
print(myString.swapcase()) #cambia las mayusculas a minusculas y viceversa
print(myString.capitalize()) #Primera letra en mayúscula
print(myString.replace("Hola", "Chau"))#Remplaza el primer argumento, por el segundo 
print(myString.count("o"))#Cuenta las veces que se repite cierto caracter o caracteres
print(myString.startswith('Hola')) #Saber si el string empieza con cierto caracter o caracteres
print(myString.endswith('ndo'))#Saber si el string termina con cierto caracter o caracteres
print(myString.split('u'))#Separa el string en base a un caracter (por defecto si no pasas argumento separa por un espacio en blanco)
print(myString.find('u'))#Devuelve el indice del caracter que pasas como argumento
print(len(myString))#Saber la longitud del string
print(myString.index('o'))#Devuelve el indice del caracter que pasas como argumento (igual al find)
print(myString.isnumeric()) #saber si solo tiene caracteres numericos
print(myString.isalnum()) #saber si solo tiene caracteres alfanumericos
print(myString.isalpha()) #saber si solo tiene caracteres alfabeticos
print(myString.isdecimal()) #saber si solo tiene caracteres decimales
print(myString.isdigit()) #saber si solo tiene  digitos
print(myString.islower()) #saber si esta en minúsculas
print(myString.isupper())#saber si esta en mayúsculas