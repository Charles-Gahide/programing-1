# write your code here
def split_in_two(xs):
    if len(xs) % 2 == 0:
        middle=len(xs)//2
    else:
        middle=len(xs)//2+1

    left=xs[:middle]
    right=xs[middle:]
    return(left,right)

    