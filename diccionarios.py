# Guardan datos a partir de una clave y un valor, es mutable


persona={
  "nombre": "Lucas",
  "apellido": "Sanchez",
  "edad": 25
}
#Acceder a un elemento de un diccionario
print(persona["nombre"])

#Añadir un elemento a un diccionario
persona["direccion"]= "Belgrano 345"

#Reasignar el valor de un elemento de un diccionario
persona["nombre"]='Emir'
print(persona)

#Eliminar un valor mediante indice
# del persona["edad"]

print(type(persona))
print(persona)

#acceder a las claves del diccionario
print(persona.keys())

#acceder a los valores del diccionario
print(persona.values())

#acceder tanto a las claves como a los valores del diccionario
print(persona.items())

#eliminar el diccionario
# del persona

#limpiar el diccionario
persona.clear()
print(persona)