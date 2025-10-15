# write your code here
def movie_ticket(duration, imax, student, ticket_count):
    if duration<90:
        price=10
        if imax==True:
            price=(10*0.2)+10
        if student==True:
             price=price-3
        return price*ticket_count
        
    elif 90<=duration<120:
        price=11
        if imax==True:
            price=(11*0.2)+11
        if student==True:
             price=price-3
        return price*ticket_count

    elif 120<=duration<150:
        price=12
        if imax==True:
            price=(12*0.2)+12
        if student==True:
             price=price-3
        return price*ticket_count

    elif 150<duration:
        price=15
        if imax==True:
            price=(15*0.2)+15
        if student==True:
             price=price-3
        return price*ticket_count
