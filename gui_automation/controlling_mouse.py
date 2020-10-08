''' controlling the mouse from python
pyautogui docs https://pyautogui.readthedocs.io/en/latest/

you'll need to update System Preferences to let IDLE control your mouse

MS paint example needed button left added to work

Note that this is blindly following instructions, so they can be dangerous.

pyautogui has a failsafe so that if the mouse is in the top left corner,
pyautogui will stop running. so if you need everything to slop, slam it to 0,0
in the top left corner
'''

import pyautogui

# get size of display
print(pyautogui.size())

#assign width and height of display to variables
width, height = pyautogui.size()

print(width)
print(height)

# prints current location of mouse pointer
print(pyautogui.position())

# moves pointer instantly
pyautogui.moveTo(10,10)

# moves pointer slower with duration = number of seconds
pyautogui.moveTo(100,500, duration = 1)

# moves pointer relatively with offsets
pyautogui.moveRel(200,300, duration = 1)

# moves pointer relatively with negative offsets to move up and left
pyautogui.moveRel(-100,-100, duration = 1)

# moving to an exact location in order to click something - choosing IDLE help
print(pyautogui.position())

# move to position and click
pyautogui.click(451,10)

# all these are valid
pyautogui.doubleClick(451,10)
pyautogui.rightClick(451,10)
pyautogui.click()

''' this example is for MS paint, which we don't have, but it draws a spiral '''
pyautogui.click()
distance = 200
while distance > 0:
    print(distance,0)
    pyautogui.dragRel(distance, 0, duration=0.1, button='left') # move right
    distance = distance - 25
    print(0, distance)
    pyautogui.dragRel(0, distance, duration=0.1, button='left') #move down
    print(-distance, 0)
    pyautogui.dragRel(-distance, 0, duration=0.1, button='left') #move left
    print(0, -distance)
    pyautogui.dragRel(0, -distance, duration=0.1, button='left') #move up

''' if you run python in a terminal window, import pyautogui, and run
pyautogui.displayMousePosition(), it will display the position and the rgb values
'''
