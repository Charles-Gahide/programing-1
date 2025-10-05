# write your code here
def coins(amount):
    coins5 = amount//5
    remaining = amount - (coins5 *5)
    
    coins2 = remaining //2
    remaining = remaining - (coins2 *2)
    
    coins1 = remaining 
    return (coins1 + coins2 + coins5)
    
    
    


