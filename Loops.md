 
# For Loop in Python
Adapted from [W3Schools Python Tutorial](https://www.w3schools.com/python/python_for_loops.asp)
 
The `for` loop lets us run a set of commands a preset number of times (such as the number of characters in a string or list). It does not require an 
indexing variable to be set beforehand. It can be used to iterate over a sequence (such as a string or list) or we can specify the number of times with the `range()` function.

The `for` loop does not require an indexing variable to set beforehand.

### Looping Through a String
Strings are iterable objects, they contain a sequence of characters:

Example: Loop through the letters in the word "banana":
```python
for x in "banana":
  print(x)
  
# Output:
b
a
n
a
n
a
```

### The `break` Statement
With the `break` statement we can stop the loop before it has looped through all the items:
Example:
```python
for x in "banana":
  print(x)
  if x == "n":
    break
  
# Output:
b
a
n
```

### The `range()` Function
To loop through a set of code a specified number of times, we can use the `range()`
 function, which returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.

Example: Using the `range()` function:
```python
for x in range(6):
  print(x)
  
# Output:
0
1
2
3
4
5
```

Note that range(6) is not the values of 0 to 6, but the values 0 to 5. The
range() function starts at 0 by default. You can also specify where you want to start by adding a parameter.
For example `range(2, 6)` means values from 2 up to (but not including) 6.

Example
```python
# Using the start parameter:
for x in range(2,6):
  print(x)
  
# Output:
2
3
4
5
```

Unless otherwise specified, the `range()` function goes up by 1 each time. If you want to change that, you can add another parameter:
`range(2, 30, 3)` In this case, the "step size" is 3.

Example: Increment the sequence with 3 (default is 1)
```python
for x in range(2,30,3):
  print(x)

# Output:
2
5
8
11
14
17
20
23
26
29
```
You can also count backward by using a negative number for the step size:
```python
for x in range(10, 0, -1):
  print(x)

# Output:
10
9
8
7
6
5
4
3
2
1
```