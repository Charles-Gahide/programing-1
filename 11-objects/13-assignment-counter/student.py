# Write your code here
class Counter:

    def __init__(self):
        # Initialize the count to 0
        self._count = 0

    def increment(self):
        # Add 1 to the count
        self._count += 1

    def get_count(self):
        # Return the current count
        print (self._count)

    def reset(self):
        # Reset the count to 0
        self._count = 0

counter=Counter()

counter.increment()
counter.increment()

counter.get_count()

counter.reset()

counter.increment()

counter.get_count()