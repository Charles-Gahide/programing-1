def valid_parentheses(string):
    count = 0
    for char in string:
        if char == '(':
            count += 1
        elif char == ')':
            count -= 1
        if count < 0:
            return False  # if the count is smaller than 0: too many closing parentheses

    return count == 0  # Must end balanced
