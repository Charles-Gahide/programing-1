# write your code here
def is_capitalized(string):
    if string == "":
        return False
    if len(string) == 1:
        return string.isupper()
    if string[0].isupper() and string[1:].islower():
        return True
    return False