#sub() method and verbose mode

import re

#find and replace with sub()

names_regex = re.compile(r'Agent \w+')
mo = names_regex.findall('Agent Alex loves Agent Neil')
print(mo)

#first argument is the new text
mo = names_regex.sub('REDACTED','Agent Alex loves Agent Neil')
print(mo)

# what if you want to sub but with part of the regex pattern?

names_regex_a = re.compile(r'Agent (\w)\w*') #group for first letter of the name and the last is additional characters
mo = names_regex_a.sub(r'Agent \1','Agent Alex loves Agent Neil') # the \1 indicates group 1
print(mo)

# verbose mode

#not verbose
phone_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

#verbose - text doesn't need new lines or white space, allows comments
phone_regex = re.compile(r'''
                         \d\d\d|    #area code no parens
                         \(\d\d\d\) #area code parens
                         -
                         \d\d\d     #prefix
                         -
                         \d\d\d\d   #last four
                         ''', re.VERBOSE)

#you can use multiple re.IGNORECASE, re.DOTALL, re.VERBOSE with this syntax

phone_regex = re.compile(r'''
                         \d\d\d|    #area code no parens
                         \(\d\d\d\) #area code parens
                         -
                         \d\d\d     #prefix
                         -
                         \d\d\d\d   #last four
                         ''', re.VERBOSE | re.DOTALL | re.IGNORECASE)
