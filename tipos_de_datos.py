
### Integer =>  int ###
print(type(10)) #type() recibe un dato y nos muestra que tipo de dato es

### Float => float ###
print(type(2.5))

### Boolean => bool ###
print(type(True))
print(type(False))

### String => str ###
print(type('Soy un string'))
#Los strings tienen indexacion. Cada caracter del string tiene asignado un indice, comienza desde 0.
nombre = 'Lucas'
print(nombre[0])
print(nombre[1])
print(nombre[2])
print(nombre[3])
print(nombre[4])

### List ###
numeros=[10,20,30,40]
saludos= ['Hola', 'Como estas'] 
mixto=[1,'hola',True]
print(type(numeros))
print(type(saludos))
print(type(mixto))

### Tuples ###
autos= ('Ford', 'Ferrari', 'Audi')
print(type(autos))

### Dictionary => dict ###
persona= {
  "nombre": "Ryan",
  "apelido": "Garcia",
  "edad": 30
}
print(type(persona))

### None => NoneType ###
print(type(None))