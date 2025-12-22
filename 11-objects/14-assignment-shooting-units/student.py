# Write your code here
class Unit:
    def __init__(self, health, firepower, armor):
        self.__health = health
        self.__firepower=firepower
        self.__armor=armor

        if health < 0 or firepower < 0 or armor < 0:
            raise ValueError("Health, firepower, and armor must be >= 0")
    
    def get_health(self):
        return self.__health        

    def get_firepower(self):
        return self.__firepower
    
    def get_armor(self):
        return self.__armor

    def shot_by(self, other):

        damage=max(0, other.get_firepower()-self.get_armor())
        self.__health = max(0, self.__health - damage)