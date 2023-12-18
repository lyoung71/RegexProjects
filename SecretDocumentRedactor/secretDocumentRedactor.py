import re

def redactorTool(text):
    #regular expressions
    namesRegex = re.compile(r'Agent \w+')
    namesRegex2 = re.compile(r'Ms. \w+')
    dateRegex = re.compile(r'\d{2}\/\d{2}\/\d{4}')
    timeRegex = re.compile(r'\d{4}')
    dayRegex = re.compile(r'\w+day')

    #substitutions
    text = namesRegex.sub('CENSORED', text)
    text = namesRegex2.sub('CENSORED', text)
    text = dateRegex.sub('CENSORED', text)
    text = timeRegex.sub('CENSORED', text)
    text = dayRegex.sub('CENSORED', text)

    return text


message = """
    On 16/12/2023, Agent Young accompanied a young woman by the name of Ms. Juliana to a barbecue.
    Agent Young arrived at the barbecue at approximately 1300. Agent Young proceeded to eat and drink and have a good time.
    He left the barbecue at 2300 hours and arrived home at 0030 the following day.
    We haven't heard from him since.
    """

print(redactorTool(message))
