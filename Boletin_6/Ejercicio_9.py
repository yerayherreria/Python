'''
Boletín 6 Bucles

Realizado por: Yeray Herrería Oña
'''

n = int(input("Ingrese un número entero positivo mayor que 0:"))
acum = 0

while n<1:
    print ("Ingrese un número válido,inténtalo de nuevo.")
    
    n = int(input("Ingrese un número entero positivo mayor que 0:")) 
    
for i in range(1,n):
    
    if n%i == 0:
        acum = acum+i

if n==acum:
    print ("El número es perfecto.")
    
else:
    print ("El número no es perfecto.")