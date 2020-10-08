# string methods examples

import pyperclip

#upper and lower
spam = 'Hello World'
print(spam.upper()) #doesn't change spam
print(spam)

spam = spam.upper() #will change spam
print(spam)

print("Would you like to play a game?")
answer = input()

if answer == 'YES': #won't work if answer is yes
    print('Input equal to \'YES ' + answer)
    
if answer.isupper():
    print('Answer is upper') 

answer = answer.upper() #helps distinguish user input if they use a different case than expected

if answer == 'YES': #will  work if answer is yes
    print('Input translated to upper case ' + answer)

answer = answer.lower() #translating to lower case

print('Input translated to lower case ' + answer)

if answer.islower(): #needs at least one lower case character, doesn't work on blank
    print('Answer is lower')

if answer.isupper(): 
    print('Answer is upper')    

print('Hello'.upper().isupper()) #does a ton of stuff right in a row!

print('Other string methods')
print('Hello'.isalpha()) #alpha
print('H12345'.isalnum()) #alphanumerics
print('5'.isdecimal()) #number
print('    '.isspace()) #only space
print('Title Is This'.istitle()) #camelcase - all words must be camelcase

#you can also translate to camelcase

print('hello world'.title())

#starts with and ends with evaluations
print('hello world'.startswith('h'))
print('hello world'.startswith('w'))
print('hello world'.endswith('h'))
print('hello world'.endswith('w'))

#join
print(' '.join(['beep', 'boop'])) #join list of strings based on space separator
print(', '.join(['beep', 'boop']))# separator changed to comma space
print('\n'.join(['beep', 'boop']))# separator changed to newline

#split
print('My name is Marjorie'.split()) #split on space
print('My name is Marjorie'.split('M')) #split on 'M'

#.rjust and .ljust

print('Hello'.rjust(10)) #tell it the number of characters so that it will know where to move stuff
print('Hello'.ljust(10)) #tell it the number of characters so that it will know where to move stuff

# use different fill characters
print('Hello'.rjust(10, '*'))
print('Hello'.ljust(10, '*'))

#center
print('Hello'.center(10, '*'))

#strip
spam = '     word    ' 
print(spam.strip()) #stripping out white space, works on other characters if they are passed as arguments
print(spam) #remember that it is immmutable, though

spam = spam.strip()
print(spam)

#lstrip and rstrip
spam = '     word    '
print('lstrip ' + spam.lstrip())
print('rstrip ' + spam.rstrip())

print(spam)
print('-wo ' + spam.strip(' wo')) #stripping characters instead of white space

#replace method
spam = 'Spam'
print(spam.replace('Spam', 'Eggs'))

# using imported pyperclip library to copy and paste to clipboard
pyperclip.copy(spam)
print(pyperclip.paste())
