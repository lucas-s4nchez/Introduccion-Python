#los sets son una coleccion desordenada, es decir no tienen indices.
colors={"red","green", "blue"}
print(type(colors))

#Comprobar si un dato existe en el set
print("red" in colors)

#agregar un valor al set
colors.add("yellow") #se agrega al inicio del set
print(colors)

#eliminar un valor del set
colors.remove("red")
print(colors)

#eliminar todos los valores del set
# colors.clear()
print(colors)