'''
Created on 31 oct 2022

@author: Yeray
'''
'''
#1.1
n1 = input("Introduce la elección del jugador1 (Piedra/Papel/Tijera/Lagarto/Spock):").upper()
n2 = input("Introduce la elección del jugador2 (Piedra/Papel/Tijera/Lagarto/Spock):").upper()

while n1!="PIEDRA" and n1!="PAPEL" and n1!="TIJERA" and n1!="LAGARTO" and n1!="SPOCK":
    n1 = input("Valores Incorrectos.Introduce la elección del jugador1 (Piedra/Papel/Tijera/Lagarto/Spock):").upper()
    
while n2!="PIEDRA" and n2!="PAPEL" and n2!="TIJERA" and n2!="LAGARTO" and n2!="SPOCK":
    n2 = input("Valores Incorrectos.Introduce la elección del jugador2 (Piedra/Papel/Tijera/Lagarto/Spock):").upper()

if n1=="SPOCK":
    if n2=="TIJERA":
        print("Spock gana tijera.")
    elif n2=="PIEDRA":
        print("Spock gana piedra.")
    elif n2=="PAPEL":
        print("Spock pierde contra papel.")
    elif n2=="LAGARTO":
        print("Spock pierde contra lagarto.")
    else:
        print("Empata.")   
elif n1=="TIJERA":
    if n2=="PAPEL":
        print("Tijera gana papel.")
    elif n2=="LAGARTO":
        print("Tijera gana lagarto.")
    elif n2=="SPOCK":
        print("Tijera pierde contra spock.")
    elif n2=="PIEDRA":
        print("Tijera pierde contra piedra.")
    else:
        print("Empata.")
elif n1=="LAGARTO":
    if n2=="SPOCK":
        print("Lagarto gana spock.")
    elif n2=="PAPEL":
        print("Lagarto gana papel.")
    elif n2=="TIJERA":
        print("Lagarto pierde contra tijera.")
    elif n2=="PIEDRA":
        print("Lagarto pierde contra piedra.")
    else:
        print("Empata.")
elif n1=="PAPEL":
    if n2=="PIEDRA":
        print("Papel gana piedra.")
    elif n2=="SPOCK":
        print("Papel gana spock.")
    elif n2=="LAGARTO":
        print("Papel pierde contra lagarto.")
    elif n2=="TIJERA":
        print("Papel pierde contra tijera.")
    else:
        print("Empata.")
elif n1=="PIEDRA":
    if n2=="TIJERA":
        print("Piedra gana tijera.")
    elif n2=="LAGARTO":
        print("Piedra gana lagarto.")
    elif n2=="SPOCK":
        print("Piedra pierde contra spock")
    elif n2=="PAPEL":
        print("Piedra pierde contra papel.")
    else:
        print("Empata.")  
    
#1.2
n1 = input("Introduce la elección del jugador1 (Piedra/Papel/Tijera/Lagarto/Spock):").upper()
n2 = input("Introduce la elección del jugador2 (Piedra/Papel/Tijera/Lagarto/Spock):").upper()

while n1!="PIEDRA" and n1!="PAPEL" and n1!="TIJERA" and n1!="LAGARTO" and n1!="SPOCK":
    n1 = input("Valores Incorrectos.Introduce la elección del jugador1 (Piedra/Papel/Tijera/Lagarto/Spock):").upper()
    
while n2!="PIEDRA" and n2!="PAPEL" and n2!="TIJERA" and n2!="LAGARTO" and n2!="SPOCK":
    n2 = input("Valores Incorrectos.Introduce la elección del jugador2 (Piedra/Papel/Tijera/Lagarto/Spock):").upper()

while n1!="SPOCK" and n2!="SPOCK":
    if n1=="TIJERA":
        if n2=="PAPEL":
            print("Tijera gana papel.")
        elif n2=="LAGARTO":
            print("Tijera gana lagarto.")
        elif n2=="PIEDRA":
            print("Tijera pierde contra piedra.")
        else:
            print("Empata.")
    elif n1=="LAGARTO":
        if n2=="PAPEL":
            print("Lagarto gana papel.")
        elif n2=="TIJERA":
            print("Lagarto pierde contra tijera.")
        elif n2=="PIEDRA":
            print("Lagarto pierde contra piedra.")
        else:
            print("Empata.")
    elif n1=="PAPEL":
        if n2=="PIEDRA":
            print("Papel gana piedra.")
        elif n2=="LAGARTO":
            print("Papel pierde contra lagarto.")
        elif n2=="TIJERA":
            print("Papel pierde contra tijera.")
        else:
            print("Empata.")
    elif n1=="PIEDRA":
        if n2=="TIJERA":
            print("Piedra gana tijera.")
        elif n2=="LAGARTO":
            print("Piedra gana lagarto.")
        elif n2=="PAPEL":
            print("Piedra pierde contra papel.")
        else:
            print("Empata.")  
    n1 = input("Introduce la elección del jugador1 (Piedra/Papel/Tijera/Lagarto/Spock):").upper()
    n2 = input("Introduce la elección del jugador2 (Piedra/Papel/Tijera/Lagarto/Spock):").upper()
print("FIN") 

#2
print ("####################################")
print ("# Bienvenido al IES JACARANDÁ      #")
print ("    1. Alumnos que han entrado")
print ("    2. Alumnos que han abandonado")
print ("    3. Total de alumnos")
print ("    4. Salir")
print ("####################################")
n1= int(input("Escribe tu opcion:"))
acum=0
while n1!=1 and n1!=2 and n1!=3 and n1!=4:
    n= int(input("Opción incorrecta.Escribe tu opcion:"))

while n1!=4:
    if n1==1:
        n2= int(input("Introduce la cantidad de alumnos que entran."))
        acum+=n2
    elif n1==2:
        n3= int(input("Introduce la cantidad de alumnos que entran."))
        acum-=n3
    else:
        print(f"Hay un total de {acum} alumnos.")
    n1= int(input("Escribe tu opcion:"))
print ("Fin del programa")

'''
#3

t= int(input("Introduce el tamaño de la empresa:"))
while t<=0:
    t= int(input("El tamaño de la empresa tiene que ser mayor a 0.Introduce el tamaño de la empresa:"))
cont=0
acum=0
acum1=0
sexoh=0
sexom=0
acume=0
acume1=0
sexoh1=0
sexom1=0
while cont<t:
    edad=int(input("Introduce la edad(18-65):"))
    sexo=input("Introduce el sexo(H-M):").upper()
    lenguaje=input("Introduce el lenguaje(Java-Python)").upper()
    while edad<18 or edad>65:
        edad=int(input("Error.Introduce la edad(18-65):"))
    while sexo!="H" and sexo!="M":
        sexo=input("Error.Introduce el sexo(H-M):").upper()
    while lenguaje!="JAVA" and lenguaje!="PYTHON":
        lenguaje=input("Error.Introduce el lenguaje(Java-Python)").upper()
    print("------------------------------------------")
    if lenguaje=="JAVA":
        acum+=1
        acume+=edad
        if sexo=="H":
            sexoh+=1
        else:
            sexom+=1
    elif lenguaje=="PYTHON":
        acum1+=1
        acume1+=edad
        if sexo=="H":
            sexoh1+=1
        else:
            sexom1+=1
    cont+=1
print(f"El {(acum/t)*acum}% de empleados utilizan Java,de los que {sexoh} son hombres y {sexom} mujeres y su edad media es de {acume/acum} años.")
print(f"El {(acum1/t)*acum1}% de empleados utilizan Python,de los que {sexoh1} son hombres y {sexom1} mujeres y su edad media es de {acume1/acum1} años.")    
    