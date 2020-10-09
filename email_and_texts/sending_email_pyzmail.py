''' sending emails from gmail

note, if you have two factor turned on, you need to turn it off:
https://myaccount.google.com/security?pmr=1

additionally, you'll need to allow less secure access to your gmail:
https://myaccount.google.com/lesssecureapps

signing in repeatedly can cause gmail to block your sign in attempts &
limit of 100-1000 emails sent a day depending on your email service

Google can allow you to generate an app specific password:
https://support.google.com/accounts/answer/185833?hl=en
'''


import smtplib

# pass domain name and port. standard smtp port is 587
conn = smtplib.SMTP('smtp.gmail.com', 587)

#type of 
print(type(conn))

# connects to server
print(conn.ehlo())

# starts tls for encryption so you can pass your password safely
conn.starttls()

# send email address and password
conn.login('email@gmail.com', 'password') #real stuff redacted

# from address, to address, then body of email including headers, newlines
# required after subject email header. send email.
conn.sendmail('email@gmail.com', 'email@gmail.com', 'Subject: So long...\n\n Dear Marjorie, \n So long and thanks for all the fish. \n\n Signed, Marjorie')

# disconnect from SMTP server
conn.quit()
