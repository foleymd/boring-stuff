# string formatting

name = 'Alice'
time = 'now'
food = 'turnips'

invitation = name + ' you are invited to a party ' + time + '; please bring ' + food
print(invitation)

print('Hello, %s, you are invited to a party %s; please bring %s.' % (name, time, food))
