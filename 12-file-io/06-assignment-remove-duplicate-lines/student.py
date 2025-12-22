def remove_duplicates(source, destination):
    with open(source, 'r', encoding='utf-8') as infile:
        with open(destination, 'w', encoding='utf-8') as outfile:
            previous_line=None
            for line in infile:
                if line != previous_line:
                    outfile.write(line)
                previous_line=line

print(remove_duplicates("C:\\Users\\charl\\Desktop\\UCLL\\Programming\\programing-1\\12-file-io\\test_doc_1.txt","C:\\Users\\charl\\Desktop\\UCLL\\Programming\\programing-1\\12-file-io\\test_doc_2.txt"))
