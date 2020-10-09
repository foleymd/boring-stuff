# reading emails from a gmail account

import ezgmail

# view unread
unreadThreads = ezgmail.unread()
print(ezgmail.summary(unreadThreads))
