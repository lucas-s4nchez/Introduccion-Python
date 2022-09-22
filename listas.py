#Una lista contiene multiples elementos, y es mutable, es decir puede modificarse.

#Puede contener datos de todo tipo, incluso otras listas.

lista_demo =[23,'edad',True,[1,2,3]]

# Las listas tienen un indice que determina la ubicacion del elemento en la lista, comenzando por 0 para el primer elemento, 1 para el segundo y asi sucesivamente...

#Crear una lista ,mediante una funcion constructora
lista_numeros= list((1,2,3,4,5))
print(lista_numeros)

#Crear una lista ,mediante una funcion constructora y de un rango de numeros
lista_rango= list(range(1,11))#1 al 10
print(lista_rango)



colores= ['rojo','verde','negro','azul', 'rojo']
print(colores)

#Acceder a un elemento de una lista
print(colores[2])

#Reasignar el valor de un elemento de una lista
colores[1]='violeta'
print(colores)

### Algunos metodos de las listas ###
# Longitud de la lista
len(colores)

#conocer si un valor existe en lista
"amarillo" in colores

#agregar un valor al final de la lista
colores.append('blanco')
print(colores)

#agregar mas de un valor a una lista
colores.extend(['naranja','celeste'])
print(colores)

#agregar un valor en determinado lugar en la lista
colores.insert(2,'verde') #lo inserta en el indice 2
print(colores)

#eliminar el último valor de la lista
colores.pop()
print(colores)

#eliminar un valor especifico de la lista mediante indice
colores.pop(2) #elimina el valor de indice 2
print(colores)

#eliminar un valor especifico de la lista mediante valor
colores.remove('violeta') #elimina 'violeta'
print(colores)

#ordena la lista de menor a mayor o alfabeticamente
colores.sort()
print(colores)

#ordena de manera inversa
colores.sort(reverse=True)
print(colores)

#obtener el indice de cierto valor de la lista
print(colores.index('blanco'))

#saber cuantas veces se repite un valor en una lista
print(colores.count('rojo'))

#borrar todos los elementos de la lista
# colores.clear()
print(colores)