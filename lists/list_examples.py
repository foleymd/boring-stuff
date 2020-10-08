# List examples

spam = [] # initializing

spam = ['cat', 'bat', 'rat', 'elephant'] #assigning variable
print(spam) #printing list

print(spam[0]) #printing items individually
print(spam[1])
print(spam[2])
print(spam[3])

spam = [['cat', 'bat'], [10, 20, 30, 40, 50]] #lists of lists
print(spam[0])
print(spam[0][1]) #item within item
print(spam[1][3])

spam = ['cat', 'bat', 'rat', 'elephant']
print(spam[-1]) #going backwards
print(spam[-2])

print('The ' + spam[-2] + ' ate the ' + spam[-1] + '.')

# slices now

print(spam[1:3])

# changing values in a list

spam = [10, 20, 30, 40, 50]
print(spam)

spam[1] = 'Hello' #replacing item
print(spam)

spam[1:3] = ['BEEP', 'BOOP'] #replacing slice
print(spam)

print(spam[:2]) #leaving out index in a slice
print(spam[3:])

del spam[2] # deleting item in list
print(spam)

print(len(spam)) #returning length of spam

spam = [1,2] + [3,4] #list concatenation
print(spam)

spam = spam * 3 #list multiplication
print(spam)

spam = list('Hello') #listifying a string
print(spam)

spam = ['howdy', 'hi', 'hey'] # if something is in or not in
print('howdy' in spam)
print('howdy' not in spam)
