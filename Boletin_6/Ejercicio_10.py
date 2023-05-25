'''
Boletín 6 Bucles

Realizado por: Yeray Herrería Oña
'''
n = int(input("Ingrese un número entero positivo:"))
acum = 1

while n < 0:
    n = int(input("El número no es válido,inténtalo de nuevo:"))

if n==0 or n==1:
    print ("El factorial es 1.")

else:    
    for i in range(0,n):
        acum = acum + acum*i
        print (acum)