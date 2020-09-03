# Booleans and Conditionals

## Boolean values
Boolean values are True and False (note the capitalization). They have a type 'bool' and are like "yes" or "no" in response to a condition.

## Comparison operators

Comparison operators check the relationship between two values. For example, ``` x == 5 ``` asks if x is equal to 5. If the statement (comparison) is true, the operator will return True. If the statement is not true, it will return a value of False.

**Note the difference between = and ==. A single = assigns the value on the right to the variable on the left (```x = 5```). A double == checks to see if the two sides are equal.**

|Operator|Check to see if...|
|:---:|:---:|
|x == y| x is equal to y |
|x != y| x is not equal to y |
| x > y | x is greater than y |
| x < y | x is less than y |
| x >= y | x is greater than or equal to y |
| x <= y | x is less than or equal to y |

## Logical operators

Logical operators are ```and```, ```or``` and ```not```. They are used with comparison operators to check the relationship between conditions.

For example, ```x > 5 and x < 10``` returns True if x is both greater than 5 and less than 10. If x is 10, False will be returned because one of the conditions is not met.

Truth tables are commonly used to keep track of the outputs of logical operators.

Truth table for ```and```:


| a | b | a and b |
| :---: | :---: | :---: |
| True | True | True |
| False | True | False |
| True | False | False |
| False | False | False |


Truth table for ```or```:

| a | b | a or b |
| :---: | :---: | :---: |
| True | True | True |
| False | True | True |
| True | False | True |
| False | False | False |

Truth table for ```not```:
(Note that ```not``` only requires one operand.)

|a| not a |
|:---:|:---|
|True|False|
|False|True|

## Conditionals

Conditional statements check to see if a certain condition is met and then executes blocks of code according to the answer.

For example, the code below checks to see if x is greater than 2. If ```x > 2``` is True, the block to print Hello will run. Otherwise, Goodbye will be printed.

```python
if x > 2:
  print("Hello")
else:
  print("Goodbye")
```
You cam have check multiple conditions at once:

```python
if x > 2:
  print("Hello")
elif x == 2:
  print("Hola")
else:
  print("Goodbye")
```

Note the indentations for each block. The indented blocks go with the statements above them and only run if those statements are True. **Be careful with indentations - incorrect indentations can cause unexpected behavior!**
