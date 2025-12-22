# write your code here
def heatwave(temperature): 
    days_atleast_30=0
    days_in_a_row=0

    for temp in temperature:
        if 25<=temp:
            days_in_a_row +=1
            if temp>=30:
                days_atleast_30 +=1
        else:
            days_in_a_row=0
            days_atleast_30=0
        
        if days_in_a_row>=5 and days_atleast_30>=3:
            return True
    return False
