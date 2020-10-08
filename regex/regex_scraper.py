# regex phone and email address web scraper from document

import re, pyperclip, pprint

# create a regex object for phone numbers

phone_regex = re.compile(r'''
                        #123-456-7890, 555-1212, (512) 666-7777, 123-5678 ext 12345, ext. 12345, x12345
                        (
                        ((\d\d\d)|(\(\d\d\d\)))?         # area code (optional)
                        (\s|-)                         # separator - space, hypen, period
                        \d\d\d                           # first three digits
                        (\s|-)                         # separator - space, hypen, period
                        \d\d\d\d                         # last 4 digits
                        (((ext(\.)?\s)|x)                # extension word(optional)
                        (\d{2,5}))?                      # extension number(optional)          
                        )
                        ''', re.VERBOSE)

# create a regex object for email addresses

email_regex = re.compile(r'''
                         [a-zA-Z0-9_.+]+ # name * don't need to escape characters in side character class
                         @                # at
                         [a-zA-Z0-9_.+]+ # domain

                         ''', re.VERBOSE)

# get text from clipboard
text = pyperclip.paste()
text = 'example@austin.utexas.edu 123-456-7896 example@gmail.com 134-567-8902' #sample text to run without copy/paste from file

# extract emails and numbers

extracted_phone = phone_regex.findall(text)
extracted_email = email_regex.findall(text)

all_phone_numbers = []

for phone_number in extracted_phone:
    all_phone_numbers.append(phone_number[0])

print(extracted_email)
print(extracted_phone)

results = '\n'.join(all_phone_numbers) +'\n' + '\n'.join(extracted_email)
print(results)

pyperclip.copy(results)
