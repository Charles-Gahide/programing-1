def remove_all(xs,item_to_remove):
    for i in xs[::-1]:
        if i==item_to_remove:
            xs.remove(i)
