#Las tuplas son muy similares a las listas, pero a diferencia de ellas, las tuplas son inmutables , es decir, no se pueden modificar
#La ventaja de las tuplas es que son mas seguras y rapidas que las listas

tupla_demo= (1,2,'hola',True,[30,40,50])
print(tupla_demo)

#Crear una tupla ,mediante una funcion constructora
tupla_numeros= tuple((10,20,30,40,40))
print(tupla_numeros)

#Para crear una tupla de un solo elemento se debe agregar una coma al final
tupla_solitaria=(1,)
print(tupla_solitaria)

#Acceder a un elemento de una tupla
print(tupla_numeros[2])

#Encontrar un elemento en una tupla
2 in tupla_numeros

#obtener el indice de cierto valor de la tupla
print(tupla_numeros.index(20))

#saber cuantas veces se repite un valor en una tupla
print(tupla_numeros.count(40))
