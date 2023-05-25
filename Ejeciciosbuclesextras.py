'''
Boletín 7 Búcles Avanzados I

Realizado por: Yeray Herrería Oña
'''
'''
#Ejercicio 1

n1= int(input("Introduce el primer número:"))
n2= int(input("Introduce el segundo número:"))

dividendo=0
divisor=0
cociente=1
resto=0

if n1==n2:
    print (f"El resultado de la división entre {n1} y {n2} es {cociente} y de resto {resto}.")

else:
    if n1>n2:
        dividendo = n1
        divisor = n2
            
    elif n2>n1:
        dividendo = n2
        divisor = n1

    while dividendo>=divisor:
        dividendo-=divisor
        cociente+=1
    resto=dividendo
print (f"El resultado de la división entre {n1} y {n2} es {cociente} y de resto {resto}.")


#Ejercicio 2

n1= int(input("Introduce un número entero por el que se va ha empezar:"))
n2= int(input("Introduce otro número entero para sacar los múltiplos:"))

cont=0
acum=0
mensaje=""

for i in range(n1,n1+n2):
    if i%n2==0:
        cont=i

while acum<10:
    if acum<9:
        mensaje+=str(cont)+","
    else:
        mensaje+=str(cont)
       
   
    cont+=n2
    acum+=1
print (mensaje)
'''
#Ejercicio 3

n1=1

while n1!=0:
    n1= int(input("Introduce un número:"))
   
    cuadrado=n1*n1
    estado="positivo"
    n="par"
   
    if n1>0:
        if n1%2!=0:
            n="impar"
           
        print (f"El {n1} es {estado},{n} y su cuadrado es {cuadrado}.")
   
    elif n1<0:
        estado="negativo"    
       
        if n1%2!=0:
            n="impar"
           
        print (f"El {n1} es {estado},{n} y su cuadrado es {cuadrado}.")
   
    else:
        print("Fin del programa.")
       

'''
#Ejercicio 4

a=0
b=0
c=0
t=int(input("Escribe el tamaño de la frecuencia:"))
mensaje=""
mensajeb=""
mensajec=""
cont=0

while cont<t:
    a=(-5)**cont
    b=cont%3    
    if b==0:
        b=1
   
    elif b==1:
        b=-1
   
    elif b==2:
        b=0
    c=3**cont
   
    cont+=1
   
    if cont<t:
        mensaje=mensaje+ str(a)+","
        mensajeb=mensajeb+ str(b)+","
        mensajec=mensajec+ str(c)+","
   
    else:
        mensaje=mensaje+ str(a)
        mensajeb=mensajeb+ str(b)
        mensajec=mensajec+ str(c)
       
print(f"a. {mensaje}")
print(f"b. {mensajeb}")
print(f"c. {mensajec}")
'''

#Ejercicio 5

