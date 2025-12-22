# write your code here
# functions to parse the position from a string in the format "(x, y)"
def parse_position_x(string):
    return float(string[1:string.find(",")])

def parse_position_y(string):
    return float(string[string.find(",")+2:len(string)-1])
    

parse_position_x("(19.112, 254.200)")
parse_position_y("(12.256, 254.200)")