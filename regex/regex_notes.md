* **https://pythex.org/** in this side we can see how a regex pattern matches a piece of text that we enter.

* to use regex pattern in python we have to first ``` import re ```

* **\d** match a single neumeral like 0 to 9. So 342-789-3456 can be matched with this ``` r'\d\d\d-\d\d\d-\d\d\d\d' ```. Now this can be written like this also ``` r'\d{3}-\d{3}-\d{4}' ```. This **r** before regex pattern string is mandatory to denote the pattern as a raw string

* passing a regex pattern to ```re.compile``` will produce a regex pattern object(or regex object).
```bash
>>> import re
>>> phoneNumberRegex = re.compile(r'\d{3}-\d{3}-\d{4}')
```

* A regex object's **search** method searches the string it is passed for any matches to the regex. The search() method will return **None** if the regex pattern is not found in the given string  and if found then it will returns a **Match** object, which have a **group** method that will return the actual matched text from the searched string. We should check if ```search``` method has returned a none before applying group method.

```bash
>>> mo = phoneNumberRegex.search('My phone number is 234-789-1234')
>>> print('Phone number found: ' + mo.group())
Phone number found: 234-789-1234
```

* If we want to retrieve a specific part of a matched string. Then we can use **grouping** created with **()**.
```bash
>>> phoneNumberRegex = re.compile(r'(\d{3})-(\d{3}-\d{4})')
>>> mo = phoneNumberRegex.search('My phone number is 234-789-1234')
>>> print('Given phone number area: ' + mo.group(1))
Given phone number area: 234
>>> print('Given phone number without area-code: ' + mo.group(2))
Given phone number without area-code: 789-1234
>>> print('Given phone number: ' + mo.group(0))
Given phone number: 234-789-1234
>>> print('Given phone number: ' + mo.group())
Given phone number: 234-789-1234
>>> 
```

* to recieve all the group at once we use ```groups``` method. We will get a tuple.
```bash
>>> mo.groups()
('234', '789-1234')
>>> 
```

* Now as we can get multiple values from ```groups``` method, we can assign each value with multiple_assignment_trick.
```bash
>>> areaCode, mainNumber = mo.groups()
>>> print(f'area-code:{areaCode} && main_number:{mainNumber}')
area-codei:234 && main_number:789-1234
>>>
```

* paranthesis have special meaning in regular expression, but when we need to match paranthesis itself then we will use **\\** like this ``` r'(\(\d{3}\))-(\d{3}-\d{4}) ```

* ``` . ^ $ * + { } [ ] \ | ( ) ``` thes have special meaning in regex. so if we want to match those also then we should use **\**

* The ** | ** ia called a **pipe**. We can use it where we want to match one of many expression. ``` re.compile(expression1|expression2)```, when both expression present in a input string then search method will return expression1 as the matching object.
```bash
>>> import re
>>> heroRegex = re.compile('Batman|Tina Fay')
>>> mo1 = heroRegex.search('Batman nad Tina Fay')
>>> mo1.group()
'Batman'
>>> mo2 = heroRegex.search('Tina Fay and Batman')
>>> mo2.group()
'Tina Fay'
```

* We can also use use the ```|``` to match one of several patterns as **part** of our regex. In following example we wanted to match different patterns as **part** of the whole regex.
```bash
>>> batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
>>> mo = batRegex.search('Batmobile lost a wheel') 
>>> mo.group()
'Batmobile'
>>> mo.group(1)
'mobile'
>>> mo.group(0)
'Batmobile'
>>> 
# Look group(0) and group() is same thing.
```

### Optional matching with '?' mark:
 If we optionally want to match a pattern, i.e the regex will find a match regardless of whether that optional pattern exist. The **?** character flags the group that preceeds it is an optional part of the pattern.   
```bash
>>> batRegex = re.compile(r'Bat(wo)?man') # Here (wo) is flagged as optional with '?' character. The regex will match text with zero or exactly one instance of wo in it.
>>> mo1 = batRegex.search('The Adventure of Batman')
>>> mo1.group()
'Batman'
>>> mo1.group(1)
>>> mo2 = batRegex.search('The Adventure of Batwoman')
>>> mo2.group()
'Batwoman'
>>> mo2.group(1)
'wo'


>>> phoneRegex = re.compile(r'(\d{3}-)?\d{3}-\d{3}')
# Here the regex will look for phone numbers that do or do not have an area code.
>>> mo1 = phoneRegex.search('My number is 455-555-4242')
>>> mo1.group()
'455-555-424'
>>> mo2 = phoneRegex.search('My number is 555-4242')
>>> mo2.group()
'555-424'
>>> 
```

### Matching Zero or More with the '*':
The star means "match 0 or more and more" - the group preceiding **\*** can be abscent or repeated multiple times. If you need to match an actual star character, prefix the star in the regular expression with a backslash, \*.
```bash
>>> batRegex = re.compile(r'Bat(wo)*man')
>>> mo1 = batRegex.search('The adventures of Batman')
>>> mo1.group()
'Batman'
>>> 
>>> mo2 = batRegex.search('The adventures of Batwoman')
>>> mo2.group()
'Batwoman'
>>> 
>>> mo3 = batRegex.search('The adventures of Batwowowowoman')
>>> mo3.group()
'Batwowowowoman'
```

### Matching one or more with '+':
A group followed by a **+** in regex, present at least once or multiple times to match in a given string.
```bash
>>> batRegex = re.compile(r'Bat(wo)+man')
>>> mo1 = batRegex.search('The adventures of Batwoman')
>>> mo1.group()
'Batwoman'

>>> mo2 = batRegex.search('The adventures of Batwowowowoman')
>>> mo2.group()
'Batwowowowoman'

>>> mo3 = batRegex.search('The adventure of Batman')
>>> mo3 == None
True
```
If you need to match an actual plus sign character, prefix the plus sign with a backslash to escape it: \+.

### Matching specific repetitions with '{}'
If we need to have specify exactly the number of repetitions of a group we need to follow the group with a number in {}. Also we can specify range with two number in braces {minimum, maximum}. If we don't mention any of two then th range will have bounded in only mentioned limit.
```bash
>>> haRegex = re.compile(r'(Ha){3}')
>>> mo1 = haRegex.search('HaHaHa')
>>> mo1.group()
'HaHaHa'

>>> mo2 = haRegex.search('Ha')
>>> mo2 == None
True
```
Python regular expressions are greedy by default, which means that in ambiguous situations they will match the longest string by default. The non-greedy(also called lazy) version, which matches the shortest string possible, has the closing brace followed by a question mark **?**   
```bash
>>> greedyHaRegex = re.compile(r'(Ha){3,5}')    # Don't in write {3, 5} like this in regex expression it will not work, write {3, 5}

>>> mo1 = greedyHaRegex.search('HaHaHaHaHa')
>>> mo1.group()
'HaHaHaHaHa'    # Here we got the string with 5 'Ha' but we mwntioned 3 to 5 Ha in regex pattern, because regex expression is greedy by default.

>>> non_greedyHaRegex = re.compile(r'(Ha){3,5}?')
>>> mo2 = non_greedyHaRegex.search('HaHaHaHaHa')
>>> mo2.group()
'HaHaHa'    # Here we got 3 'Ha's, though there is also 5 'Ha's present because we use non-greedy regex here.
```
Note that the question mark can have two meanings in regular expressions: declaring a non-greedy match or flagging an optional group. These meanings are entirely unrelated.

### findall() method:
while **search** method returns a **Match** object of the first matched text in the search string, the **findall** method will return the string of every match in the searched string. When there is no group in regex object, then the findall will return a list of strings(those matches with the regex). but in case present of group in regex findall method will return list of tuples of strings(matches group of regex).
```bash
>>> phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{4}')    # has no groups
>>> phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
['415-555-9999', '212-555-0000']

>>> phoneNumRegex = re.compile(r'(\d{3})-(\d{3})-(\d{4})')  # has groups
>>> phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
[('415', '555', '9999'), ('212', '555', '0000')]
```

# Character class
with them we can write shorter regex. 
Shorthand character class    Represents
\d                           Any numeric digit from 0 to 9.
\D                           Any character that is not a numeric digit from 0 to 9.
\w                           Any letter, numeric digit, or the underscore character. (Think of this as matching “word” characters.)
\W                           Any character that is not a letter, numeric digit, or the underscore character.
\s                           Any space, tab, or newline character. (Think of this as matching “space” characters.)
\S                           Any character that is not a space, tab, or newline.

[0-9], [a-zA-z] these are also considered as character class. So, with **[]** we can make our own customized character classes.

* inside [] the normal regular expression symbols are not interpreted as such. So you don't need to escape them with '\' inside [].

* By placing a caret sign **^** just after the character class's opening bracket, you can make negative character class. A negative cahracter class will match all the characters that are not in the character class.
```bash
>>> consonantRegex = re.compile(r'[^aeiouAEIOU]')
>>> consonantRegex.findall('Robocop eats baby food. BABY FOOD.')
['R', 'b', 'c', 'p', ' ', 't', 's', ' ', 'b', 'b', 'y', ' ', 'f', 'd', '.', ' ', 'B', 'B', 'Y', ' ', 'F', 'D', '.']
```

### The Caret(^) and Dollar($) sign:
You can also use the caret symbol (^) at the start of a regex to indicate that a match must occur at the beginning of the searched text. 
Likewise, you can put a dollar sign ($) at the end of the regex to indicate the string must end with this regex pattern. 
And you can use the ^ and $ together to indicate
that the entire string must match the regex—that is, it’s not enough for a match to be made on some subset of the string.
```bash
>>> beginsWithHello = re.compile(r'^Hello')
>>> beginsWithHello.search('Hello, world!')
<re.Match object; span=(0, 5), match='Hello'>
>>> mo = beginsWithHello.search('Hello, world!')
>>> mo.group()
'Hello'

>>> beginsWithHello.search('He said hello') == None
True

>>> endsWithNumber = re.compile(r'\d$')
>>> endsWithNumber.search('Your number is 42')
<re.Match object; span=(16, 17), match='2'>
>>> endsWithNumber.search('Your number is forty two') == None
True

>>> wholeStringIsNum = re.compile(r'^\d+$')
>>> wholeStringIsNum.search('1234567890')
<re.Match object; span=(0, 10), match='1234567890'>
>>> 
>>> wholeStringIsNum.search('12345xyz67890') == None
True
>>> wholeStringIsNum.search('12 34567890') == None
True
# These last two search() calls in the previous interactive shell example demonstrate how the entire string must match the regex if ^ and $ both are used.
```

### the wildcard character '.':
The **.** character in regular expression is called a wildcard character and will match any character except for a newline.
```bash
>>> atRegex = re.compile(r'.at')
>>> atRegex.findall('The cat in the hat sat on the flat mat.')
['cat', 'hat', 'sat', 'lat', 'mat']
```
remember that the dot character will match only one character, which is why the match for the text ```flat``` in the above example matched only ```lat```. To match an actual dot, escape the dot with a backslash '\'

### matching everything with '.*':
Sometimes we will want to match everything and anything. For example,
say you want to match the string 'First Name:', followed by any and all text,
followed by 'Last Name:', and then followed by anything again. You can
use the dot-star (.*) to stand in for that “anything.” Remember that the
dot character means “any single character except the newline,” and the
star character means “zero or more of the preceding character.”
```bash
>>> nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
>>> mo = nameRegex.search('First Name: Nabin Chandra Last Name: Maiti')
>>> mo.group()
'First Name: Nabin Chandra Last Name: Maiti'
>>> mo.group(1)
'Nabin Chandra'
>>> mo.group(2)
'Maiti'
```
* the **dot-star** uses greedy mode. It will always try to match as much text as possible. To match in non-greedy manner we will use **?** after ```.*``` like this ```.*?```
```bash
>>> nongreedyRegex = re.compile(r'<.*?>')
>>> mo = nongreedyRegex.search('<To serve man> for dinner.>')
>>> mo.group()
'<To serve man>'
>>> 
>>> greedyRegex = re.compile(r'<.*>')
>>> mo = greedyRegex.search('<To serve man> for dinner.>')
>>> mo.group()
'<To serve man> for dinner.>'
>>> 
```

* In case of need to match newline also by passing ```re.DOTALL``` to compile method like this
```bash
>>> noNewlineRegex = re.compile('.*')
>>> noNewlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group()
'Serve the public trust.'
>>>
>>> newlineRegex = re.compile(r'.*', re.DOTALL)
>>> mo = newlineRegex.search('Serve the public trust.\nProtect the innocent.\n Upload the law')
>>> mo.group()
'Serve the public trust.\nProtect the innocent.\n Upload the law'
>>> 
```

### Case-Insensetive matching:
Normally regular expression match text with exact casing we have specified. but sometimes we need to match text insensetively. To do that we need to pass ```re.IGNORCASE or re.I``` to re.compile(). 
```bash
>>> robocop = re.compile(r'robocop', re.IGNORECASE)
>>> robocop.search('RoboCop is part man, part machine, all cop.')
<re.Match object; span=(0, 7), match='RoboCop'>
>>> robocop.search('RoboCop is part man, part machine, all cop.').group()
'RoboCop'
```

### Substituting with sub() method:
Regular expressions can not only find text patterns but can also substitute
new text in place of those patterns. The sub() method for Regex objects
is passed two arguments. The first argument is a string to replace any
matches. The second is the string for in which we want to apply substitution. The sub() method returns a string with the substitutions applied.
```bash
>>> nameRegex = re.compile(r'Agent \w+')
>>> nameRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.')
'CENSORED gave the secret documents to CENSORED.'
>>> 
```
Sometimes you may need to use the matched text itself as part of the
substitution. In the first argument to sub(), you can type \1, \2, \3, and so
on, to mean “Enter the text of group 1, 2, 3, and so on, in the substitution.
    For example, say you want to censor the names of the secret agents by
showing just the first letters of their names. To do this, you could use the
regex Agent (\w)\w* and pass r'\1****' as the first argument to sub(). The \1
in that string will be replaced by whatever text was matched by group 1—
that is, the (\w) group of the regular expression.
```bash
>>> agentNamesRegex = re.compile(r'Agent (\w)\w*')
>>> agentNamesRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve Knew Agen
t Bob was a double agent')
'A**** told C**** that E**** Knew B**** was a double agent'
>>> 
```

### Managing Complex Regexes:
for sake of readaibility we use multiline raw string with ```r'''....'''``` and inside this string we comment out each part(each located on different line) with **#**
```bash
phoneRegex = re.compile(r'''(
(\d{3}|\(\d{3}\))?  # area code
(\s|-|\.)?          # separator
\d{3}               # first 3 digits
(\s|-|\.)           # separator
\d{4}               # last 4 digits
(\s*(ext|x|ext.)\s*\d{2,5})?    # extension
)''', re.VERBOSE)

### Combining re.IGNORECASE, re.DOTALL, and re.VERBOSE:
```re.compile()``` takes only two argument, one of them is regex pattern. So when you need three of conditions together you need **|**, bitwise or operator. 
```bash
>>> someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)
```
