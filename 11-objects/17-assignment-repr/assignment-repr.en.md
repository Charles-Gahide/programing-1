# `__repr__`
For this exercise, you'll be making a `Pokemon` class. We will implement it step by step.

## `TASK`
Create a class `Pokemon`.

* It should have three fields: `number`, `name` and `type`.
* The constructor should allow the user to initialize these fields.

## USAGE

```python
>>> bulbasaur = Pokemon(1, "Bulbasaur", "Grass-Poison")
>>> bulbasaur.name
Bulbasaur

>>> charmander = Pokemon(4, "Charmander", "Fire")
>>> charmander.type
Fire

>>> squirtle = Pokemon(7, "Squirtle", "Water")
>>> squirtle.number
7
```

## `TASK`

Add the proper method to return an unambiguous string representation of the object so when we try to print a `Pokemon` object, it will show us relevant information.

## USAGE

```python
>>> bulbasaur = Pokemon(1, "Bulbasaur", "Grass-Poison")
>>> print(bulbasaur)
Pokemon(1, "Bulbasaur", "Grass-Poison")

>>> charmander = Pokemon(4, "Charmander", "Fire")
>>> print(charmander)
Pokemon(4, "Charmander", "Fire")

>>> squirtle = Pokemon(7, "Squirtle", "Water")
>>> print(squirtle)
Pokemon(7, "Squirtle", "Water")
```