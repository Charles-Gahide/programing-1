def contains_duplicates(xs):
    seen = set()
    for x in xs:
        if x in seen:
            return True
        seen.add(x)
    return False