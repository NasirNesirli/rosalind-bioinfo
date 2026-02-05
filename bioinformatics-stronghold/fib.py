def fibonacci_rabbits(n:int, k:int):
    
    if n == 1:
        result = 1
    elif n == 2: 
        result = 1
    else:
        result = fibonacci_rabbits(n - 1, k) + k * (fibonacci_rabbits(n - 2, k))
    
    return result
 
print(fibonacci_rabbits(34, 4))