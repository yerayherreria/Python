'''
Boletín 6 Bucles

Realizado por: Yeray Herrería Oña
'''
#Ejercicio 3

n1 = int(input("¿Cuántos números desea ingresar?"))

while n1<1:
    n1 = int(input(f"El número {n1} no es válido, debe ser mayor a 0:"))

for n in range(n1):
    n1 = int(input("Ingrese un número mayor que 0:")) 
    if n1%2==0:
        print (f"El número {n} es par")
        
    else:
        print (f"El número {n} es impar")