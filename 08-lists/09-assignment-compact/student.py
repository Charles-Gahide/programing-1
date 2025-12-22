def compact(xs):
    new_list=[]
    for i in xs:
        if i is not None:
            new_list.append(i)
    return(new_list)
print(compact([1, None, 2, None,3]))
        





def compact_in_place(xs):
    for i in xs[::-1]:
        if i is None:
            xs.remove(i)
            
print(compact_in_place([1, None, 2, None,3]))