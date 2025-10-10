# Fake Casino

### `Task – Roll Dice`
Write a function `roll_dice(n)` that simulates rolling an *n*-sided dice.  
The function should always return an integer between **1** and **n** (inclusive).

`n` is guaranteed to be a positive integer.

Make use of the `randint` function from the `random` module.

### `Usage`

```python
>>> roll_dice(6)
# This number will be different for you, because it is random!
5 

>>> roll_dice(6)
3

>>> roll_dice(6)
1
```

### `TASK - Fake Casino`
We are running a fake casino. Our only goal is to cheat in the dice game and steal money from our customers!
This is only possible if we can predict the "random" sequence of dice rolls. But didn’t we already see a way to influence the random numbers?

Write a function `fake_casino(n)` that:
- Ensures all following dice rolls are based on the number 42 ([After all, 42 is the answer to everything](https://en.wikipedia.org/wiki/42_(number)#The_Hitchhiker's_Guide_to_the_Galaxy)).
- Calls your roll_dice function five times to simulate 5 rolls of a n-sided dice.
- Prints the result of each roll to the terminal.

`n` is guaranteed to be a positive integer.

### `USAGE`

```python
>>> fake_casino(6)
6
1
6
1
3

>>> fake_casino(6)
# The second time you call your function, it should return exact the same numbers!
6
1
6
1
3
```



