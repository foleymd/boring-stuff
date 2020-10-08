# filenames and absolute/relative filenames

import os #contains file path functions

file_path = 'c:\\spam\\eggs.png' #two backslashes in order not to be using escape characters
print(file_path)

file_path = r'c:\spam\eggs.png' # or use raw string
print(file_path)

file_path = 'c:\\' + '\\'.join(['folder1', 'folder2', 'folder3']) #only works on widows
print(file_path)

file_path = os.path.join('folder1', 'folder2', 'folder3') #returns path appropriate to OS
print(file_path)

print('\\') #single backslash
print(os.sep) #separator on the OS

print(os.getcwd()) #current working directory
# os.chdir('../..') #up two
# print(os.getcwd())


# spam.png = relative file patch
# absolute path = C:\spam\eggs.png
# . equals this directory
# .. equals parent directory
# etc.

#os path functions

print(os.path.abspath('files_filenames.py')) #print absolute path of file

print(os.path.isabs('files_filenames.py')) #is something an absolute path: False

print(os.path.isabs('/Users/mdf594/Desktop/automate/files_filenames.py')) #is something an absolute path: True

print(os.path.relpath('/Users/mdf594/Desktop/automate/files_filenames.py', '/Users/mdf594/')) #relative path between two items

print(os.path.relpath('/Users/mdf594/', '/Users/mdf594/Desktop/automate/files_filenames.py')) # as above but reversed

print(os.path.dirname('/Users/mdf594/Desktop/automate/files_filenames.py')) # directories

print(os.path.basename('/Users/mdf594/Desktop/automate/files_filenames.py')) # file name only 

print(os.path.exists('/Users/mdf594/Desktop/automate/files_filenames.py')) # does the file exist

print(os.path.isfile('/Users/mdf594/Desktop/automate/files_filenames.py')) # is it a file

print(os.path.isdir('/Users/mdf594/Desktop/automate/files_filenames.py')) # is it a directory/folder

print(os.path.getsize('/Users/mdf594/Desktop/automate/files_filenames.py')) #size of file/dir

print(os.listdir('/Users/mdf594/Desktop/')) # list items in directory

# getting total size of all non-directory files in a directory:
total_size = 0

for filename in os.listdir('/Users/mdf594/Desktop/'):
    if not os.path.isfile(os.path.join('/Users/mdf594/Desktop/', filename)):
            continue
    total_size += os.path.getsize(os.path.join('/Users/mdf594/Desktop/', filename))

print(total_size)

# making directories:

# os.makedirs('test') #creates a test folder in the current directory; can also take an absolute path


