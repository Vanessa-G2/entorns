#EJERCICIO 1 PYTHON

A = int(input("Pon el valor de A = "))
B = int(input("Pon el valor de B = "))

print(f"Antes del intercambio de A y B : A = {A}, B = {B}")

A, B = B, A

print(f"despues de intercambiar A y B: A= {A}, B= {B}")

#EJERCICIO 2 PYTHON

print (f"El resultado es = {A + B }")
print (f"El resultado es = {A - B }")
print (f"El resultado es = {A * B }") 
print (f"El resultado es = {A / B }")

#EJERCICIO 3 PYTHON

if A > B:
    print(f"Menor: {A} Mayor: {B}")
    
elif A < B:
    print(f"Menor: {A} Mayor: {B}")
else:
    print("Los dos números son iguales.")

# EJERCICIO 4 PYTHON

A = int(input("Pon el valor de A = "))
B = int(input("Pon el valor de B = "))
C = int(input("Pon el valor de C = "))

if A==B and B==C: #Aqui me estoy refiriendo que si son iguales muestre cualquiera
    
    print(f"Son iguales , el numero es : ", A)
else:
    if A>B and A>C: #Aqui si es mayor que B y C que muestre que el valor A es el mayor
        
            print(f"La mayor es " , A)
    else:
        if B>A and B>C: #Aqui si es mayor que A y C que muestre que el valor B es el mayor
            
            print(f"La mayor es : " , B)
        else:
            if C>A and C>B: #Aqui si es mayor que A y B que muestre que el valor C es el mayor
                
                print(f"La mayor es : " ,C)

#EJERCICIO 5 PYTHON 

numero1 = int(input("Pon el valor de numero1 = "))
numero2 = int(input("Pon el valor de numero2 = "))
numero3 = int(input("Pon el valor de numero3 = "))

if numero1<0: #Aqui mira que si es negativo , hace el calculo del producto (OJO SI ES EL PRIMER NUMERO NEGATIVO)
    
    resultado = numero1 * numero2 * numero3
    
else: #Y si no que los sume , como nos pide el ejercicio
    
    resultado = numero1 + numero2 + numero3
    
    print ("El resultado es ", resultado)
    
#EJERCICIO 6 PYTHON

numero = float(input("pon el numero: "))

if numero <= 0:
    print(f"Error: El número tiene que ser mayor que 0.")
    exit() # con el exit me sacara del programa si el número es 0 o menor

# Si el número es mayor que 0, el programa sigue

cuadrado = numero ** 2 #Aqui le saco la potencia

raiz = numero ** 0.5 #Aqui el cuadrado

print(f"del numero que has puesto {numero}, la potencia es {cuadrado} y la raíz es {raiz}") #OJO ACUERDATE DE PONER SIEMPRE {} y la variable que quieres que la información que se muestre 