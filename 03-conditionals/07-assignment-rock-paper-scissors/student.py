# write your code here

#rock=0
#paper=1
#scissor=2

def rock_paper_scissors(player1_chocie, player2_choice):
    p1=player1_chocie
    p2=player2_choice   
    if p2+2==p1:        #activates when player2 picked rock(0) en player1 picked scissors(2)
        return 2
    elif p1+2==p2:      #same thing but player1 picks rock and player2 picks scissors
        return 1
    elif p2+1==p1:      #activates when player2 picked a value that is one lower than player1
        return 1
    elif p1+1==p2:      #activates when player1 picks a value that is one lower
        return 2
    else:
        return 0

print(rock_paper_scissors(1,2))
