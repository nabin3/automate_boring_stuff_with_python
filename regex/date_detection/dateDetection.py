#! python3
# dateDetection.py can check if a given date is valid or not 

import re

dateRegex = re.compile(r'(\d{2})\/(\d{2})\/(\d{4})')

mo = dateRegex.search('My date of birth is not 29/02/2004')

day = int(mo.group(1), 10)
month = int(mo.group(2), 10)
year = int(mo.group(3), 10)

if day > 31 or (month < 1 or month > 12) or (year < 1000 or year > 2999):
    print('Ops! Invalid Date')
else:
    # Checking if the year is lip-year
    isLeapYear = False
    if year % 400 == 0:
        isLeapYear = True
    elif year % 100 == 0:
        isLeapYear = False
    elif year % 4 == 0:
        isLeapYear =True


    isValidDate = True

    # If day is 31 and month is one of 4 month - september, april, june, november
    months_with_thirty_days = [9, 4, 6, 11]
    if day == 31:
        if month in months_with_thirty_days:
            isValidDate = False

    # If day is 29 and month is February
    if month == 2 and day > 28:
        if not isLeapYear:
            isValidDate = False

    if isValidDate:
        print('Valid Date')
    else:
        print('Ops! Invalid Date')
