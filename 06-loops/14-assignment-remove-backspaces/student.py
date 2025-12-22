def remove_backspaces(string):
    result = []
    for char in string:
        if char == '\b':
            if result:
                result.pop()
        else:
            result.append(char)
    return ''.join(result)