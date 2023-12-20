import re


def dateDetector():
    dateRegex = re.compile(
        r'''
            ([0][1-9]|[1-2][0-9]|[3][0-1])       # day
            /                                   #separator
            ([0][1-9]|[1][0-2])                 #month
            /                                   #separator
            ([1-2][0-9]{3})                       #year
        ''',
        re.VERBOSE)

    match = dateRegex.search(input("Please enter a date in DD/MM/YYYY format "))
    print(match)
    day = int(match.group(1))
    month = int(match.group(2))
    year = int(match.group(3))

    if year % 4 != 0 and month == 2 and day > 28:
        return "Not a valid date"
    elif year % 4 == 0 and month == 2 and day > 29:
        return "Not a valid date"
    elif (month == 4 and day > 30) or (month == 6 and day > 30) or (month == 9 and day > 30) or (month == 11 and day > 30):
        return "Not a valid date"
    else:
        return "Date is valid"

print(dateDetector())
