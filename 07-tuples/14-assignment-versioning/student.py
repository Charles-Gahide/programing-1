def increase_version(version, breaking_change, new_features):
    x,y,z=version
    if breaking_change:
        x+=1
        y=0
        z=0
    elif new_features:
        y += 1
        z = 0
    else:
        z += 1
    return (x,y,z)

print(increase_version((2,5,6),False, True))


def is_more_recent(v1,v2):
    a,b,c=v1
    x,y,z=v2

    if a==x:
        if b>y:
            return True
        elif b==y:
            if c>z:
                return True
    
    elif a>x:
        return True
    return False

print(is_more_recent((2,6,9),(2,5,0)))
            

def is_older(v1, v2): return v1[0] < v2[0] or (v1[0] == v2[0] and (v1[1] < v2[1] or (v1[1] == v2[1] and v1[2] < v2[2])))


def is_more_recent(v1,v2):
    return v1>v2