# Fake Casino Revisited

### `Task – Generate Number`
Write a function `generate_number(n)` that should always return a floating point number (rounded to 1 digit) between **1** and **n** (inclusive).

`n` is guaranteed to be a positive integer.

### `Usage`

```python
>>> generate_number(10)
# This number will be different for you, because it is random!
5.4

>>> generate_number(10)
10.0

>>> generate_number(10)
1.4
```

### `TASK - Fake Casino Revisited`
We are still running a fake casino. Our goal is to also cheat in the number guessing game and still steal money from our customers!
This is only possible if we also can predict the "random" sequence of generating numbers.

Write a function `fake_casino_revisited(n)` that:
- Ensures all following number generations are based on the number 42 ([After all, 42 is the answer to everything](https://en.wikipedia.org/wiki/42_(number)#The_Hitchhiker's_Guide_to_the_Galaxy)).
- Calls your generate_number function five times
- Prints the result of each generation to the terminal.

`n` is guaranteed to be a positive integer.

### `USAGE`

```python
>>> fake_casino_revisited(10)
6.8
1.2
3.5
3.0
7.6

>>> fake_casino_revisited(10)
# The second time you call your function, it should return exact the same numbers!
6.8
1.2
3.5
3.0
7.6
```