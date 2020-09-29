#Elimina duplicados
def repetido(lista):
    lista_nueva=[]
    for i in range(len(lista)):
        if lista[i] not in lista_nueva:
            lista_nueva.append(lista[i])
    return lista_nueva

lista = [4,7,11,4,9,5,11,7,3,5]
lista.sort()
print(lista)
print(repetido(lista))
