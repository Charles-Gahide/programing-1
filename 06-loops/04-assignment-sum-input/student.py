def sum_input():
    
    sum = 0

    user_input = int(input("Enter Integer: "))
    
    while user_input != 0:
        sum+=user_input
        user_input = int(input("Enter Integer(0 to stop): "))

    input (f"the sum equals {sum}")


sum_input()



















