def empty_seats(used_seats):
    total = 0
    for i in range(len(used_seats) - 1):
        a = used_seats[i]
        b = used_seats[i + 1]         
        if b > a + 1:              # only if there’s a gap
            total += (b - a - 1)   # count seats between a and b
    return total