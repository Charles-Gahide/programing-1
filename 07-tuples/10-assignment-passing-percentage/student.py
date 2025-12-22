# write your code here
def passing_percentage(grades):
    passing_grades=0
    failing_grades=0
    for grade in grades:
        if grade<10:
            failing_grades +=1
        else:
            passing_grades +=1
    result=passing_grades/len(grades)*100
    return result

print(passing_percentage((20, 20, 9)))
        