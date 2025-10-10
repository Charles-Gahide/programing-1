# write your code here
def is_valid_month(month):
    if 1<= month <=12:
        return True
    return False

def is_leap_year(year):
    x = year 
    if x%100==0:
        if x%400==0:
            return True
        return False
    elif x%4==0:
        return True
    return False

def has_30_days(month):
    if month==4 or month==6 or month==9 or month==11:
        return True
    return False
    
def has_31_days(month):
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        return True
    return False

def has_28_days(month,year):
    if month==2 and is_leap_year(year)==False:
        return True
    return False

def has_29_days(month,year):
    if month==2 and is_leap_year(year):
        return True
    return False


def is_valid_date(day, month, year):
    if is_valid_month(month)==False:
        return False
    if has_31_days(month):
        return 1 <= day <= 31
    elif has_30_days(month):
        return 1 <= day <= 30
    elif has_29_days(month, year):
        return 1 <= day <= 29
    elif has_28_days(month, year):
        return 1 <= day <= 28
    return False
         

