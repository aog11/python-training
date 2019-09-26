#Matching name of someone whose last name is Nakamoto

import re

nameRegex = re.compile(r'(^[A-Z]{1}\w+\s+Nakamoto$)')

match = nameRegex.findall('Satoshi Nakamoto')

print(str(match))