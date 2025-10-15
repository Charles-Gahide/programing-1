
def player_movement(position, left_arrow ,right_arrow, shift):
    if left_arrow==True and right_arrow== True:
        return position         #makes you not move if both keys are pressed at the same time
    
    if left_arrow==True:
        if shift==True:
            return position-2
        return position-1       #makes you go left by 2 if holding shift, and 1 if not
    
    elif right_arrow==True:
        if shift==True:
            return position+2
        return position+1       #same thing but to the right
    
    else:
        return position         #dont move if no keys are pressed
    