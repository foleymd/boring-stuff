#regex basics

import re #regex functions

#complicated code showing why we want regex
def is_phone_number(text):
    if len(text) != 12:
        return False
    for i in range (0,3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    if i in range(4,7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    if i in range(8,12):
        if not text[i].isdecimal():
            return false
    return True

print(is_phone_number('111-222-3333'))
print(is_phone_number('beep'))

message = 'call me at 111-222-3333 or 222-333-4444'
found_number = False

for i in range(len(message)):
    chunk = message[i:i+12]
    if is_phone_number(chunk):
        print('Phone number found.')
        found_number = True

if not found_number:
    print('No phone number found.')

# much smaller program!
phone_number_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phone_number_regex.search(message) #mo equals match object
print('number is: ' + mo.group())
print(phone_number_regex.findall(message)) 

