def to_roman(n):
    num = (1000, 900, 500, 400,
           100, 90, 50, 40,
           10, 9, 5, 4, 1)
    roman_num = ("M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV", "I")
    
    value_in_roman = ""
    i = 0
    while n > 0:
        if n >= num[i]:
            value_in_roman += roman_num[i]
            n -= num[i]
        else:
            i += 1
    return roman_num