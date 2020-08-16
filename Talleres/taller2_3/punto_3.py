##Invertir palabra
s = str(input("Escriba una palabra \n"))
def invertir(s):
    if s == '':
        return s
    else:
        return invertir(s[1:]) + s[0]
    
print(invertir(s))