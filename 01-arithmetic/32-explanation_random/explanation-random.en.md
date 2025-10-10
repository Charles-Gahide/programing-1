# Random
Sometimes in programming, we want our programs to behave differently each time they are run.  

For example:
- Rolling a dice
- Picking a random card from a deck
- Creating random test data

In Python, we can use the **`random`** module to generate random values.

## Importing the module
Before we can use random functions, we need to **import** the module:

```python
import random
```

## `random.random()`
The simplest random function is:

```python
random.random()
```

It returns a random **floating-point number** between **0.0 and 1.0** (not including 1.0).

Example:

```python
import random

value = random.random()
print(value)   # e.g., 0.37444887175646646
```

## `random.randint(a, b)`

To get a random **integer** between two numbers (inclusive):

```python
random.randint(1, 6)
```

This simulates rolling a dice, because the result will always be an integer between 1 and 6.

Example:

```python
import random

dice = random.randint(1, 6)
print("You rolled:", dice)
```

## Setting the seed: `random.seed()`

By default, random numbers change each time we run the program.  
If we want **reproducible results**, we can set a *seed*:

```python
import random

random.seed(42)    # same seed = same sequence
print(random.randint(1, 10))
print(random.randint(1, 10))
```

Every time you run this code with seed `42`, you will get the same numbers.

## Summary

- `random.random()` → random float in [0.0, 1.0)
- `random.randint(a, b)` → random integer between a and b
- `random.seed(n)` → reproducible randomness

