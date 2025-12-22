class Pokemon:
    def __init__(self,number,name,type):
        self.number= number
        self.name=name
        self.type=type

    def __repr__(self):
        return(f'Pokemon({self.number}, "{self.name}", "{self.type}")')
    

bulbasaur = Pokemon(1, "Bulbasaur", "Grass-Poison")
charmander = Pokemon(4, "Charmander", "Fire")
squirtle = Pokemon(7, "Squirtle", "Water")

print(bulbasaur,charmander,squirtle)

