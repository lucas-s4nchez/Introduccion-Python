# Guardan datos a partir de una clave y un valor

persona={
  "nombre": "Lucas",
  "apellido": "Sanchez",
  "edad": 25
}
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