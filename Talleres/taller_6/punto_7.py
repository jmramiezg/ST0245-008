def negativos(lista):
    lista_nueva=[]
    for i in range(len(lista)):
        if lista[i]<0:
            lista_nueva.append(lista[i])
            i+=1
        else:
            i+=1
    return lista_nueva

lista = [1,2,5,6,7,-2,1,-8,-7,-4,-2]

print(negativos(lista))