'''
Bolentín Condicionales Extras

Realizado por:Yeray Herrería Oña
'''
'''
#Ejercicio 1

nota= int(input("Escribe la nota (0-100):"))

if nota<101 and nota>89:
    print ("La nota es de Sobresaliente.")

elif nota<90 and nota>69:
    print ("La nota es de Notable.")
    
elif nota<70 and nota>59:
    print ("La nota es de Bien.")

elif nota<60 and nota>49:
    print ("La nota es de Suficiente.")

elif nota<50 and nota>=0:
    print ("La nota es de Suspenso.")
    
else:
    print ("La nota tiene que estar comprendida entre 0 y 100.")

#Ejercicio 2

fecha = input("Introduzca la fecha actual (dd-mm):")
hemisferio = input("Introduzca el hemisferio (Norte/Sur):").upper()

dia= int(fecha{0:2})
mes= int(fecha{3:5})

if (mes==10 or mes==11) or (mes==9 and 23<=dia<=31) or (mes==12 and 1<=dia<=20:
    if hemisferio=="Norte":
        print ("Se encuentra en la estación de Otoño.")
    
    elif hemisferio=="Sur":
        print ("Se encuentra en la estación de Primavera.")
        
elif (mes==1 or mes==2) or (mes==3 and 1<=dia<=20) or (mes==12 and 21<=dia<=31):
    if hemisferio=="Norte":
        print ("Se encuentra en la estación de Invierno.")
    
    elif hemisferio=="Sur":
        print ("Se encuentra en la estación de Verano.")
    
elif (mes==4 or mes==5) or (mes==3 and 21<=dia<=31) or (mes==6 and 1<=dia<=20):
    if hemisferio=="Norte":
        print ("Se encuentra en la estación de Otoño.")
    
    elif hemisferio=="Sur":
        print ("Se encuentra en la estación de Primavera.")
    
elif (mes==7 or mes==8) or (mes==6 and 21<=dia<=30) or (mes==9 and 1<=dia<=22):
    if hemisferio=="Norte":
        print ("Se encuentra en la estación de Verano.")
    
    elif hemisferio=="Sur":
        print ("Se encuentra en la estación de Invierno.")
    

#Ejercicio 3

fecha = input("Introduzca una fecha (dd-mm-yyyy):")

day= int(fecha[0:2])
month= int(fecha[3:5])
year= int(fecha[6:10])
yearbisiesto= (year%4==0) and (year%100!=0 or year%400==0)
totaldias=0

if month==1 and 1<=day<=31:
    totaldias=day

elif (month==2 and 1<=day) and ((yearbisiesto and day<=29) or not (yearbisiesto and day<=28)):
    totaldias= 31+day

elif month==3 and 1<=day<=31:
    totaldias= 59+day

elif month==4 and 1<=day<=30:
    totaldias= 90+day

elif month==5 and 1<=day<=31:
    totaldias= 120+day

elif month==6 and 1<=day<=30:
    totaldias= 151+day

elif month==7 and 1<=day<=31:
    totaldias= 181+day

elif month==8 and 1<=day<=31:
    totaldias= 218+day

elif month==9 and 1<=day<=30:
    totaldias= 243+day

elif month==10 and 1<=day<=31:
    totaldias= 273+day

elif month==11 and 1<=day<=30:
    totaldias= 304+day

elif month==12 and 1<=day<=31:
    totaldias= 334+day
   
else:
    print ("Valores introducidos no válidos.")
 
if month >2 and yearbisiesto:
    totaldias +=1 

print (f"Han transcurrido {totaldias} días desde el 1 de Enero del {year}")
'''
#Ejercicio 4

grupo1= input("Escriba un grupo sanguíneo (Ej:0):").upper()
grupo2= input("Escriba otro grupo sanguíneo (Ej:AB):").upper()

if grupo1=="A" and (grupo2=="A" or grupo2=="AB" or grupo2=="0"):
    if grupo2=="A":
        print (f"El {grupo1} y {grupo2} son compatibles y puede donar y recibir del {grupo2}.")

    elif grupo2=="AB":
        print (f"El {grupo1} y {grupo2} son compatibles y puede donar al {grupo2}.")
    
    else:
        print (f"El {grupo1} y {grupo2} son compatibles y puede recibir del {grupo2}.")
        
elif grupo1=="B" and (grupo2=="B" or grupo2=="AB" or grupo2=="0"):
    if grupo2=="B":
        print (f"El {grupo1} y {grupo2} son compatibles y puede donar y recibir del {grupo2}.")

    elif grupo2=="AB":
        print (f"El {grupo1} y {grupo2} son compatibles y puede donar al {grupo2}.")
    
    else:
        print (f"El {grupo1} y {grupo2} son compatibles y puede recibir del {grupo2}.")
    
elif grupo1=="AB" and (grupo2=="B" or grupo2=="AB" or grupo2=="0" or grupo2=="A"):
    if grupo2=="AB":
        print (f"El {grupo1} y {grupo2} son compatibles y puede donar y recibir del {grupo2}.")

    elif grupo2=="A":
        print (f"El {grupo1} y {grupo2} son compatibles y puede recibir del {grupo2}.")
    
    elif grupo2=="B":
        print (f"El {grupo1} y {grupo2} son compatibles y puede recibir del {grupo2}.")

    else:
        print (f"El {grupo1} y {grupo2} son compatibles y puede recibir del {grupo2}.")
    
elif grupo1=="0" and (grupo2=="B" or grupo2=="AB" or grupo2=="0" or grupo2=="A"):  
    if grupo2=="0":
        print (f"El {grupo1} y {grupo2} son compatibles y puede donar y recibir del {grupo2}.")

    elif grupo2=="A":
        print (f"El {grupo1} y {grupo2} son compatibles y puede donar al {grupo2}.")
    
    elif grupo2=="B":
        print (f"El {grupo1} y {grupo2} son compatibles y puede donar al {grupo2}.")

    else:
        print (f"El {grupo1} y {grupo2} son compatibles y puede donar al {grupo2}.")

else:
    print(f"El {grupo1} y {grupo2} no son compatibles")