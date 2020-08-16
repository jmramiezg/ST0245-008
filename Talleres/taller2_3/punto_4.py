#Palabra escalera
x = input("Escriba una palabra \n")

def escalera(x):
    a = 1
    for i in x:
        print(x[0:a])
        a = a+1

print(escalera(x))

