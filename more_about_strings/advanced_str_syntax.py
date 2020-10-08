#escape characters

#quotation
print('I can\'t go to the store.')
print("That is Alice's cat.")
print('That isn\'t Alice\'s "cat."')
print("Hello, \"cat\".")
print('''Hello, you aren't a "cat."''')

#tab
print('Hello, \t cat.')

#newline
print('Hello, \n cat.')
print('Hello there!\nHow are you?\nI\'m fine!')

#backslash
print('Hello, \\ cat.')

#raw string (doesn't do escape characters)

print(r'Hello there!\nHow are you?\nI\'m fine!')

#triple quotes for multiline strings

print('''Dear Alice,
Eve's cat has been arrested for catnapping, cat burglary, and extortion.
Sincerely,
Bob''')
print("""Dear Alice,
Eve's cat has been arrested for catnapping, cat burglary, and extortion.
Sincerely,
Bob""")

spam = """Dear Alice,
Eve's cat has been arrested for catnapping, cat burglary, and extortion.
Sincerely,
Bob"""

print(spam) #it keeps the new lines when it stores the variables

#strings uses indexes and slices and in/not in

hello = 'hello world'
print(hello[2])
print(hello[1:3])
print('world' in hello) #True
print('World' in hello) #False
