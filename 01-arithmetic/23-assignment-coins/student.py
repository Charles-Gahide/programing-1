# write your code here
def coins(amount):
    coins5 = amount//5
    remaining = amount - (coins5 *5)
    
    coins2 = remaining //2
    remaining = remaining - (coins2 *2)
    
    coins1 = remaining 
    return (coins1 + coins2 + coins5)
    
    
    
#def coins1(amount):
    x=coins(amount)
    remaining = amount-(x*5)
    return(remaining//2)
    
#def coins2(amount):
    x=coins(amount)
    y=coins1(amount)
    remaining = amount-(x*5)-(y*2)
    return (remaining)

