# write your code here
def box(string):
    length = len(string)
    print("+" + "-" * (length + 2) + "+")
    print("| " + string + " |")
    print("+" + "-" * (length + 2) + "+")
box("Hello, World!")