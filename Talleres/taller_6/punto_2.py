
def eliminar_ordenados(lista):
    nueva_lista = []
    for i in range(len(lista)):
        if lista[i] not in nueva_lista:
            nueva_lista.append(lista[i])
    return nueva_lista

lista = [3,4,4,5,5,7,7,9,11,11]
print(eliminar_ordenados(lista))

