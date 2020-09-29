#Candidato #1 se representan los votos con 0
#candidato #2 se representan los votos con 1
def ganador (lista):
    votos_1=0
    votos_2=0
    for i in range(len(lista)):
        if lista[i]==1:
            votos_1+=1
        elif lista[i]==0:
            votos_2+=1
        else:
            pass
    if votos_1>votos_2:
        print("El ganador es el candidato #1")
    else:
        print("El ganador es el candidato #2")
    
    return votos_1,votos_2

lista = [0,1,1,0,1,0,1,1,1,0,1,0,1,0,1,0,0,0,1,0,1,0,1,0,1,0,0,0,1,0,1,0,1,1,0,3,3,3,0,0,0,1,1,1,0,1,0,1,0,1,1,1,0,1,0,1,0,1,0,1,1,1]
print(ganador(lista))