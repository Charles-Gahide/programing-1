def remove_empty_lines(source, destination):
    with open(source, 'r', encoding='utf-8') as infile:
        with open(destination, 'w', encoding='utf-8') as outfile:
            for line in infile:
                if line.strip("\n") != "":
                    outfile.write(line)