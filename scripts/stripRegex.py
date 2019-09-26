#Chapter 7
#Regex version of strip project

import re

def stripRegex(text, param=''):
    if param == '':
        stripRegex = re.compile(r'^\s+|\s+$')
        match = stripRegex.findall(text)
        if match:
            result = stripRegex.sub('',text)
    else:
        stripRegex = re.compile('' + param, re.I)
        result = stripRegex.sub('',text)

    print(result)

#Text to strip of spaces
text = '    This is a test.       '
#What to remove from the text instead
param = 't'

stripRegex(text)
stripRegex(text,param)