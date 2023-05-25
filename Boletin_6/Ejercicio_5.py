'''
Boletín 6 Bucles

Realizado por: Yeray Herrería Oña
'''
#Ejercicio 5

n = int(input("Ingrese un número (negativo para terminar):"))
suma = 0

while n>-1:
    suma += n
    n = int(input("Ingrese un número (negativo para terminar):"))

print(f"Ha ingresado {suma} números positivos.")
    
