def rpg2(n_sides, goal):

    roll_count = 0
    times_rolled_goal = 0

    for roll in range (1, n_sides +1): #roll from 1 to n_sides
        for roll2 in range (1, n_sides +1): #roll from 1 to n_sides
            roll_count += 1

            if roll+roll2 >= goal: 
                times_rolled_goal += 1 

    print(float(times_rolled_goal/roll_count * 100))
    return(float(times_rolled_goal/roll_count * 100))

rpg2(6,1)




def rpg3(n_sides, goal):

    roll_count = 0
    times_rolled_goal = 0

    for roll in range (1, n_sides +1): #roll from 1 to n_sides
        for roll2 in range (1, n_sides +1): #roll from 1 to n_sides
            for roll3 in range (1, n_sides +1): #roll from 1 to n_sides
                roll_count += 1

                if roll+roll2+roll3 >= goal: 
                    times_rolled_goal += 1 

    print(float(times_rolled_goal/roll_count * 100))
    return(float(times_rolled_goal/roll_count * 100))

