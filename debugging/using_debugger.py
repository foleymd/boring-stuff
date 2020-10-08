# using the IDLE debugger & using breakpoints

# enable IDLE debugger by going to Debug in the top menu and selecting debugger


print('enter first number:')
first = int(input())
print('enter second number:')
second = int(input())
print('enter third number:')
third = int(input())
# right click and select "set breakpoint" to set a breakpoint for the debugger
# doing so will highlight the code as well
# the code will execute in the debugger at normal speed until it hits the breakpoint
total = first + second + third
print('The sum is ' + str(total))
