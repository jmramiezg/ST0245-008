def postorden(pre, ino):
    if pre == "":
        return ""
    if len(pre)==1:
        return pre
    PostOrden = ""
    Ino_izq = ""
    Pre_izq = ""
    Ino_der = ""
    Pre_der = ""
    aux = 0
    while ino[aux] != pre[0]:
        Ino_izq = Ino_izq + ino[aux]
        aux+=1
    aux+=1
    while aux<len(ino):
        Ino_der = Ino_der + ino[aux]
        aux+=1
    aux=0
    for i in pre:
        if i in Ino_izq:
            Pre_izq = Pre_izq + i
        if i in Ino_der:
            Pre_der = Pre_der + i
    PostOrden = PostOrden+postorden(Pre_izq, Ino_izq)+postorden(Pre_der, Ino_der)+pre[0]
    return PostOrden
print(postorden("GEAIBMCLDFKJH", "IABEGLDCFMKHJ"))

#Output = IBAEDLFCHJKMG

