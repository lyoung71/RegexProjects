#! python3

# uses regexes to convert American dates to European dates for all files with dates in their filenames.
# uses shutil module to manipulate and move files with python

import shutil, re, os


american_date_regex = re.compile(
    r'''^(.*?)          #all text before the date
    ((0|1)?\d)          #one or two digits for the month
    -
    ((0|1|2|3)?\d)      #one or two digits for the day
    -
    ((19|20)\d\d)       #four digits for the year
    (.*?)$              #all text after the date
    ''', re.VERBOSE)


for amerFilename in os.listdir('.'):
    mo = american_date_regex.search(amerFilename)
    if mo is None:
        continue
    before_part = mo.group(1)
    month_part = mo.group(2)
    day_part = mo.group(4)
    year_part = mo.group(6)
    after_part = mo.group(8)

    euroFilename = f'{before_part}{day_part}-{month_part}-{year_part}{after_part}'

    absWorkingDir = os.path.abspath('.')
    amerFilename = os.path.join(absWorkingDir, amerFilename)
    euroFilename = os.path.join(absWorkingDir, euroFilename)

    print(f'Renaming "{amerFilename}" to "{euroFilename}"...')
    shutil.move(amerFilename, euroFilename)
