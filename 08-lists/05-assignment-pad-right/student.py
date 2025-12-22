def pad_right(xs, length, padding):
    if len(xs) >= length:
        return xs

    if len(xs)!=length:
        padding_needed=length-len(xs)
        for i in range (padding_needed):
            xs.append(padding)
        return xs
    
    
    
print(pad_right([1,2,3,4,5],10,"x"))