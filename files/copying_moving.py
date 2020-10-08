# copying and moving files and folders

import shutil # sh utility

#coping a file from one location to the next
# print(shutil.copy('files_filenames.py', '/users/mdf594/desktop')) 

#copy and rename
# print(shutil.copy('files_filenames.py', '/users/mdf594/desktop/second.py'))

#copy a directory
# print(shutil.copytree('/users/mdf594/desktop/automate', '/users/mdf594/desktop/automate_backup'))

# move directory
# print(shutil.move('/users/mdf594/desktop/automate_backup', '/users/mdf594/desktop/automate'))

# rename
# print(shutil.move('/users/mdf594/desktop/automate/automate_backup', '/users/mdf594/desktop/automate/automate_v2'))

