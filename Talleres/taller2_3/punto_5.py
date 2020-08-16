## Palindromo
s = str(input("Escriba una palabra \n"))
def espalindromo(s):
    if len(s) < 2: 
        return True
    if s[0] != s[-1]: 
        return False
    return espalindromo(s[1:-1])

print(espalindromo(s))