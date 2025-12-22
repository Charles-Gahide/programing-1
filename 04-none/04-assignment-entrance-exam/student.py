def entrance_exam(grade1, grade2, grade3, grade4, grade5):

    skipped_tests = 0
    taken_tests = 0
    total_grade = 0

    if grade1 is None:
        skipped_tests += 1
    else:
        total_grade += grade1
        taken_tests += 1

    if grade2 is None:
        skipped_tests += 1
    else:
        total_grade += grade2
        taken_tests += 1

    if grade3 is None:
        skipped_tests += 1
    else:
        total_grade += grade3
        taken_tests += 1

    if grade4 is None:
        skipped_tests += 1
    else:
        total_grade += grade4
        taken_tests += 1

    if grade5 is None:
        skipped_tests += 1
    else:
        total_grade += grade5
        taken_tests += 1


    if skipped_tests > 1 or taken_tests < 4:
        return False
    
   
    average = total_grade/taken_tests
    return average>=12
        
    
