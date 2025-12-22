# write your code here
def subtuple(xs, ys):

    if ys==():
        return True
    
    n = len(xs)
    m = len(ys) 
    
    for i in range(n - m + 1):
        if xs[i:i+m] == ys:  
            return True
    return False




