#EJERCICIO 1 PYTHON

edad = int(input("Escribe tu edad= "))
peso = float(input("Escribe tu peso= "))

print(f"Tu eso es {edad} tu peso es {peso}")

#EJERCICIO 2 PYTHON

#Triángulo: base * altura / 2
#Rectángulo: base * altura
#Rombo: diagonal 1 * diagonal 2 / 2
#Círculo: Pi * radio a la potencia 2

base = float(input("Dime la base del triangulo= "))
altura = float(input("Dime la altura del triangulo= "))

base * altura /2 

print (f"el area del triangulo es = {base * altura /2 }")

#EJERCICIO 3 PYTHON

A = int(input("Dame el valor A= "))
B = int(input("Dame el valor B= "))

if A>B:
    print(f"El resultado es: {A/B}")
else:
    print(f"El resultado es: {B/A}")
    
#EJERCICIO 4 PYTHON

num1 = int(input("Escribe el valor de num1= "))
num2 = int(input("Escribe el valor de num2= "))
num3 = int(input("Escribe el valor de num3= "))

if num1>num2:
    print(f"{num1} es el mayor")
else:
    if num2>num3:
        print(f"{num2} es el mayor")
    else:
        if num3>num1:
            print(f"{num3} es el mayor")
        else:
            if num1==num2==num3:
                print(f"son iguales")

#EJERCICIO 5 PYTHON

def date_check():

    day = int(input("Escribe el dia"))
    month = int(input("Escribe el mes"))

    day_of_month=[31,28,31,30,31,30,31,31,30,31,30,31]

    if day>day_of_month[month-1]:
        print(f"dia del mes incorrecto")
    else:
        print(f"el dia es {day} y el mes es {month}")
        
        
        
date_check()