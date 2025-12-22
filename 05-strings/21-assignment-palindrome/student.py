# write your code here
def palindrome(string):
    reversed_string = string[::-1]
    if string == reversed_string:
        return True
    return False