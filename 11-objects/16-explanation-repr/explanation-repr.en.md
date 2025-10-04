# `__repr__`
When we create our own classes in Python, we often want a useful string representation of the objects.  

This is especially important when:
- Printing objects to the terminal
- Debugging
- Working in an interactive Python shell

Python provides a special method for this purpose: **`__repr__`**.

## The role of `__repr__`

- `__repr__` should return an **unambiguous** string representation of the object.  
- Its main purpose is to help **developers** understand the object when they print it or inspect it.  
- Ideally, the string returned by `__repr__` could be copied and pasted back into Python to recreate the same object (if possible).

## Example without `__repr__`

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(2, 3)
print(p)        # <__main__.Point object at 0x000001E8A2F8>
```

By default, Python shows the type and memory address, which is not very helpful.

## Adding `__repr__`

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

p = Point(2, 3)
print(p)        # Point(2, 3)
```

Now the object has a clear and informative representation.

## Summary

- `__repr__` is a special method that returns a string representation of the object.  
- Its purpose is **debugging** and **developer clarity**.  
- By default, objects inherit a `__repr__` that shows the type and memory address.  
- We can redefine `__repr__` to return something more useful, often resembling valid Python code.  
