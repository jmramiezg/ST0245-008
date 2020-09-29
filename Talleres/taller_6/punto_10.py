def busqueda(matriz,numero):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if numero in matriz[j]:
                return "Si"
    return "no"


matriz = [[1,2,2,2,3,4],[1,2,3,3,4,5],[3,4,4,4,4,6],[4,5,6,7,8,9]]
print(busqueda(matriz,4))