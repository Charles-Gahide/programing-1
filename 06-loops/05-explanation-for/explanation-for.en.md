# For Loop

A very common loop pattern is


```python
i = 0
while i < i_max:
    # ...
    i += 1
```



In other words, the loop body is executed for every value from `0` to `i_max` (where `i_max` must of course be a variable defined somewhere before the loop starts.)
Such loops occur so often that many programming language provide a separate looping construct for it.
Python is no exception:


```python
for i in range(0, i_max):
    # ...
```



Meet the `for` loop.
The loop shown above makes `i` go through all values of the `range(0, i_max)`, i.e., `0`, `1`, `2`, &hellip; `i_max - 1`.
Note: the variable name `i` can be freely chosen.

### `IMPORTANT`
Note that `range(start, stop)` does not include `stop` itself.


### `EXAMPLE`


```python
>>> for i in range(0, 3):
...    print(i)
0
1
2
```

## `range`

`range` exhibits a lot of similarities with slicing.

* `range(start, stop)` represents all integers from `start` to `stop` (exluding `stop` itself).
* `range(start, stop, step)` goes from `start` to `stop` with increments of `step`.
* `range(stop)` is the same as `range(0, stop)`.
* Negative `step` allows you to count backwards.

## Debugging loops

Sometimes your loops will not run the way you want them to run. They will end too soon or each iteration will do something you didn't intend it to do. In these cases, print statements can generally work pretty well to find out where your code goes wrong. 

```python
for index in range(0,x):
    result = 0
    #some code here that changes the result
    print(f"During iteration {index} the result is {result}.")
```

This way, you will see what every intermediate result is. Whenever it deviates from what it should be, you can check what's happening there. You will also see when your loop ends, which can be handy because often your loop will run for too long or too short, especially while-loops.