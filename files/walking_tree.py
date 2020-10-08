# walking a directory tree

# that is, writing code to apply to all files and folders in a directory

import os

print (os.walk('/users/mdf594/desktop/automate'))

for folder_name, subfolders, filenames in os.walk('/users/mdf594/desktop/test'):
    print('The folder is ' + folder_name)
    print('The subfolders in ' + folder_name + ' are : ' + str(subfolders))
    print('The files in ' + folder_name + ' are : ' + str(filenames))
    
    for subfolder in subfolders:
        print(subfolder)
        # delete, move, copy, rename, etc. 
