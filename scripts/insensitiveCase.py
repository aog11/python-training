# How would you write a regex that matches a sentence where the first word is either Alice, Bob, or Carol; 
# the second word is either eats, pets, or throws; the third word is apples, cats, or baseballs; 
# and the sentence ends with a period?

import re

sentenceRegex = re.compile(r'''
    (^(Alice|Bob|Carol)       #Starting name
    \s+                       #in case of extra spaces
    (eats|pets|throws)        #second word
    \s+                       #in case of extra spaces
    (apples|cats|baseballs)   #next word
    (\.$))                    #ends with a dot
''', re.VERBOSE | re.I)

result = sentenceRegex.findall('BOB EATS CATS.')

print(result)