'''
Boletín 6 Bucles

Realizado por: Yeray Herrería Oña
'''
#Ejercicio 7

n = int(input("¿Cuántos números desea ingresar?"))
mitad=0

while n<1:
    n = int(input(f"El {n} no es válido,debe ser mayor a 0."))

for n1 in range (n):
    n1 = int(input(f"Ingrese un número mayor que 0:"))
    mitad+=n1

print (f"El medio es {mitad/n}")