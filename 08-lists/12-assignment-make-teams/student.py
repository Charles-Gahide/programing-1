def make_teams(participants, team_size):
    # If team_size is invalid or larger than participants, just one team
    if team_size <= 0 or team_size >= len(participants):
        return [participants[:]]
    
    teams = []
    n = len(participants)
    index = 0
    
    # Create base teams
    while index + team_size <= n:
        teams.append(participants[index:index+team_size])
        index += team_size
    
    # Distribute leftovers across existing teams
    leftover = participants[index:]
    for i, person in enumerate(leftover):
        teams[i % len(teams)].append(person)
    
    return teams