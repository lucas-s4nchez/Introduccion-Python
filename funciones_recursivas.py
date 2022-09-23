#Son funciones que se llama a sí misma

#tiene dos elementos fundamentales en su estructura: el caso base, y el caso recursivo
#el caso base es una condicion que permite que la funcion termine su ejecucion.
# El caso recursivo es aquél en el que una función se llama a sí misma, y es el que hace que la recursión continúe hasta que se encuentre con el caso base

# Ejemplo con la secuencia fibonacci 
def fibonacci(n):
  if(n==0 or n==1):
    return n
  else:
    return fibonacci(n-2) + fibonacci(n- 1)
## ingresamos como argumento la posicion en la serie de fibonacci, y obtenemos el valor que tiene esa posicion 
print(fibonacci(7))

#las diez primeras posiciones en la serie fibonacci
for i in range(11):
  print(fibonacci(i))

#Ejemplo de factorial de un número:

def factorial(n):
  if(n<1):
    return 1
  else:
    return n * factorial(n-1)

print(factorial(5))