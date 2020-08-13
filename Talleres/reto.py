import time

def get_recursive_factorial(n):
    if n == 1:
        return 1
    else: 
        return n*get_recursive_factorial(n-1)

def get_iterative_factorial(n):
    producto = 1
    for i in range (1, n+1):
        producto *= i
    return producto

start_time = time.time()
get_recursive_factorial(998)
print("Recursion--- %s seconds ---" % (time.time() - start_time))
start_time = time.time()
get_iterative_factorial(998)
print("Iteration--- %s seconds ---" % (time.time() - start_time))

