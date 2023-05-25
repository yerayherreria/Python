'''
Boletín 6 Bucles

Realizado por: Yeray Herrería Oña
'''

n = int(input("Ingrese un número:"))
estado = "S"

while estado=="S":
    n2 = int(input("Ingrese un número:"))
    
    if n2<n:
        n=n2
    
    estado = input("¿Quieres ingresar más números? (S/N)")
    
    while not(estado == "S" or estado == "N"):
        print ("Introduce el valor 'S' o 'N'.")
        estado = input("¿Quieres ingresar más números? (S/N)")

print(f"El numero más pequeño es {n}")
