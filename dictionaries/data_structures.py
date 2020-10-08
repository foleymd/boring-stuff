# data structures
import pprint

cat = {'name':  'Cat', 'age': 7, 'color': 'orange'}
print(cat)

all_cats = []
all_cats.append({'name':  'Sheila', 'age': 7, 'color': 'orange'})
all_cats.append({'name':  'Kitten', 'age': 10, 'color': 'gray'})
all_cats.append({'name':  'Cutie', 'age': 1, 'color': 'black'})
pprint.pprint(all_cats)

#making a tic-tac-toe data structure and print output

the_board = {'top-L': ' ',
             'top-M': ' ',
             'top-R': ' ',
             'mid-L': ' ',
             'mid-M': ' ',
             'mid-R': ' ',
             'low-L': ' ',
             'low-M': ' ',
             'low-R': ' '}

the_board['mid-M'] = 'X'
the_board['mid-L'] = 'X'
the_board['mid-R'] = 'X'
the_board['low-M'] = 'O'
the_board['top-M'] = 'O'
the_board['low-R'] = 'O'

pprint.pprint(the_board)
             
def print_board(board):
    print (board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print ('-----')
    print (board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print ('-----')
    print (board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

print_board(the_board)

print(type(int('42'))) #type function tells you data type of object
print(type(the_board))
