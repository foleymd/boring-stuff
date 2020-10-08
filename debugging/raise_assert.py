# the raise and assert statements
import traceback, os

# print a box
def box_print(symbol, width, height):

    if len(symbol) != 1:
        raise Exception('The input symbol must be a single-character string.')
    

    if (width < 2) or (height < 2) :
        raise Exception('Box width and height must be greater than or equal to 2.')
    
    print(symbol * width) #top line

    for i in range (height - 2):
        print(symbol + (' ' * (width -2)) + symbol) #outer edge + inner space + outer edge
        
    print(symbol * width) #bottom line

print('Printing boxes: \n')        
box_print('$', 10, 9)
box_print('#', 15, 4)

print('\nExceptions : \n')
# box_print('!!', 15, 4) # raises single-character exception
# box_print('G', 1, 4) # raises width/height exceptions

# raise Exception('This is the error message.')

try:
    raise Exception('This is the error message.')
except:
        error_file = open('error_log.txt', 'a')
        error_file.write(traceback.format_exc())
        error_file.close()
        print('The traceback info was written to error_log.txt')

# assertions are checks to make sure nothing weird is happening
# if asserts fail, programs should crash - they help you find problems sooner rather than later
# assertions are for programmer errors and not non-fatal errors

print('\nAssertions: \n')

assert False, 'This is the error message.'


