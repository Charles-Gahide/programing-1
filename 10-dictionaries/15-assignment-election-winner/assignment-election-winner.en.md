# Election Winner

As promised before, we revisit the election problem (chapter 7, assignment 19).
Using `dict`s, it should be easier to solve it.

#### RECAP

An election is held and it's your job to determine who the winner is. You get a sequence of votes. Find out which vote occurs most often.

### `TASK`

Write a function `election_winner(votes)` that returns the winner of the election, i.e., the element of `votes` that occurs most often.

- `votes` is a tuple of strings. 
- If there's a tie between winners, you are free to return any winner.
- If no votes have been cast, return `None`.

#### USAGE

```python
# Two votes for Kang, only one for Kodos. Kang wins.
>>> election_winner(('Kang', 'Kodos', 'Kang'))
'Kang'
```
