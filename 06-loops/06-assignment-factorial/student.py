def factorial(n):
    result = 1
    for i in range(2, n + 1): #from 2 to n, range doesnt include n so we add +1
        result *= i  # multiply result by i, wich will first be 2, then 3, then 4, up to n
    return (result)
factorial(5)
factorial(0)