# write your code here


def hours(duration):
    
    return(duration//3600)

    
def minutes(duration): 
    h=hours(duration)
    remaining = duration-(h*3600)
    return (remaining//60)
    

def seconds(duration):
    h=hours(duration) 
    m=minutes(duration)
    remaining = duration-(h*3600)-(m*60)
    return(remaining)

    