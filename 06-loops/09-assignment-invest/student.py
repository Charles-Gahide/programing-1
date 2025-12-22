def invest(amount, rate, goal):
    years=0

    while amount < goal:
        amount *= (1 + rate/100) #1 + rate/100 is = 1 + 1, so we are doing amount *2
        years +=1

    print (years)
    return(years)

invest (100,100,400)


