def quick_sort(lista):
    izquierda = []
    derecha = []
    centro = [] # Siempre sera una lista de un solo elemnto
    
    if len(lista)>1:
        pivote = lista[len(lista)-1]
        for i in lista:
            if i<pivote:
                izquierda.append(i)
            elif i  == pivote:
                centro.append(i)
            else:
                derecha.append(i)
        return quick_sort(izquierda) + centro + quick_sort(derecha)
    else:
        return lista

lista_a= [38, 50, 23, 37, 56, 36, 54, 56, 4, 7, 36, 18, 38, 38, 3, 49, 46, 52, 31, 36, 9, 27, 45, 11, 48, 41, 11, 49, 15, 46, 45, 42,

 4, 10, 15, 47, 5, 41, 48, 34, 8, 1, 49, 2, 56, 30, 30, 51, 26, 9, 23, 3, 56, 27, 53, 4, 57, 44, 17, 23]

lista_b = [12, 20, 9, 10, 17, 36, 59, 36, 31, 67, 5, 80, 87, 75, 80, 78, 58, 6, 4, 93, 63, 61, 22, 46, 48, 12, 34, 97, 74, 49, 85, 12,

 83, 44, 54, 29, 66, 62, 26, 2, 59, 98, 68, 92, 55, 12, 68, 45, 49, 32, 16, 18, 75, 46, 84, 12, 72, 7, 22, 17, 68, 34, 71, 98, 40, 31, 37,
    94, 40, 24, 78, 91, 17, 12, 50, 5, 92, 51, 38, 39, 78, 74, 98, 25, 66, 48, 3, 29, 41, 7, 64, 98, 29, 13, 75, 74, 84, 16, 48, 10]

print("Lista a ",quick_sort(lista_a))
print("Lista b ",quick_sort(lista_b))

lista_c = lista_a + lista_b
print("lista c: ", quick_sort(lista_c))