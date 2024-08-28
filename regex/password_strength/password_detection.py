#! python3
# password_detection.py detect if a given password is strong enough

import re, sys

if len(sys.argv) != 2: 
    print('Ivalid usage of script\nusage:// python password_detection.py your_password')
    sys.exit(0)
password = sys.argv[1]

lRegex = re.compile(r'[a-z]+')
uRegex = re.compile(r'[A-Z]+')
dRegex = re.compile(r'\d+')
mo1 = lRegex.search(password)
mo2 = uRegex.search(password)
mo3 = dRegex.search(password)

if mo1 == None or mo2 == None or mo3 == None:
    print('This is an weak password')
else:
    print('This is a strong password')
