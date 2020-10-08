# logging

import logging

# the following prints out the log messages
#logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

#this one prints the log messages to a file
logging.basicConfig(filename='log.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# five debug levels are debug, info, warning, error, and critical
# comment out to remove logging, uncomment to add logging back
# the following disables messaging at listed level or lower - since it's CRITICAL, that means all of them
# logging.disable(logging.CRITICAL) 

logging.debug('Start of program.')

def factorial(n):
    logging.debug('Start of factorial(%s)' % (n))
    total = 1
    for i in range(1, n + 1):
        total *= i
        logging.debug('i is %s, total is %s' % (i, total))
    logging.debug('Return value is %s' % (total))
    return total

print(factorial(7))

logging.debug('End of program.')
