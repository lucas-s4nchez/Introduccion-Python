#Son estructuras de control que permiten ejecutar una o vrias lineas de codigo multiples veces

###! For basado en una secuencia númerica:
  #for i in range(incio,final,paso):

#i (puede llamarse como quieras): es la variable que se actualiza en cada iteracion del ciclo
#range: es el rango en el que se ejecuta el ciclo, recibe un valor de inicio, un valor para marcar el final y otro para el paso range(inicio,final,paso) 
# si solo pasas un valor este lo va a tomar como el valor que marca el final del ciclo, el valor de inicio va a ser 0 (por defecto) y el el paso va a ser 1 (por defecto)

#Ejemplo: hacer una iteracion del 1 al 10 con paso 2 (de 2 en 2)
for i in range(1,11,2):
  print(i)

###! For para recorrer los elementos de un objeto iterable (lista, tupla, diccionario, …):
# for <elem> in <iterable>:
# elem: es la variable que toma el valor del elemento dentro del iterador en cada paso del bucle. Este finaliza su ejecución cuando se recorren todos los elementos.
# iterable: es un objeto que se puede iterar sobre él, es decir, que permite recorrer sus elementos uno a uno(lista, tupla, diccionario, …).

#Ejemplo: recorrer una lista e imprimir cada uno de sus elementos
nombres=['Juan','Facundo','Lucas']
for nombre in nombres:
  print(nombre)

#Ejemplo: recorrer las claves del diccionario.
valores = {'A': 4, 'E': 3, 'I': 1, 'O': 0}
for clave in valores:
    print(clave)

#Ejemplo: iterar sobre los valores del diccionario
for valor in valores.values():
    print(valor)

#Ejemplo: iterar a la vez sobre la clave y el valor de cada uno de los elementos del diccionario.
for k, v in valores.items():
    print('clave=', k, ', valor=', v)