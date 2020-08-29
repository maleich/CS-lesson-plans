# Python Day 1
## Type these into the command line for students to follow
```python
>>> print("Hello world!")
Hello world!
>>> print('Hello world!')
Hello world!
```
* Hello world is called a string and needs quotes - single or double.
* print() is a pre-defined Python function that dispays arguments on the screen.
* Whitespace doesn't matter except indentations. Single spaces btwn operators is convention.

```
>>> 2 + 2
4
```
Comments let you leave notes, too!
```
>>> 2 + 2    # This is an expression. 2 is a value, + is an operator.
4           # The expression evaluates to 4
```
Python operators (in order of precedence):

| Operator | Operation | Example | Evaluates to: |
|  :---:   |  :---:    |  :---:  |     :---:     |
|   **     |  Exponent |  2 ** 3 |       8       |
| % | Modulus/remainder | 22 % 8  | 6 |
|// | Integer division | 22 // 8 | 2 |
| / | Division | 22 /8 | 2.75
| * | Multiplication | 3 * 5 | 15|
| - | Subtraction | 5 - 2 | 3 |
| + | Addition | 5 + 2 | 7 | 

Parentheses are your friends! Be careful of order of operations.

```
>>> 2 + 3 * 6 # What do you think this evaluates to?
20

```
Safer to use parentheses to be sure you get what you what - and make it easier to read.

```
>>> 2 + (3 * 6)
20

>>> (2 + 3) * 6
30
```
 Play with the Console for a bit. Notice any errors you get - or other unexpected behavior.
 
 ### Data types
 Data can have four main data types:
 * int - integers
 * float - floating point numbers (decimals)
 * str - strings (text), surround with quotes
 * bool - boolean (True, False)

To check the type, use function type()
```python
>>> type(3)
<class 'int'>
``` 

To convert between types, use type functions:
* int()
* float()
* str()
* bool()
(Note that this only works when the conversion makes sense.)

```
int('Hello')    # This will give an error!
```