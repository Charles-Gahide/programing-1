def matching_brackets(string):
    new_string = []
    pairs = {')': '(', ']': '[', '}': '{'}
    
    for ch in string:
        if ch in "([{":
            new_string.append(ch)
        elif ch in ")]}":
            if not new_string or new_string[-1] != pairs[ch]:
                return False
            new_string.pop()
    
    return len(new_string) == 0
        