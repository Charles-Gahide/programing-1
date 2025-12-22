# write your code here
def fix_date(date):
    month = date[0:2]
    day = date[3:5]
    year = date[6:10]
    return (f"{year}/{month}/{day}")


fix_date("07/12/2020")