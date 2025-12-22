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
        if direction in self.current_room.exits.keys():
            start_room_name = self.current_room.name
            next_room_name = self.current_room.exits[direction]
            self.current_room = rooms[next_room_name]
            print(f"You move {direction} to {self.current_room.name}")
            self.write_move(direction, self.current_room.name, start_room_name)
        else:
            print("You can't go that way!")

    def write_move(self, direction, room_name, start):
        with open("maze_moves.txt", 'a', encoding='utf-8') as file:
            output = f"You moved {direction} from {start} to {room_name}."
            file.write(output)

def parse_maze_file(filename):
    rooms = {}

    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    current_room = None

    for line in lines:
        if line.startswith("ROOM:"):
            if current_room:
                rooms[current_room] = Room(current_room, description, exits)

            current_room = line.split(":")[1].strip()
            
        elif line.startswith("DESCRIPTION:"):
            description = line.split(":")[1].strip()
        elif line.startswith("EXITS:"):
            exit_data = line.split(":")[1].strip()
            exits = {}
            for pair in exit_data.split(";"):
                direction, destination = pair.split("=")
                exits[direction.strip()] = destination.strip()

    # Save last room
    if current_room:
        rooms[current_room] = Room(current_room, description, exits)

    # Determine start and exit automatically
    if "Entrance" not in rooms or "Exit" not in rooms:
        raise ValueError("Maze must contain 'Entrance' and 'Exit' rooms!")

    return rooms;            

def main():
    rooms = parse_maze_file("maze.txt")

    player = Player(rooms["Entrance"])

    print("Welcome to the Maze Game")
    player.current_room.info()

    play = True

    while play:
                
        command = input("\n Which command?: ").strip().lower()

        if command == "quit":
            print("Thank you for playing")
            play = False

        elif command == "look":
            player.current_room.info()

        elif command.startswith("go "):
            direction = command.split(" ")[1]
            player.move(direction, rooms)
        
        else:
            print("Unknown command. Try <look>, <go direction> or <quit>.")
        
        if player.current_room.name == "Exit":
            print("\n Congratulations! You have found the exit!")
            play = False

main()
