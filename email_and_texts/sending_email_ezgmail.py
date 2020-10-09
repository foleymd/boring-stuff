''' sending and receiving email with gmail api through ezgmail
   enable gmail api and get a credentials.json file here
   https://developers.google.com/gmail/api/quickstart/python/
'''
import ezgmail, os

# the below command creates token.json file -
# needed to get started but not thereafter
# ezgmail.init()

# tells you which email address token.json is configured for
print(ezgmail.EMAIL_ADDRESS) 

# arguments are recipient email, subject, body, and attachment
ezgmail.send('email@gmail.com', 'EZ Mail!', 'Are\'t you glad you received this email?', \
             ['sending_email_ezmail.py']) # this last bit adds an attachment - in this case this python file


# you can cc and bcc people as well

ezgmail.send('email@gmail.com', 'CC and BCC', 'I\'m a body',
cc='example@austin.utexas.edu', bcc='otherfriend@example.com,someoneelse@example.com')
