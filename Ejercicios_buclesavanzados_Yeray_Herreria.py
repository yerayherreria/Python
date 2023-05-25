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


#Ejercicio 5

n= int(input("Escribe un número:"))
mensaje=""

while n!=1:       
    if n%2!=0:
        n=n*3+1  
    else:
        n=n//2
    
    if n!=1:    
        mensaje=mensaje+ str(n)+"->"
    else:
        mensaje=mensaje+ str(n)
        
print(mensaje)

#Ejercicio 6

n= int(input("Escribe aquí la edad:"))

acumdinero=0
acumpuzzle=1
acum=20

while n<=0:
    n= int(input("Error.La edad tiene que ser mayor que 0.Escribe aquí la edad:"))

for i in range (1,n+1):   
    if i!=1 and i%2!=0:
        acumpuzzle=acumpuzzle*2+1
    
    if i==2:
        acumdinero=20
    elif i!=2 and i%2==0:
        acumdinero=acumdinero+15
        acum=acum+acumdinero
    
print (f"Juan con {n} de edad tiene {acum}€ y {acumpuzzle} puzzles.")

#Ejercicio 7

n =int(input("Introduce un número:"))

cont=0

for i in range(n):
    cont+=1
    print(f"{n}"*cont)

#Ejercicio 8

f=input("Escribe aquí el tipo de figura(Cuadrado/Triangulo/Rombo):").upper()
t=int(input("Escribe aquí el tamaño de la figura(1-10):"))

while t<1 or t>10:
    t=int(input("Error.Escribe aquí el tamaño de la figura(1-10):"))
while f!="CUADRADO" and f!="TRIANGULO" and f!="ROMBO":
    f=input("Error.Escribe aquí el tipo de figura(Cuadrado/Rectangulo/Rombo):").upper()
    
if f=="CUADRADO":
    for i in range(t):
        print("* "*t)
elif f=="TRIANGULO":
    for i in range(t):
        print(" "*(t-i-1)+"*"*(2*i+1))
else:
    for i in range(t):
        print(" "*(t-i-1)+"*"*(2*i+1))
    for j in range(t-1,0,-1):
        print(" "*(t-j)+"*"*(2*j-1))  
   
#Ejercicio 9

f=input("Escribe aquí el tipo de figura(Cuadrado/Triangulo/Rombo):").upper()
while f!="CUADRADO" and f!="TRIANGULO" and f!="ROMBO":
    f=input("Error.Escribe aquí el tipo de figura(Cuadrado/Rectangulo/Rombo):").upper()

t=int(input("Escribe aquí el tamaño de la figura(1-10):"))
while t<1 or t>10:
    t=int(input("Error.Escribe aquí el tamaño de la figura(1-10):"))

if f=="CUADRADO":
    for i in range(1,t+1):
        mensaje=""
        for j in range(1,t+1):
            if i==1 or i==t or j==1 or j==t:
                mensaje+="* "
            else:
                mensaje+="  "
        print(mensaje)     
elif f=="TRIANGULO":
    for i in range(1,t*2+1,2):
        mensaje=""
        for j in range(t*2-i):
            mensaje+=" "
        for j in range(1,i+1):
            if i==1 or j==i or j==1 or i==t*2-1:
                mensaje+="* "
            else:
                mensaje+="  "
        print(mensaje)
else:
    for i in range(1,t*2+1,2):
        mensaje=""
        for j in range(t*2-i):
            mensaje+=" "
        for j in range(1,i+1):
            if i==1 or j==i or j==1:
                mensaje+="* "
            else:
                mensaje+="  "
        print(mensaje)
    for i in range(1,t*2-1,2):
        mensaje=""
        for j in range(1,i+1):
            mensaje+=" "
        for j in range(t*2-i):
            if j==1 or j==t*2-i-2:
                mensaje+="* "
            else:
                mensaje+="  "
        print(mensaje)
 
#Ejercicio 10

f=input("Escribe aquí el tipo de figura(Cuadrado/Triangulo/Rombo):").upper()
while f!="CUADRADO" and f!="TRIANGULO" and f!="ROMBO":
    f=input("Error.Escribe aquí el tipo de figura(Cuadrado/Rectangulo/Rombo):").upper()

t=int(input("Escribe aquí el tamaño de la figura(1-10):"))
while t<1 or t>10:
    t=int(input("Error.Escribe aquí el tamaño de la figura(1-10):"))

caracter=input("Escribe el caracter que desees:")

if f=="CUADRADO":
    for i in range(1,t+1):
        mensaje=""
        for j in range(1,t+1):
            if i==1 or i==t or j==1 or j==t:
                mensaje+=f"{caracter} "
            else:
                mensaje+="  "
        print(mensaje)     
elif f=="TRIANGULO":
    for i in range(1,t*2+1,2):
        mensaje=""
        for j in range(t*2-i):
            mensaje+=" "
        for j in range(1,i+1):
            if i==1 or j==i or j==1 or i==t*2-1:
                mensaje+=f"{caracter} "
            else:
                mensaje+="  "
        print(mensaje)
else:
    for i in range(1,t*2+1,2):
        mensaje=""
        for j in range(t*2-i):
            mensaje+=" "
        for j in range(1,i+1):
            if i==1 or j==i or j==1:
                mensaje+=f"{caracter} "
            else:
                mensaje+="  "
        print(mensaje)
    for i in range(1,t*2-1,2):
        mensaje=""
        for j in range(1,i+1):
            mensaje+=" "
        for j in range(t*2-i):
            if j==1 or j==t*2-i-2:
                mensaje+=f"{caracter} "
            else:
                mensaje+="  "
        print(mensaje)

'''
#Ejercicio 11

t=int(input("Escribe aquí el tamaño del cuadrado(Mayor que 1):"))
while t<2:
    t=int(input("Error.Escribe aquí el tamaño del cuadrado:"))

mensaje=""
n=0 

  
for i in range(1,t+1):
    for j in range(1,t+1):
        if i<j:
            n=i 
        else:
            n=j

        mensaje=mensaje + str(t-n+1) + " "
 
    for j in range(t-1,0,-1):
        if i<j:
            n=i 
        else:
            n=j

        mensaje=mensaje + str(t-n+1) + " "
        if j==1:
            print(mensaje)
            mensaje=""

for i in range(t-1,0,-1): 
    for j in range(1,t+1): 
        if i<j:
            n=i 
        else:
            n=j
             
        mensaje=mensaje + str(t-n+1) + " "
        
    for j in range(t-1,0,-1): 
        if i<j:
            n=i 
        else:
            n=j 

        mensaje=mensaje + str(t-n+1) + " "
        if j==1:
            print(mensaje)
            mensaje=""
