# list methods

spam = ['hello', 'hiya', 'hi', 'howdy', 'hello']
print(spam.index('hello')) #returns index of item but only the first one

'''list has a number of methods'''

# print(spam.index('beep')) #raises an excpetion because it doesn't exist

spam.append('adieu') #adding to end of list
print(spam)

spam.insert(3, 'salut') #inserting at listed index
print(spam)

# we don't do 'spam = spam.append('thing')'
# we can't use append on strings or ints because they don't have the append method

'''allows you to specify value rather than index, but only the first instance
will be removed if the value is repeated in the list. compare to del spam[1]'''
spam.remove('hi') 
print(spam)

spam.sort()
print(spam)

spam = [1, 6, 5.7, 2, 89, 4]
spam.sort()

print(spam)

spam.sort(reverse=True)

print(spam)

#can't sort a list that has both ints and strings, e.g. ['hello', 1, 'neat']

# uses ASCII sort, which means upper case characters come before lower case letters

spam = ['Alice', 'Bob', 'alice', 'bob']
spam.sort()
print(spam)

spam.sort(key=str.lower) # convert to lower case string method for true alpha sort
print(spam)
