my_cat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}
print(my_cat['size'])

print('My cat has ' + my_cat['color'] + ' fur.')

spam = {12345: 'Luggage combination', 42: 'The Answer'}

print([1,2,3] == [3,2,1]) #should be false for list unless it's exact

my_cat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}
your_cat = {'size': 'fat','disposition': 'loud', 'color': 'gray'}

print(my_cat == your_cat) #should be true because ordering doesn't matter in dicts

print('size' in my_cat) #whether key is in there
print('size' not in my_cat)

#dictionary methods
# these return listy objects
print(list(my_cat.keys()))
print(list(my_cat.values()))
print(list(my_cat.items())) #returns list of two-item tuples

#can use keys and values in loops
for i in my_cat.keys():
    print(i)

for i in my_cat.values():
    print(i)

#multiple assignments for keys and values

for k,v in my_cat.items():
    print(k,v)

for i in my_cat.items(): #prints tuples
    print(i)

print('fat' in my_cat.values()) #true or false if value is there

# get method (takes key and default as args)

print(my_cat.get('color', 'orange')) #key/value is available
print(my_cat.get('age', 37)) #key/value is not available

# another example of the get method
picnic_items = {'apples': 6, 'cups': 9}
print('I am bringing ' + str(picnic_items.get('napkins', 0)) + ' napkins to the picnic.')

#setdefault method - sets default value if key doesn't exist
my_cat.setdefault('claws', 'many')
print(my_cat.items())


