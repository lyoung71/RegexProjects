import re


def strongPasswordDetector():
    password = input("Please enter your password ")

    lengthRegex = re.compile(r'\w{8,}')
    lowercaseRegex = re.compile(r'[a-z]+')
    uppercaseRegex = re.compile(r'[A-Z]+')
    digitRegex = re.compile(r'\d+')

    lengthMatch = lengthRegex.search(password)
    lowercaseMatch = lowercaseRegex.search(password)
    uppercaseMatch = uppercaseRegex.search(password)
    digitMatch = digitRegex.search(password)

    if lengthMatch is None:
        return "Please make sure password has at least 8 characters"
    elif lowercaseMatch is None:
        return "Please make sure password includes at least 1 lowercase character"
    elif uppercaseMatch is None:
        return "Please make sure password includes at least 1 uppercase character"
    elif digitMatch is None:
        return "Please make sure password includes at least 1 number"
    else:
        return "You have a strong password!"

print(strongPasswordDetector())
