### Operadores Numericos ###

print(2 + 2)
print(2 - 1)
print(3 * 4)
print(9 / 3) #devuelven un float
print(3 // 2) #devuelve un int
print(2 + 2.0) # El resultado es de tipo float cuando hay un numero float en la operacion
print(2 ** 3) #calcula la potencia
print(3 % 2) #retorna el resto de la division

#El orden de las operaciones es tal cual como en matematicas (PEMDAS): Paréntesis, Exponentes, Multiplicacion,Division,Suma,Resta

### Operadores Lógicos ###

#Permiten trabajar con valores booleanos
x=True
y= False
#el operador 'and' evalúa si todos los valores de la expresion son verdaderos
print(x and y)

#el operador 'or' evalúa si alguno de los valores de la expresion es verdadero
print(x or y)

#el operador 'not' niega el valor de la expresion
print(not x)

# La prioridad de los operadores logicos es: not, and y or

### Operadores relacionales ###
#Permiten comparar valores y retornan un valor booleano

#Mayor que >
print(5>3)
print('b'>'a')
#Mayor o igual que >=
print(5>=5)
#Menor que <
print(3<5)
print('b'<'c')
#Menor o igual que <=
print(3<=3)
#Igual que
print(8==8)
print('hola'=='hola')
#Diferente de
print(8 != 8)
print('hola'!='chau')

### Operadores de asignacion ###
#Permiten asignar un valor a una variable
edad=25 #asigna 25 como valor de edad
print(edad)
edad += 2 #suma 2 al valor de edad
print(edad)
edad -= 5 #resta 5 al valor de edad
print(edad)
edad *= 3 #multiplica por 3 el valor de edad
print(edad)
#y asi con todos los operadores aritmeticos
