def all_equal(xs):
    
    equal_count=0
    for i in (xs):
        if i == xs[0]:
            equal_count += 1
        else:
            return False
    if equal_count == len(xs):
        return True
    

