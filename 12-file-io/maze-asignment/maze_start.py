class Room:
    def __init__(self, name, description, exits):
        self.name = name
        self.description = description
        self.exits = exits  # Dictionary: direction -> room name

    def info(self):
        print(f"\n{self.name}")
        print(self.description)
        print("Exits:", ", ".join(self.exits.keys()))


class Player:
    def __init__(self, start_room):
        self.current_room = start_room

    def move(self, direction, rooms):
        pass


def parse_maze_file(filename):
    pass


def main():
    pass

main()
