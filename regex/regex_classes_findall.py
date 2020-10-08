# regex character classes and the findall() method

import re

phone_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
phone_text = '123-456-7890 is a good number. 345-678-9012 works. So does 123-890-4567.'


#findall finds all matches rather than the first match
# this won't return mo (match object)
print(phone_regex.findall(phone_text))

# for findall, if the regex has 0 to one groups,it will only return a list of strings

# if it does have groups, it returns list of touples with groups in there
phone_regex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
phone_text = '123-456-7890 is a good number. 345-678-9012 works. So does 123-890-4567.'
print(phone_regex.findall(phone_text)) #returns list of tuples with each group from the regex separated

#character class examples
numeric_regex = re.compile(r'\d')
not_numeric_regex = re.compile(r'\D') # numeric
word_regex = re.compile(r'\w') # alpha, numeric, underscore
not_word_regex = re.compile(r'\W') # not alpha, numeric, underscore
space_regex = re.compile(r'\s') # space, tab, newline
not_space_regex = re.compile(r'\S') # space, tab, newline

# counting number + noun e.g 12 drummers, 11 lords, etc. 
lyrics = '12 days of christmas 12 drummers drumming 11 lords leaping 5 golden rings'
xmas_regex = re.compile(r'\d+\s\w+')
print(xmas_regex.findall(lyrics)) #outputs list of numbers and nouns from 

#you can make your own character classes:
# just vowels and a-f examples
vowels_obj = re.compile(r'[aeiou]') #same as r'(a|e|i|o|u)'
a_to_f_obj = re.compile(r'[a-f]') #same as r'(a|b|c|d|e|f)'
vowels_plus_caps_obj = re.compile(r'[aeiouAEIOU]') #same as r'(a|e|i|o|u|A|E|I|O|U)'
a_to_f_plus_caps_obj = re.compile(r'[a-fA-F]') #same as r'(a|b|c|d|e|f|A|B|C|D|E|F)'

print(vowels_obj.findall('grandma got run over by a reindeer'))

#multiple vowels in a row
vowels_mult_obj = re.compile(r'[aeiou]{2}')
print(vowels_mult_obj.findall('grandma got run over by a reindeer'))

# negative character classes using caret -  does the opposite of the listed letters
no_vowels_obj = re.compile(r'[^aeiouAEIOU]')
print(no_vowels_obj.findall('grandma got run over by a reindeer'))
