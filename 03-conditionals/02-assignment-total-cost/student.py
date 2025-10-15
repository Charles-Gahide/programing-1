def total_cost(amount):
    if amount >= 200:
        return (amount-(amount*0.05))
    if amount<100:
        return amount + 10
    return amount
    

print(total_cost(90))
