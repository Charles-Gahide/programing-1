def remove_duplicates(xs):
    seen = set()     # fast membership checks
    result = []      # keeps order
    for x in xs:
        if x not in seen:
            seen.add(x)       
            result.append(x)  # preserves order
    return result