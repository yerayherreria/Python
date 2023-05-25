'''
Boletín 6 Bucles

Realizado por: Yeray Herrería Oña 
'''
#Ejercicio 1

for variable in range(0,101,1):
    print (variable)
    
    if variable % 7 == 0 and variable % 13 == 0:
        print (f"El número {variable} es múltiplo de 7 y 13.")
    
    elif variable % 7 == 0:
        print (f"El número {variable} es múltiplo de 7.")
    
    elif variable % 13 == 0:
        print (f"El número {variable} es múltiplo de 13.")