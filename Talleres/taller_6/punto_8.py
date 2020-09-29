def margeSort(lista):
    if len(lista)==1:
        return lista
    izq, der = dividirAlMedio(lista)
    print("Pasada ", lista)
    return mezclar(margeSort(izq), margeSort(der))

def dividirAlMedio(lista):
    middle = len(lista)//2
    return lista[:middle], lista[middle:]

def mezclar(izquierda, derecha):
    mergeList= []
    i=0
    j=0
    while i<len(izquierda) and j<len(derecha):
        if izquierda[i]<derecha[j]:
            mergeList.append(izquierda[i])
            i+=1
        else:
            mergeList.append(derecha[j])
            j+=1
    mergeList.extend(izquierda[i:])
    mergeList.extend(derecha[j:])
    return mergeList

lista = [21, 1, 26, 45, 29, 28, 2, 9, 16, 49, 39, 27, 43, 34, 46, 40] 
print("Esta es la lista final ---->", margeSort(lista))