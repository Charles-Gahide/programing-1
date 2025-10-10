# Functions

An *algorithm* is a series of instructions that, when followed, achieve a certain goal.
Cooking recipes are an example of algorithms: follow the recipe's steps and you'll end up with a (hopefully) delicious dish.
A programming language, such as Python, allows you to write down instructions in a way that your computer can understand them.

Recipes are given names: chili con carne, cacio e pepe, larb kai, etc.
The same can be done for algorithms in programming languages: we bundle the instructions together and give them a name.
Such a named group of instructions is called a ***function***.

```python
def my_function():
    instruction1
    instruction2
    instruction3
    ...
```

The code shown above defines a function named `my_function`.

## Return Values

When following a recipe, you end up with some dish.
Similarly, functions can also produce a result.
This result is called the *return value* of the function.

```python
def zero():
    return 0
```

Here we have defined a very simple function that produces `0` as return value.


## Calling a Function

Once you have defined a function, you can *call* it.
This means that you want all instructions contained within the function to be executed.
Calling a function is done with `function_name()`.

You can test this out in the Python shell:


```python
>>> def zero():
...     return 0

>>> zero()
0
```

## Running your own code

So far, we have seen how to define functions, but we have not seen how to actually execute them. Let's say we have this script:

```python
def greet():
  print("Hello, world!")
```

How would we get to see the message `Hello, world!` in our terminal? If we execute this piece of code, we only tell Python that we have defined a function that prints a statement to the console, but we never tell Python to execute this function. 

An easy way to actually run your code, is by **calling your function**. Calling a function is done with `function_name()`. 

```python
def greet():
  print("Hello, world!")

greet()
```

This way, Python will define the function in the first two lines. In the last line, you will actually run the function. This means that you want all instructions contained within the function to be executed. In this case,  you will see `Hello, world!` in the console. To execute your own scripts, you can just click the "play" button in the top right corner of your editing window. 

### Showing your results in the terminal

If you want to actually see what the return value is of a function, you will have to print it to the terminal, otherwise Python will just remember it behind the scenes. 

```python
def zero():
    return 0

zero()
```

The code above will not show you anything. Python will just remember that `zero()` returns `0`, but it will not show you. To actually see it in the terminal, you have to use a print statement, like so:

```python
def zero():
    return 0

print(zero())
```

This will print whatever the function returns, in this case `0`.

### Call your functions after defining them

Python is peculiar when it comes to line sequencing. You have to define your functions before you can call them. For instance, if we would run this script:

```python
greet()

def greet(): 
    print("Hello, world!")
```

We would get this error:

```python
Traceback (most recent call last):
  File "example.py", line 1, in <module>
    greet()
    ^^^^^
NameError: name 'greet' is not defined
```

Be aware to put your function calls **below** your function definitions. 