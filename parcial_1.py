## TI = 1001446527
def tarjeta(n):
    if n==1:
        return 1
    else:
       return str(n)+ " " +str(tarjeta(n-1))

print(tarjeta(27))   

