def count_lines_in(path):
    line_count=0
    with open(path,'r', encoding='utf-8' ) as file:
        for line in file:
            if line.strip() != "":
                line_count+=1
    return line_count

print(count_lines_in("C:\\Users\\charl\\Desktop\\UCLL\\Programming\\programing-1\\12-file-io\\test_doc_1.txt"))
      