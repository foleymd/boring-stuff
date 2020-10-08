import pprint #pretty print

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {} #'r': 12 - key is r, value is 12

for character in message.upper(): #going through an upper case version of this string
    count.setdefault(character, 0)
    count[character] += 1

pprint.pprint(count) #prints prettily!
print('---------')
pp_variable = pprint.pformat(count) #can assign pretty f ormat to variables instead of just printing
print(pp_variable)
