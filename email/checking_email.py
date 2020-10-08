''' checking email messages via IMAP
 python has imaplib module but we are using different ones
 
 could not pip install pyzmail; used pip install pyzmail36 instead

 need to run this command from inside the Python 3.8 folder:
 ./Install\ Certificates.command
 or else you will get a ssl cert failure

 I couldn't get the ['SINCE 10-Aug-2020'] style syntax to work for
 conn search, so I imported date and used the below format

 imapclient docs: https://imapclient.readthedocs.io/en/2.1.0/
'''

import imapclient, pyzmail
from datetime import date

# pass name of server and set ssl encryption to true
conn = imapclient.IMAPClient('imap.gmail.com', ssl=True)

# log in with name and password
conn.login('email@gmail.com', 'password')

# list all email folders
print(conn.list_folders())

# pass folder name and readonly to precent deletion
print(conn.select_folder('INBOX', readonly=True))

## allows you to delete:
# print(conn.select_folder('INBOX', readonly=False))
# UIDs = conn.search(['SINCE', date(2020, 10, 6)])
# conn.delete_massages([63020, 63019])
## or
# conn.delete_massages(UIDs)

#pass string inside list
# UIDs = conn.search(['SINCE 05-Oct-2020'])
UIDs = conn.search(['SINCE', date(2020, 10, 6)])
print(UIDs)

# fetching a specific email - pass it the UID snad the parts you want
# 
raw_message = conn.fetch([63020],['BODY[]', 'FLAGS'])

print(raw_message)

# this parses the message; it returns a pyzmail msg object
message = pyzmail.PyzMessage.factory(raw_message[63020][b'BODY[]'])

# print subjects and addresses
print(message.get_subject())
print(message.get_addresses('from'))
print(message.get_addresses('to'))

# is it an html or text email?

print(message.text_part) # does it have a text part?
print(message.html_part) # does it have an html part?

# formatting is usually UTF-8 but you may need to fiddle with it
# this prints a readable email!
print(message.text_part.get_payload().decode('UTF-8'))

# log out
conn.logout()
