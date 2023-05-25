'''
Boletín 6 Bucles

Realizado por: Yeray Herrería Oña
'''
#Ejercicio 4

n = int(input("Introduzca un número mayor que 0:"))

while n<1:
    n = int(input(f"El {n} no es correcto,inténtalo de nuevo:"))
    
for n1 in range(1,n+1):
    print(f"La suma de los {n} primeros números es: {n+n1}")
    