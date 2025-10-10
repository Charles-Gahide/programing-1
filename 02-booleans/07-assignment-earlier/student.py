# write your code here
def earlier(h1, m1, h2, m2):
    if h1<h2:
        return True
    elif h1>h2:
        return False
    elif h1==h2:
        if m1>=m2:
            return False
        elif m1<m2:
            return True
    