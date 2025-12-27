import random

# -------- Location Class --------
class Location:
    def __init__(self, longitude, latitude, name, country):
        self.__longitude = longitude
        self.__latitude = latitude
        self.name = name
        self.country = country
        
    def verify_guess_is_close_enough(self, longitude, latitude):
        # Check if guess is within 1 degree of the real location
        return abs(longitude - self.__longitude) <= 1 and abs(latitude - self.__latitude) <= 1

    def question_hard(self):
        return f"{self.name}:"
    
    def question_easy(self):
        return f"{self.name}, {self.country}:"
    
    def full_info(self):
        return f"{self.country}, {self.name}: ({self.__longitude}, {self.__latitude})"
    
    def get_longitude(self):
        return self.__longitude
    
    def get_latitude(self):
        return self.__latitude

# -------- Game Class --------
class Game:
    def __init__(self):
        self.locations = {}  # {(city, country): Location}
        self.n_rounds = 5
        self.score = 0

    def load_locations_from_file(self, file_name):
        # Read all lines first
        with open(file_name, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        for line in lines:
            parts = [p.strip() for p in line.split(",")]  # strip whitespace
            if len(parts) < 4:
                continue  # skip invalid lines
            city, country, longitude, latitude = parts
            longitude = float(longitude)
            latitude = float(latitude)
            new_location = Location(longitude, latitude, city, country)
            self.locations[(city, country)] = new_location

    def get_score(self):
        return self.score

    def ask_number_of_rounds(self):
        while True:
            try:
                amount_of_rounds = int(input("How many locations would you like to guess? (min=5, max=20): "))
                if 5 <= amount_of_rounds <= min(20, len(self.locations)):
                    self.n_rounds = amount_of_rounds
                    break
                else:
                    print(f"Invalid amount. Enter a number between 5 and {min(20, len(self.locations))}.")
            except ValueError:
                print("Please enter a valid integer.")

    def play_rounds(self):
        if not self.locations:
            print("No locations left to play.")
            return

        attempts = 2
        # Pick a random Location object
        random_location = random.choice(list(self.locations.values()))
        print(f"Location to guess: {random_location.question_hard()}")
        print(f"Attempts left: {attempts}")

        while attempts > 0:
            try:
                longitude_guess = float(input("Longitude guess: "))
                latitude_guess = float(input("Latitude guess: "))
            except ValueError:
                print("Please enter valid numbers for longitude and latitude.")
                continue

            if random_location.verify_guess_is_close_enough(longitude_guess, latitude_guess):
                print(f"Congratulations! Correct! The location was {random_location.full_info()}")
                self.score += 1
                break
            else:
                attempts -= 1
                if attempts > 0:
                    print(f"Incorrect. Try again! Attempts left: {attempts}")
                else:
                    print(f"Out of attempts! The location was {random_location.full_info()}")

        # Remove the location from the pool so it's not asked again
        key_to_remove = None
        for key, loc in self.locations.items():
            if loc == random_location:
                key_to_remove = key
                break
        if key_to_remove:
            del self.locations[key_to_remove]

# -------- Play New Game Function --------
def play_new_game(user):
    print(f"Starting a new game for {user}!\n")
    
    # Create a new game instance
    game = Game()
    
    # Load locations from file
    game.load_locations_from_file("Examenportfolio\\geoGuesser\\locations.txt")
    
    # Ask how many rounds to play
    game.ask_number_of_rounds()
    
    print(f"\nLet's start the game! You will play {game.n_rounds} rounds.\n")
    
    rounds_played = 0
    
    # Play rounds until the number of rounds is reached or no locations left
    while rounds_played < game.n_rounds and game.locations:
        print(f"Round {rounds_played + 1} of {game.n_rounds}")
        game.play_rounds()
        rounds_played += 1
        print("-" * 40)
    
    print(f"\nGame over! {user}'s final score: {game.get_score()} points")


play_new_game("charles")