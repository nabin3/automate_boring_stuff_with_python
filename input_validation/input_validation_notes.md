# PyInputPlus module:
PyInputPlus is not a part of the Python Standard Library, so you must install it separately using Pip. To install PyInputPlus, run ```pip install pyinputplus``` 
from the command line.

Various functions from **PyInputPlus** module:
* inputStr(): Is like the built-in input() function but has the general PyInputPlus features. We can also pass a custom validation function to it.
* inputNum(): Ensures the user enters a number, and return an int or float, depending on if the number has a decimal point in it.
* inputChoice(): Ensures user enter one of the provided choices.
* inputMenu(): Same as inputChoice, but provide a menu with numbered ao lettered options.
* inputDatetime(): Ensures the user enters a date and time.
* inputYesNo(): Ensures the user enters a 'yes' or 'no' response.
* inputBool(): Is similar to inputYesNo(), but takes a “True” or “False” response and returns a Boolean value.
* inputEmail(): Ensures the user enters a valid email address.
* inputFilepath(): Ensures the user enters a valid fi le path and fi lename, and can optionally check that a fi le with that name exists
* inputPassword(): Is like the built-in input(), but displays * characters as the user types so that passwords, or other sensitive information, aren’t displayed on the screen

Note: These functions will automatically reprompt the user for as long as they enter invalid input. And prompt can be used with ```promt``` keyword argumeny.
```bash
import pyinputplus as pyip
>>> response = pyip.inputInt(prompt='Enter a number: ') 
Enter a number: cat 
'cat' is not an integer.
Enter a number: 42 
>>> response 
42
```

## using help() function:
help(pyip.inputChoice) displays help information for the inputChoice() function. Can get help about any function by the same way.

## Additional options:
pyinputplus have sevaral additional features for input validation.

### min, max, greaterThan and lessThan keyword arguments:
inputNum(), inputInt, inputFloat() have these.
```bash
>>> import pyinputplus as pyip
>>> response = pyip.inputNum('Enter num: ', min=4)
Enter num: 3
Number must be at minimum 4.
Enter num: 4
>>> response
4
>>> response = pyip.inputInt('Enter integer: ', max=7)
Enter integer: 9
Number must be at maximum 7.
4.5
'4.5' is not an integer.
Enter integer: 5
>>> response
5
>>> response = pyip.inputNum('Enetr num: ', greaterThan=4)
Enetr num: 4
Number must be greater than 4.
Enetr num: 7
>>> response
7
>>> response = pyip.inputNum('Enter Num: ', lessThan=5)
Enter Num: 6
Number must be less than 5.
Enter Num: 5
Number must be less than 5.
Enter Num: 2
>>> response
2
```

### blank keyword argument:
By default, blank input isn't allowed unless the blank keyword argument is set to be true.
```bash
>>> import pyinputplus as pyip 
>>> response = pyip.inputNum('Enter num: ') 
Enter num:(blank input entered here) 
Blank values are not allowed.
Enter num: 42 
>>> response 
42 
>>> response = pyip.inputNum(blank=True) 
(blank input entered here) 
>>> response 
''
```
Use blank=True if you’d like to make input optional so that the user doesn’t need to enter anything

### limit, timeout and default keyword arguments:
By default, the pyinputplus functions will continue to ask the user for valid input forever. With limit and timeout keyword argument we can specify how many times or how much second a function will ask for valid input and if user don't pass one valid input in those constraints then ```RetryLimitException``` or ```TimeoutException``` will be thrown. But if we use ```default``` keyword argument with those then a default value should be return by the functions instead of throwing exception.
```bash
>>> import pyinputplus as pyip 
>>> response = pyip.inputNum(limit=2) 
blah 
'blah' is not a number.
number 
'number' is not a number.
Traceback (most recent call last):
 --snip--
pyinputplus.RetryLimitException 
>>> response = pyip.inputNum(timeout=10) 
42 (entered after 10 seconds of waiting)
Traceback (most recent call last):
 --snip--
pyinputplus.TimeoutException

>>> response = pyip.inputNum(limit=2, default='N/A')
ha
'ha' is not a number.
up
'up' is not a number.
>>> response
'N/A'
>>>
```

### allowRegex() and blockRegex() keyword arguments:
```allowRegexes``` and ```blockRegexes``` keyword arguments take a list of regex string to determine what the pyinputplus functions will accept or reject as valid input.
```bash
>>> import pyinputplus as pyip 
>>> response = pyip.inputNum(allowRegexes=[r'(I|V|X|L|C|D|M)+', r'zero']) 
XLII 
>>> response 
'XLII' 
>>> response = pyip.inputNum(blockRegexes=[r'[02468]$'])
42
This response is invalid.
41
>>> response
41
```
If specified both allowRexes and blockRegexes argument, the allowRegexes will override blockRegexes list.
```bash
>>> import pyinputplus as pyip 
>>> response = pyip.inputStr(allowRegexes=[r'caterpillar', 'category'], blockRegexes=[r'cat']) 
cat 
This response is invalid.
catastrophe 
This response is invalid.
category 
>>> response
'category'

### Passing a custom validation function to inputCustom():
We can write a function to perform our own custom validation logic by passing the function to inputCustom()
```bash
import pyinputplus as pyip 

def addsUpToTen(numbers):
    numberList = list(numbers)
    for i, digit in enumerate(numberList):
        numberList[i] = int(digit)
    if sum(numberList) != 10:
        raise Exception(f'The digits must add up to 10, not {sum(numberList)}')
    return int(numbers)

response = pyip.inputCustom(addsUpToTen)
123
The digits must add upto 10, not 6
1234
```
The inputCustom() function also supports the general PyInputPlus fea-tures, such as the blank, limit, timeout, default, allowRegexes, and blockRegexes keyword arguments
