# screenshot and image recognition

import pyautogui

pyautogui.screenshot() # this returns a pillow object
pyautogui.screenshot('screenshot1.png') # saves png in cwd

# locates place on screen based on image provided
# provides location and size
pyautogui.locateOnScreen('screenshot.png')

# provides center location and size of location that matches image provided
# it only matches pixel-perfect screenshots, so it can't handle updated stuff
pyautogui.locateCenterOnScreen('screenshot.png')

# with image recognition and keyboard and mouse controls, you can do tons of
# fun things!
