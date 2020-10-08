# . * ^ $ characters

# ^ match the start and $ match the end

import re

# caret for beginning
begins_with_hello_regex = re.compile(r'^hello')

mo = begins_with_hello_regex.search('hello') #match 
print(mo.group())

mo = begins_with_hello_regex.search('yo hello') #no match
print(mo)

# dollar for ending
ends_with_world_regex = re.compile(r'world$')

mo = ends_with_world_regex.search('yo world') #match
print(mo.group())

mo = ends_with_world_regex.search('yo world hello') # no match
print(mo)

# matching with pattern at start and at end with ^ and $
all_digits_regex = re.compile(r'^\d+$')

mo = all_digits_regex.search('12981298713987129387') #match
print(mo.group())

# with character in middle, doesn't match exactly
mo = all_digits_regex.search('129x1234') # no match
print(mo)

# wildcard  .  character

#single character wildcard
at_regex = re.compile(r'.at')

mo = at_regex.findall('cat hat mat flat') #doesn't return flat because it's only a single character before the 'at'
print(mo) # list object does not have a group

#multiple character wildcard
at_regex = re.compile(r'.{1,2}at') # one or two characters (this includes whitespace characters now)

mo = at_regex.findall('cat hat mat flat') #doesn't return flat because it's only a single character before the 'at'
print(mo) # list object does not have a group

# regex that gets a variable name of characters
name_regex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = name_regex.findall('First Name: Marjorie Last Name: Foley')
print(mo)

# .* uses greedy mode; .*? is non-greedy mode
serve = '<To serve humans> for dinner.>'

#nongreedy
nongreedy = re.compile(r'<(.*?)>')
mo = nongreedy.findall(serve)
print(mo)

#greedy
greedy = re.compile(r'<(.*)>')
mo = greedy.findall(serve)
print(mo)

# note that * is for any character for new line, so the example below will
# only print the first line
prime = 'Serve the public trust. \n Protect the innocent. \n Uphold the law.'
print(prime)

dot_star = re.compile(r'.*')
mo = dot_star.search(prime)
print(mo.group()) 

# how to get the dot to mean everything including new lines

dot_star = re.compile(r'.*', re.DOTALL) #second argument says it includes EVERYTHING
mo = dot_star.search(prime)
print(mo.group()) #prints all lines of the prime directive

# IGNORECASE will allow you to do just that
vowel_regex =re.compile(r'[aeiou]', re.IGNORECASE)
mo = vowel_regex.findall('aeio fdhse AIE dhd')
print(mo) 
