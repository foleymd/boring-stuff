# control the keyboard with pyautogui

import pyautogui

# clicking on text editor in upper left corner and typing text
pyautogui.click(100,100); pyautogui.typewrite('Hello World')

# add interval to go slower
pyautogui.click(100,100); pyautogui.typewrite('Hello World', interval=0.1)

# add special characters - this uses left key. more info in docs
pyautogui.click(100,100); pyautogui.typewrite(['a', 'b', 'left', 'left', 'X', 'Y'])

print(pyautogui.KEYBOARD_KEYS) #all available keys

# use press for single key
pyautogui.press('volumeup')

# hotkey combos
pyautogui.hotkey('command', 's')
