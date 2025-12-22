def gcd(a, b):
    a, b = abs(a), abs(b)  # Convert both numbers to positive
    while b != 0:
        a, b = b, a % b
    return a

print(gcd(-5, 7))   
print(gcd(-24, -18))  
