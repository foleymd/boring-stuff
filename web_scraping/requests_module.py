# downloading from the web with the requests module
# documentation at https://requests.readthedocs.io/en/master/
# requests just downloads content and then you can do whatever you want with it
# if you have to log in, this might not be the best way

import requests

response_object = requests.get('https://automatetheboringstuff.com/files/rj.txt')

print(response_object.status_code)

print(response_object.text[:500])

print(response_object.raise_for_status())

bad_response = requests.get('https://automatetheboringstuff.com/files/foobar.txt')
 
print(bad_response.status_code)

# print(bad_response.raise_for_status()) # put this in a try except block if you want!

# creating a new file; pass it the new file name and the wb for write-binary
# mode to maintain unicode encoding for the text (vs. plain text)

rj_play = open('RomeoAndJuliet.txt', 'wb')

# to write the content to a file, use a for loop with the iter_content method
# returns byte data type - this is 100K bytes

for chunk in response_object.iter_content(100000):
    print(rj_play.write(chunk))

    
    
    
