# write your code here
def domino_chain(dominos):
    if dominos==():
        return True    
    for d in range(len(dominos)-1):

        last_part_firstD=dominos[d][1]
        first_part_secondD=dominos[d+1][0]
        print(last_part_firstD )
        print(first_part_secondD)
        print ("x")
        if last_part_firstD!=first_part_secondD:
            return False
    return True

          

(domino_chain(((2,5),(5,3),(3,4))))

