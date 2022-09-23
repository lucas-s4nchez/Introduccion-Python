#En Python, puedes usar los bloques try y except para manejar estos errores como excepciones.

#algunos errores pueden ser:
# IndexError (usar un índice no válido para acceder a un elemento del iterable.)
# KeyError (usar una clave inexistente de un diccionario)
# ZeroDivisionError (dividir por 0)
# TypeError (tipo de dato incorrecto)

# sintaxis:
# 
# try:
 	# Codigo a ejecutar
 	# Pero podria haber errores en este bloque
    
# except <tipo de error>:
 	# Haz esto para manejar la excepcion
 	# El bloque except se ejecutara si el bloque try lanza un error
    
# else:
 	# Esto se ejecutara si el bloque try se ejecuta sin errores
   
# finally:
	# Este bloque se ejecutara siempre

#Ejemplo de IndexError: 
mi_lista = ["Python","C","C++","JavaScript"]
try:
  print(mi_lista[4])
except IndexError:
  print("Lo siento, el indice esta fuera de rango")

#Ejemplo de KeyError: 
mi_dict ={"clave1":"valor1", "clave2":"valor2", "clave3":"valor3"}
try:
  print(mi_dict["asdasd"])
except KeyError:
  print("¡Lo siento, clave invalida!")

#Ejemplo de TypeError: 
mi_num = "cinco"
try:
  print(10 + mi_num)
except TypeError:
  print("El argumento `mi_num` deberia ser un número")

#Ejemplo de ZeroDivisionError: 
def dividir(x,y):
  return x/y
try:
    res = dividir(5,0)
    print(res)
except ZeroDivisionError:
    print("Trataste de dividir entre cero :( ")