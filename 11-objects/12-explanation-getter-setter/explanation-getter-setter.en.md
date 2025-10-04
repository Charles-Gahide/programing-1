# Getters and Setters

So far, we have seen that:
- A class can have **fields** (attributes).
- Fields can be declared **private** by starting their name with a double underscore (`__`).
- Methods inside the class can access these private fields.

Sometimes, we want to provide **controlled access** to these private fields.  
Instead of letting the user access them directly, we define methods:
- A **getter** to *return* the value of a private field.
- A **setter** to *update* the value of a private field.

By convention, these methods start with `get_` and `set_`.

## Example: Box with getters and setters

In our previous explanation (`explanation-hiding-data`), we already had methods to read and change the value of the field `contents`. We will now change those methods, so they are following our convention for getters and setters:

```python
class Box:
    def __init__(self, contents):
        self.set_contents(contents)

    def get_contents(self):
        return self.__contents
    
    def set_contents(self, contents):
        if self.valid_contents(contents):
            self.__contents = contents
        else:
            raise ValueError()

    def is_empty(self):
        return self.__contents is None

    def valid_contents(self, contents):
        return isinstance(contents, int)
```

## Using getters and setters

```python
b = Box(100)
print(b.get_contents())   # 100

b.set_contents(42)
print(b.get_contents())   # 42
```

## Read-only fields

If we only provide a **getter** (and no setter), the field becomes *read-only* from outside the class.  
This means the value can be accessed, but not modified directly.

## Example: contents as read-only

```python
class Box:
    def __init__(self, contents):
        if self.valid_contents(contents):
            self.__contents = contents
        else:
            raise ValueError()

    def get_contents(self):
        return self.__contents

    def is_empty(self):
        return self.__contents is None

    def valid_contents(self, contents):
        return isinstance(contents, int)
```
## Using getters and setters

```python
b = Box(100)
print(b.get_contents())   # 100

# There is no set_contents method → contents cannot be changed directly
```

## Summary

- **Getter** → method that *returns* a private field (convention: `get_...`).  
- **Setter** → method that *updates* a private field (convention: `set_...`).
- If only a getter exists, the field is read-only from outside the class.  
- They provide controlled access to data and allow validation before changes.  
