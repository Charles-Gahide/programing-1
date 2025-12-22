def remove_runs(ns):
    if not ns:
        return []
    result = [ns[0]]
    for x in ns[1:]:
        if x != result[-1]:
            result.append(x)
    return result
    
        