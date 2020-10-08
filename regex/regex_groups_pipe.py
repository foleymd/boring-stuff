#regex groups and the pipe character
import re

phone_number_regex = re.compile(r'\d\d\d-\d\d\d\-\d\d\d\d')

#searching for phone number match instring
mo = phone_number_regex.search('My number is 555-555-1212')
print(mo.group())

#parentheses group parts of the regex - they are not looking for literal parentheses
phone_number_regex = re.compile(r'(\d\d\d)-(\d\d\d\-\d\d\d\d)')
mo = phone_number_regex.search('My number is 555-555-1212')
print(mo.group())
print(mo.group(1))
print(mo.group(2))

# if you wanted to find literal parentheses, escape the parentheses with a backslash
phone_number_regex = re.compile(r'\(\d\d\d\)-\(\d\d\d\-\d\d\d\d\)')
mo = phone_number_regex.search('My number is (555)-(555-1212)')
print(mo.group())

#find all words that start with Bat and match a list of options separated by a pipe

bat_regex = re.compile('Bat(man|mobile|copter)')
mo = bat_regex.search('Batcopter')
print(mo)
print(mo.group())
print(mo.group(1)) # if we just want to know the suffix

# no match example
mo = bat_regex.search('Batwoman')
print(mo) #none doesn't have .group
