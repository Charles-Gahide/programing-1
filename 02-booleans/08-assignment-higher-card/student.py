# write your code here
def higher_card(c1,c2):
    if c1==c2:
        return False
    elif c1==1:
        return True
    elif c1>c2:
        if c2==1:
            return False
        return True
    return False