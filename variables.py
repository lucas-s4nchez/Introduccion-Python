#El scope de las variables (ambito donde son accesibles) en python puede ser global o local.
#las variables globales son accesibles desde cualquier parte del codigo, las locales solo son accesibles dentro de la funcion donde fueron definidas.

var_global='soy una variable global'
def mi_funcion():
  var_local= 'soy una variable local'
  print(var_global)#si se puede porque es accesible en todo el código (scope global)

#print(var_local) #no se puede porque solo es accesible dentro de la funcion donde fue definida (scope local)

#Declarar varaibles en python
num = 5 
print(num)

#Reasignar variables
num=15

print(num)

#Los nombres de variables deben empezar con una letra o con un guión bajo.
mi_variable='sin guion'
_mi_variable='con guion'
print(mi_variable +' '+ _mi_variable)

#Los nombres de variables no pueden empezar con un número (Error de sintaxis). Ademas solo pueden contener letras, numeros y guion bajo

#Se distingue entre minúsculas y mayúsculas
edad = 20
Edad= 25
EDAD= 30
print(edad)
print(Edad)
print(EDAD)

#Una manera de declarar variables en una sola linea
nombre, apellido = 'Lucas', 'Sanchez'
print(nombre, apellido)

#Convensiones para escribir variables:
snake_case = "snake case"
camelCase= 'camel case'
PascalCase= 'pascal case'
#en python es comun utilizar snake case

#En constantes es una convencion escribirlas en mayúsculas
PI = 3.1416
print(PI)
