def increasing(ns):
    for i in range(len(ns)-1):
        if ns[i] > ns[i+1]:
            return False
    return True