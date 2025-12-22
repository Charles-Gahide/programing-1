class Heating:
    def __init__(self,name,current_temp,min_temp,max_temp):
        self.name=name
        self.min_temp=min_temp
        self.max_temp=max_temp
        self.set_current_temp(current_temp)
    def get_current_temp(self):
        return self.__current_temp
        
    def set_current_temp(self,temp):
        if temp>self.max_temp:
            print("Temp input too high, defaulting to highest possible")
            self.__current_temp=self.max_temp

        elif temp<self.min_temp:
            print("Temp input too low, defaulting to lowest possible")
            self.__current_temp=self.min_temp

        else:
            self.__current_temp=temp

    def change_temperature(self, temp_change):
        new_temp = self.__current_temp + temp_change
        self.set_current_temp(new_temp)

    def __repr__(self):
        return f"Heating('{self.name}', {self.__current_temp:.1f}, {self.min_temp:.1f}, {self.max_temp:.1f})"

device1 = Heating('radiator kitchen', 20, 0, 40)
device2 = Heating('radiator bathroom', 20, 0, 40)
device3 = Heating('radiator living room', 20, 0, 40)
device4 = Heating('radiator bedroom', 20, 0, 40)

print(device1)
device1.change_temperature(-10)
print(device1)
