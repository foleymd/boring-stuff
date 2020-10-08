#! /usr/bin/env python3

# opens map in Google maps and run it without opening python or giving it the full url
# according to the instructions for OS X, this .py file should be saved to the home folder
# then, change the permissions to make the file executable: chmod +x mapit.py
# you can then run the program by typing ./mapit.py on the command line
# instructions also add the shebang line to the top
#
# works with address copied to clipboard or as an argument, e.g.:
# ./mapit.py 5501 N Lamar Blvd Suite C101, Austin, TX 78751
# to run from any directory, its parent directory needs to be added to PATH
 
import webbrowser, sys, pyperclip

sys.argv # e.g. ['mapit.py', '870', 'Valencia', 'St.']

if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste() #assume the user has copied something to the clipboard

# google maps base url plus our address
webbrowser.open('https://google.com/maps/place/' + address)

