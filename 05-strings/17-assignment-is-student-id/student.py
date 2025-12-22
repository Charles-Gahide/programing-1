# write your code here
def is_student_id(string):
    if len(string) != 8:
        return False
    if string[0].lower() not in ("s", "r"):
        return False
    if not is_digit(string[1])or not is_digit(string[2]) or not is_digit(string[3]) or not is_digit(string[4]) or not is_digit(string[5]) or not is_digit(string[6]) or not is_digit(string[7]):
        return False
    return True

def is_digit(char):
    return char >= "0" and char <= "9"