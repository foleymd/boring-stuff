# deleting files

import os, shutil, send2trash

# these first examples are dangerous because they are permanent deletions

# delete file
# print(os.unlink('hello.txt')) #unlink is an old name for delete

# delete directory
# print(os.rmdir('../automate')) #direcotry must be empty to remove

# deleting directory and contents at the same time requires shutil
# there do be dragons here!
# print(shutil.rmtree('../automate'))

# you can use the send2trash module to drop it in the recycle bin instead
# send2trash.send2trash.('/users/mdf594/desktop/filename.txt')

