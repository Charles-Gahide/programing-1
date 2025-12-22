class Averager:
    def __init__(self):
        self.values=[]

    def add(self,value):
        self.values.append(value)

    def average(self):
        return sum(self.values) / len(self.values)
    
    def reset(self):
        self.values = []
