#Son bloques de codigo reutilizales que realizan una sola tarea específica.

#Algunas funciones nativas de python
# len(),input(),print(),dir()

# definir una funcion en python 
def hola_mundo():
  print('Hola Mundo')

# llamar a la funcion que creamos
hola_mundo()

### funciones con parametros:

#parametro: variable que se incluye en la definicion de la funcion para representar y guardar un valor quepodemos pasar cuando llamamos a la funcion
#argumento: valor real que asignamos a un parametro cuando llamamos a una funcion

def mostrar_mensaje(mensaje): #mensaje es el parametro
  print(mensaje) #imprimimos el parametro

#llamo a la funcion con el argumento
mostrar_mensaje('Hola wachin') #'Hola Mundo' es el argumento, es decir, es el valor real del parametro mensaje y lo que se va a imprimir

#funciones con parametros por defecto:
def mostrar_doble(numero=2):
  print(numero * 2)
mostrar_doble()#como no le pase nada el valor por defecto a a ser dos

###funcion con mas de un parametro

def sumar(x,y):
  print(x + y)
sumar(2,6)

###funciones que retornan un valor:
def restar(x,y):
  return x - y

# cuando llame a la funcion y pase los argumentos me va a devolver la resta entre ellos 
resultado= restar(4,2)
print(resultado)

###! funciones anonimas
#  las funciones lambda son también conocidas como funciones anónimas porque se definen sin un nombre.
# La sintaxis para definir una función lambda es la siguiente:

#     lambda parámetros: expresión

# A continuación, te detallo las características principales de una función anónima:

# Son funciones que pueden definir cualquier número de parámetros pero una única expresión. Esta expresión es evaluada y devuelta.
# Se pueden usar en cualquier lugar en el que una función sea requerida.
# Estas funciones están restringidas al uso de una sola expresión.
# Se suelen usar en combinación con otras funciones, generalmente como argumentos de otra función.
# Ejemplo:

cuadrado = lambda x: x ** 2
print(cuadrado(3))