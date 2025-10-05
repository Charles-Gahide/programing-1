# write your code here
#divide the amount by 10 to remove lsat digit and then round down
from math import floor
def drop_last_digit(n):
    return floor(n/10)