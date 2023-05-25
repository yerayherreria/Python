'''
Boletín 6 Bucles

Realizado por: Yeray Herrería Oña
'''
#Ejercicio 2

n1 = int(input("Ingrese un número entre 0 y 10:"))

if n1>-1 and n1<11:
    for t in range(1,11): 
        print (f"{n1}*{t}={n1 * t}")
    
else:
    print (f"El {n1} esta fuera de los límites.")