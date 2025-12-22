def ranking_table(ranking):
    # Step 1: Sort by time
    sorted_list = []
    for runner in ranking:
        inserted = False
        for i in range(len(sorted_list)):
            if runner[1] < sorted_list[i][1]:
                sorted_list.insert(i, runner)
                inserted = True
                break
        if not inserted:
            sorted_list.append(runner)
    
    # Step 2: Build table with positions
    table = []
    pos = 1
    for i in range(len(sorted_list)):
        name, time = sorted_list[i]
        table.append((pos, name, f"{time:.2f}"))  # format timing with 2 decimals
        pos += 1
    
    # Step 3: Determine column widths
    rank_width = max(len(str(row[0])) for row in table)
    name_width = max(len(row[1]) for row in table)
    time_width = max(len(row[2]) for row in table)
    
    # Step 4: Format rows
    lines = []
    for row in table:
        rank, name, time = row
        line = f"{str(rank).rjust(rank_width)} {name.ljust(name_width)} {time.ljust(time_width)}"
        lines.append(line)
    
    return "\n".join(lines)



print(ranking_table([ 
    ('Max Park', 3.13),
    ('Yusheng Du', 3.47),
    ('Tymon Kolasiński', 3.85),
    ('Jode Brewster', 3.88),
    ('Asher Kim-Magierek', 3.89),
    ('Yiheng Wang', 3.90),
    ('Luke Garrett', 3.95),
    ('Max Siauw', 4.03),
    ('Ruihang Xu', 4.06),
    ('Sean Patrick Villanueva', 4.11)
]))

