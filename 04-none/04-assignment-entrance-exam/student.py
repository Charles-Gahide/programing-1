def entrance_exam(grade1, grade2, grade3, grade4, grade5):
    skipped_tests = 0
    if grade1 is None:
        skipped_tests + 1
    if grade2 is None:
        skipped_tests + 1
    if grade3 is None:
        skipped_tests + 1
    if grade4 is None:
        skipped_tests + 1
    if grade5 is None:
        skipped_tests + 1

    if skipped_tests > 1:
        return False

    taken_tests=5
    if grade1 is None:
        taken_tests -1
    if grade2 is None:
        taken_tests - 1
    if grade3 is None:
        taken_tests - 1
    if grade4 is None:
        taken_tests - 1
    if grade5 is None:
        taken_tests - 1
    if taken_tests<4:
        return False

    total_grade=grade1+grade2+grade3+grade4+grade5 
   
    if (total_grade)/taken_tests>=12:
        return True
    else:
        return False