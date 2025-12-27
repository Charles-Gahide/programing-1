# -----------------------------
# Pokemon class
# -----------------------------
# This class stores information about ONE Pokemon
class Pokemon:
    def __init__(self, number, name, p_type):
        self.number = number        # Pokemon number (e.g. 25)
        self.name = name            # Pokemon name (e.g. Pikachu)
        self.type = p_type          # Pokemon type (e.g. Electric)

        # These tell us what the player has discovered
        self.name_found = False
        self.type_found = False


# -----------------------------
# Pokedex class
# -----------------------------
# This class controls all Pokemon and game logic
class Pokedex:
    def __init__(self):
        # Dictionary to store Pokemon object by name
        self.pokemon_list = {}

    # Add a Pokemon to the Pokedex
    def add_pokemon(self, number, name, p_type):
        self.pokemon_list[name] = Pokemon(number, name, p_type)

    # Get a Pokemon by name
    def get_pokemon_by_name(self, name):
        return self.pokemon_list.get(name)

    # Check the player's guess
    def check_pokemon(self, name, p_type):
        pokemon = self.get_pokemon_by_name(name)

        # If Pokemon does not exist
        if pokemon is None:
            return f"{name} is not a Pokemon"

        # If the name was already found
        if pokemon.name_found:

            # Player guessed name again
            if p_type is None:
                return f"You already found {name}"

            # Player already found the type
            if pokemon.type_found:
                return f"You already know the type of {name}"

            # Wrong type guess
            if pokemon.type != p_type:
                return f"{p_type} is not the correct type for {name}"

            # Correct type guess
            pokemon.type_found = True
            return f"Correct! You found the type of {name}"

        # First time finding the name
        pokemon.name_found = True

        # Name found, no type guessed
        if p_type is None:
            return f"Nice! You found {name}"

        # Name correct, type wrong
        if pokemon.type != p_type:
            return f"You found {name}, but {p_type} is not the right type"

        # Name and type correct
        pokemon.type_found = True
        return f"Awesome! You found {name} and its type"

    # Show the Pokedex
    def print_overview(self):
        print("#" * 30)

        # Sort Pokemon by number
        pokemon_by_number = {p.number: p for p in self.pokemon_list.values()}    # LEFT of : is the key | RIGHT of : is the value


        for number in range(1, 152):
            pokemon = pokemon_by_number.get(number)

            # If Pokemon does not exist
            if pokemon is None:
                print("...")
                continue

            # Show name/type only if found
            name = pokemon.name if pokemon.name_found else "???"
            p_type = pokemon.type if pokemon.type_found else "???"

            print(f"#{number:03d} | {name} | {p_type}")

        print("#" * 30)

    # Save progress to file
    def write_progress(self, filename):
        with open(filename, "w") as file:
            for pokemon in self.pokemon_list.values():
                if pokemon.name_found:
                    if pokemon.type_found:
                        file.write(f"{pokemon.name},{pokemon.type}\n")
                    else:
                        file.write(f"{pokemon.name}\n")


# -----------------------------
# Read Pokemon data from file
# -----------------------------
def read_pokemon_data(filename):
    pokemon_list = []

    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue

            parts = line.split(",")
            if len(parts) != 3:
                continue

            number = int(parts[0].replace("#", ""))
            name = parts[1]
            p_type = parts[2]

            pokemon_list.append((number, name, p_type))

    return pokemon_list


# -----------------------------
# Read saved progress
# -----------------------------
def read_progress_data(filename):
    progress = []

    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue

            parts = line.split(",")
            name = parts[0]
            p_type = parts[1] if len(parts) > 1 else None

            progress.append((name, p_type))

    return progress


# -----------------------------
# Main game
# -----------------------------
def play_game():
    pokedex = Pokedex()

    # Load Pokemon list
    for number, name, p_type in read_pokemon_data("Programing 1\\programing-1\\Examenportfolio\\pokemon\\pokemons.txt"):
        pokedex.add_pokemon(number, name, p_type)   #number name and p_type together are a tuple, the pokemon data is also a tuple so we compare the contents of both tuples (3 things)

    # Load saved progress
    for name, p_type in read_progress_data("Programing 1\\programing-1\\Examenportfolio\\pokemon\\progress.txt"):
        pokemon = pokedex.get_pokemon_by_name(name)
        if pokemon:
            pokemon.name_found = True
            if p_type:
                pokemon.type_found = True

    # Game loop
    while True:
        choice = input(
            "\n(G) Guess Pokemon\n(S) Show Pokedex\n(Q) Quit\nChoice: "
        ).upper()

        if choice == "G":
            name = input("Pokemon name: ")
            p_type = input("Pokemon type (leave empty if unknown): ")
            p_type = p_type if p_type else None
            print(pokedex.check_pokemon(name, p_type))

        elif choice == "S":
            pokedex.print_overview()

        elif choice == "Q":
            pokedex.write_progress("progress.txt")
            print("Progress saved. Bye!")
            break

        else:
            print("Please choose G, S, or Q")


# Start the game
play_game()
