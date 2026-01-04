class Team:
    def __init__(self, name):
        self.name = name
        self.matches_played = 0
        self.matches_won = 0
        self.matches_tied = 0
        self.matches_lost = 0
        self.total_goals = 0
        self.total_goals_against = 0
        self.total_points = 0

    def goal_difference(self):
        return self.total_goals - self.total_goals_against

    def play(self, team, goals, opponent_goals):
        self.matches_played += 1
        team.matches_played += 1

        self.total_goals += goals
        team.total_goals += opponent_goals

        self.total_goals_against += opponent_goals
        team.total_goals_against += goals

        if goals == opponent_goals:
            self.matches_tied += 1
            team.matches_tied += 1
            self.total_points += 1
            team.total_points += 1
        elif goals > opponent_goals:
            self.matches_won += 1
            team.matches_lost += 1
            self.total_points += 3
        else:
            self.matches_lost += 1
            team.matches_won += 1
            team.total_points += 3


class Competition:
    def __init__(self):
        self.team_list = {}

    def add_team(self, team_name):
        if team_name not in self.team_list:
            self.team_list[team_name] = Team(team_name)

    def get_team_by_name(self, name):
        return self.team_list[name]

    def update_competition(self, matches):
        for team1_name, team2_name, goals1, goals2 in matches:
            self.add_team(team1_name)
            self.add_team(team2_name)
            team1 = self.get_team_by_name(team1_name)
            team2 = self.get_team_by_name(team2_name)
            team1.play(team2, goals1, goals2)

    def display_table(self):
        table = f"{'Team':<18} | Pld | Won | Tie | Lst | Gls+ | Gls- | Diff | Pts\n"
        for team in self.team_list.values():
            table += f"{team.name:<18} | {team.matches_played:<3} | {team.matches_won:<3} | {team.matches_tied:<3} | {team.matches_lost:<3} | {team.total_goals:<5} | {team.total_goals_against:<5} | {team.goal_difference():<4} | {team.total_points}\n"
        return table

    def write_table(self, filename):
        with open(filename, "w", encoding="utf-8") as file:
            file.write(self.display_table())


def process_match_data(match_data_file_name, output_file_name):
    matches = []
    # Read and parse match data into tuples
    with open(match_data_file_name, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()

            parts = line.replace(":", "-").split("-")
            parts = [p.strip() for p in parts]
            matches.append((parts[0], parts[1], int(parts[2]), int(parts[3])))

    # Create competition, update it, and write the table
    competition = Competition()
    competition.update_competition(matches)
    competition.write_table(output_file_name)


process_match_data("Examenportfolio\\soccer\\match_data.txt","Examenportfolio\\soccer\\output.txt")