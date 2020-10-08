# for loops with lists, multiple assignment, and augmented operators
for i in range(4):
    print(i)

print(range(4))

for i in [0,1,2,3]:
    print(i)

print(list(range(4))) 

print(list(range(0, 100, 2))) # good for getting a list of numbers


supplies = ['pens', 'staplers', 'food', 'snacks']

for i in range(len(supplies)): # for when you need the value of the index as well
    print('Index ' + str(i) + ' in supplies is: ' + supplies[i])

supplies = ['pens', 'staplers', 'food', 'snacks',
            'pens', 'staplers', 'food', 'snacks',
            'pens', 'staplers', 'food', 'snacks']

for i in range(len(supplies)): # works for big lists
    print('Index ' + str(i) + ' in supplies is: ' + supplies[i])

cat = ['fat', 'orange', 'loud']
size, color, disposition = cat #multiple assignment

print(size)
print(color)
print(disposition)

size, color, disposition = 'tiny', 'green', 'meek' #multiple assignment both ways

print(size)
print(color)
print(disposition)

a = 'a'
b = 'b'

b, a = a, b #swapping variables

print(a)
print(b)

spam = 0
spam = spam + 1
spam += 1 #augmented assignment
print(spam)

spam -= 1
print(spam)

spam *= 6
print(spam)

spam /= .5
print(spam)

spam %= 5 #remainder
print(spam)


