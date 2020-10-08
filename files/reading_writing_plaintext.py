''' reading and writing plaintext files (other files are binary files;
    we're not doing those here. '''

import shelve

# opening and reading file; can use absolute path as well. defaults to opening in read
# mode only
hello_file = open('hello.txt') 
print('first read through: \n', hello_file.read())

# using the read method only allows us to read the file once, so if we want to use it
# multiple times, we need to save it to a variable

file_content = hello_file.read() 

hello_file.close() #closes file

# you can also use the readlines method

hello_file = open('hello.txt')
print('list of strings: \n', hello_file.readlines()) #returns list of strings
hello_file.close()

# opening file in write mode - overwrites and starts from scratch
# but each call to the write method will add to the file until you close it
# if this file doesn't already exist, python will create a new blank file

hello_file = open('hello.txt', 'w')
hello_file.write('I wrote the file!\n')
hello_file.write('I wrote the file again!\n')
hello_file.close()

# opening file in append mode allows you to add to the end of an existing file
# if this file doesn't already exist, python will create a new blank file

hello_file = open('hello.txt', 'a')
hello_file.write('I appended to the file!\n')
hello_file.close()

hello_file = open('hello.txt') 
print('read after append: \n', hello_file.read())

# shelve module - can store lists and dictionaries to binary shelve file
# make a shelf file object called mydata that acts like a dictionary
# on mac, creates a .db file

shelf_file = shelve.open('mydata') 
shelf_file['cats'] = ['Cat 1', 'Catty', 'Nallie', 'Harvest Coyote']
shelf_file.close()

shelf_file = shelve.open('mydata')
print(shelf_file['cats']) 
shelf_file.close()

#keys() and values() shelf methods.

shelf_file = shelve.open('mydata')
print('keys: \n', list(shelf_file.keys()))
print('values: \n', list(shelf_file.values()))
shelf_file.close()
