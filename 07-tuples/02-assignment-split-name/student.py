def split_name(full_name):
    part=full_name.split(" ")
    first_name=part[0]
    last_name=part[1]
    return (first_name, last_name)
print(split_name("John Doe"))