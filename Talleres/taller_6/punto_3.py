def bublesort(unalista):
    for numPasada in range(len(unalista)-1,0,-1):        
        for i in range (numPasada):
            print("bublesort: ",unalista)
            if unalista[i]>unalista[i+1]:
                temp = unalista[i]
                unalista[i]=unalista[i+1]
                unalista[i+1] = temp

unalista = [47,3,21,32,56,92]
bublesort(unalista)
print(unalista)

def insercion (lista):
    for i in range(1,len(lista)):
        print("insercion:", lista)
        valor_a_ordenar=lista[i]
        while lista[i-1]>valor_a_ordenar and i>0:
            lista[i],lista[i-1] = lista[i-1],lista[i]
            i = i-1
    return lista

lista = [47,3,21,32,56,92]
lista.sort()
print("lista sort",lista)
print(insercion(lista))
