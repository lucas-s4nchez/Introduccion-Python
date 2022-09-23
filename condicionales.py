#Instrucciones que se ejecutan dependiende de una condicion booleana

## la sentencia 'if', ejecuta el codigo si la condicion se cumple, si no pasa de largo
if(2==2):
  print('Desde el if')

if(2>10):
  print('No es correcto')

##la sentencia 'else', ejecuta el codigo cuando la condicion del if o elif es false

if(2>20):
  print("Desde el if")
else:
  print('Desde el else')

##la sentencia 'elif', evalua otra condicion cuando la condicion del if es false, puede haber mas de una 

if(2>20):
  print("Desde el if")
elif(3==3):
  print('Desde el elif')
else:
  print('Desde el else')