# similarities between lists and strings
print(list('Hello'))

name = 'Sophie'
print(name)
print(name[0])
print(name[1:3])
print(name[-1])
print('So' in name)
print('So' not in name)

for letter in name:
    print(letter)

#strings are immutable, but lists are mutable

# you cannot reassign letters in a string, instead create new strings using slices

name = "Sophie the Cat"
new_name = name[:7] + 'a' + name[10:]
print(new_name)

#references

# when you do the following to strings, the variables print out as you may expect
spam = 42
cheese = spam
spam = 100

print(cheese, spam)

# lists are differenet. when you assign a list, you're really assigning a list reference

spam = [1, 2, 3, 4, 5]
cheese = spam
cheese[1] = 'hello' #changes list item in both cheese and spam
print(cheese)
print(spam)

# the variable just holds a reference to where the data is sotred in memory
# when you assign the list to cheese and spam, it just assigns the same
# reference ID to this

def eggs(cheese):
    cheese.append('Hello')

spam = [1,2,3]
eggs(spam)
print(spam) #changes in spam continue outside the function because it's immutable/referenced

import copy #create a real copy rather than a reference to same list with deepcopy

spam = [1, 2, 3, 4, 5]
cheese = copy.deepcopy(spam)
cheese[1] = 98

print(spam)
print(cheese) #these should really list separate things

#line continuation exception - list can span multiple lines

spam = [1,
        2,
        3,
        4,
        5]

# or you can use the slash to do line continuation

print('Four score and seven ' + \
      'years ago.')
      


