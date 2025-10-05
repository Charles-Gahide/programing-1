# write your code here
def next_player(player,player_count):
    x=player
    y=player_count
    next_up= (x+1)%y  # "%" makes it so i can go back to 0
    return(next_up)
    
    
    