# Trabajar con módulos permite dividir el trabajo en muchos archivos, para que el código sea mas legible por ejemplo

#un modulo es un archivo que contiene codigo relacionado entre sí (funciones,variables,etc)
# ademas de los modulos que nosotros creamos, existen modulos incorporados en python y tambien modulos de terceros
#podemos importar modulos con la sentencia 'import'
#importar el modulo entero
import mimodulo
print(mimodulo.add(2,2))
#poner un nombre alternativo al modulo
import mimodulo as matematicas
print(matematicas.add(2,2))
#importar solo alguna/s funcion/es del modulo
from mimodulo import add

print(add(2,2))
