#repetition in regex and greedy/non-greedy matching
import re

bat_regex = re.compile(r'Bat(wo)?man') #batman or #batwoman 'wo' can appear 0 or 1 times

mo = bat_regex.search('The adventures of Batman')
print(mo.group())
mo = bat_regex.search('The adventures of Batwoman')
print(mo.group())
mo = bat_regex.search('The adventures of Batwowowoman') #nope
print(mo)

phone_regex = re.compile(r'\d\d\d\-\d\d\d-\d\d\d\d')

mo = phone_regex.search('My number is 111-222-3333')
print(mo.group())

mo = phone_regex.search('My number is 222-3333') #nope
print(mo)

phone_regex = re.compile(r'(\d\d\d\-)?\d\d\d-\d\d\d\d')
mo = phone_regex.search('My number is 111-222-3333')
print(mo.group())

mo = phone_regex.search('My number is 222-3333') 

# to literally match a question mark, since question marks are used to
# indicate optional character in the regex, just escape the question mark
# with a backslash e.g. \?

# * character = 0 or more
bat_regex = re.compile(r'Bat(wo)*man') # * is for 0 or more
mo = bat_regex.search('Batman')
print(mo.group())
mo = bat_regex.search('Batwoman')
print(mo.group())
mo = bat_regex.search('Batwowowowoman')
print(mo.group())

# + character - 1 or more
bat_regex = re.compile(r'Bat(wo)+man')
mo = bat_regex.search('Batwoman')
print(mo.group())
mo = bat_regex.search('Batwowowowoman')
print(mo.group())

#escaping +, *, ? if you want to match those actual characters

regex = re.compile(r'\+\*\?')
mo = regex.search('hi +*?')
print(mo.group())


#match exactly for a number of iterations of the same text - use curly braces

ha_regex = re.compile(r'(Ha){3}')
mo = ha_regex.search('HaHaHa')
print(mo.group())

#match a range of iterations

ha_regex = re.compile(r'(Ha){0,5}')
mo = ha_regex.search('HaHaHa')
print(mo.group())
mo = ha_regex.search('Ha')
print(mo.group())
mo = ha_regex.search('HaHaHaHaHa')
print(mo.group())

# greater than a number of iterations

ha_regex = re.compile(r'(Ha){3,}')
mo = ha_regex.search('HaHaHaHaHaHaHaHa')
print(mo.group())

# match a string that has a certain number of digits (3-5)
#while it could have matched on the first three or first four characters
# it matches on the first five because it auto does a "greedy" match
digit_regex =  re.compile(r'(\d){3,5}')
mo = digit_regex.search('1234567890')
print(mo.group())

# non-greedy match for first 3 digits (adds a question mark)
digit_regex =  re.compile(r'(\d){3,5}?')
mo = digit_regex.search('1234567890')
print(mo.group())


