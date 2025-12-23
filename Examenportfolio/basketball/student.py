# =========================
# Class: Player
# Represents a single basketball player and their statistics
# =========================
class Player:
    def __init__(self, name, number):
        self.name = name           # Player's full name
        self.number = number       # Jersey number

        # Shooting statistics
        self.FGA = 0   # Field Goals Attempted (inside 3-point line)
        self.FGM = 0   # Field Goals Made (inside 3-point line)
        self.FTA = 0   # Free Throws Attempted
        self.FTM = 0   # Free Throws Made
        self.ThreePA = 0  # 3-Point Shots Attempted
        self.ThreePM = 0  # 3-Point Shots Made

        # Other stats
        self.AS = 0    # Assists
        self.RB = 0    # Rebounds

    # Return all stats as a tuple
    def get_statistics(self):
        return self.FGA, self.FGM, self.FTA, self.FTM, self.ThreePA, self.ThreePM, self.AS, self.RB
    
    # Representation when printing the Player object
    def __repr__(self):
        return f"{self.name} #{self.number}"


# =========================
# Class: Team
# Represents a basketball team containing multiple players
# =========================
class Team:
    def __init__(self, team_name, name_abrv):
        self.team_name = team_name  # Full team name
        self.name_abrv = name_abrv  # Short abbreviation
        self.players = {}           # Dictionary to store players by name   

    # Add a Player object to the team
    def add_player(self, player):
        self.players[player.name] = player

    # Get a player by their jersey number
    def get_player_by_number(self, number):
        for player in self.players.values():
            if player.number == number:     #we store the player as an OBJECT so we can find his number by doing .number (see line 8)
                return player
        return None

    # Return all players as a dictionary
    def get_players(self):
        return self.players

    # Representation when printing the Team object
    def __repr__(self):
        return f"{self.team_name} ({self.name_abrv})"


# =========================
# Class: Match
# Represents a single basketball match containing multiple teams and statistics
# =========================
class Match:
    def __init__(self):
        self.teams = []  # List to store all teams in the match

    # Read team and player data from a file
    def read_match_data_file(self, file_name):
        with open(file_name, 'r', encoding='utf-8') as file:
            current_team = None  # Tracks the current team while reading

            for line in file:
                line = line.strip()  # Remove whitespace
                if not line:
                    continue  # Skip empty lines

                parts = [p.strip() for p in line.split('-')]  # Split line by '-'

                if line[0].lower() == 't':  # If line starts with 't', it's a team
                    current_team = Team(parts[1], parts[2])
                    self.teams.append(current_team)
                else:  # Otherwise, it's a player
                    if current_team is None:
                        raise ValueError("Player line found before any team line.")

                    player_number = int(parts[0].replace("#", ""))  # Convert number to int
                    player_name = parts[1]

                    player = Player(player_name, player_number)
                    current_team.add_player(player)

    # Read match statistics from a CSV file and update player stats
    def read_match_statistics_file(self, file_name):
        with open(file_name, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue

                parts = [p.strip() for p in line.split(',')]  # CSV split

                team_abbr = parts[0]
                player_number = int(parts[1].replace('#',''))  # Remove '#' from number
                event_type = parts[2]

                # Find the correct team and player
                team = self.get_team_by_abrv(team_abbr)
                if team is None:
                    continue

                player = team.get_player_by_number(player_number)
                if player is None:
                    continue

                # Update stats depending on event type
                if event_type == "FG":
                    player.FGA += 1
                    if parts[3] == "Scored":
                        player.FGM += 1
                elif event_type == "3P":
                    player.ThreePA += 1
                    if parts[3] == "Scored":
                        player.ThreePM += 1
                elif event_type == "FT":
                    player.FTA += 1
                    if parts[3] == "Scored":
                        player.FTM += 1
                elif event_type == "RB":
                    player.RB += 1
                elif event_type == "AS":
                    player.AS += 1

    # Return all teams
    def get_teams(self):
        print(self.teams)
        return self.teams

    # Find a team by abbreviation
    def get_team_by_abrv(self, abrv):
        for team in self.teams:
            if team.name_abrv == abrv:
                return team

    # Build the match boxscore as a string
    def display_match(self):
        line_width = 84
        separator = "-" * line_width
        output = ""

        for team in self.teams:
            output += separator + "\n"
            output += f"| {team.team_name:<80} |\n"
            output += separator + "\n"

            # Header row
            output += (
                "| Nbr | Name                         | FGA | FGM | 3PA | 3PM | "
                "FTA | FTM | AS | RB |\n"
            )

            # Player rows, sorted by jersey number
            for player in sorted(team.players.values(), key=lambda p: p.number):
                output += (
                    f"| #{player.number:<2} | "
                    f"{player.name:<28} | "
                    f"{player.FGA:>3} | "
                    f"{player.FGM:>3} | "
                    f"{player.ThreePA:>3} | "
                    f"{player.ThreePM:>3} | "
                    f"{player.FTA:>3} | "
                    f"{player.FTM:>3} | "
                    f"{player.AS:>2} | "
                    f"{player.RB:>2} |\n"
                )

            output += separator + "\n"

        return output

    # Write the match boxscore string to a file
    def write_match_details(self, file_name):
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(self.display_match())
