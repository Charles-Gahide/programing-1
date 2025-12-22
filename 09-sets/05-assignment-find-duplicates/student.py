def find_duplicates(xs):
    seen=set()
    duplicates=set()
    for i in xs:
        if i not in seen:
            seen.add(i)
        else:
            duplicates.add(i)
    return list(duplicates)