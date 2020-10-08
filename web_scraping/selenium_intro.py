# controlling the browser with selenium
# got lots of geckodriver errors. installed and added to path.
# the executable_path = '/usr/local/bin/geckodriver' bit isn't in the instructions
# example css selector used caused an error, I chose a different one
# selenium docs: https://selenium-python.readthedocs.io/

import sys
from selenium import webdriver

# opening firefox
browser = webdriver.Firefox(executable_path = '/usr/local/bin/geckodriver')

# goint to url below
browser.get('https://automatetheboringstuff.com')

# selecting a clickable link via its css selector
elem = browser.find_element_by_css_selector('.main > div:nth-child(1) > \
                                            p:nth-child(25) > a:nth-child(1)')
# clicking on the selected link
elem.click()

# getting all paragraph elements returned in a list
elems = browser.find_elements_by_css_selector('p')

# print number of items in the above list
print(len(elems))

browser.quit()

# you can find elements by class, id, text, name, tag.
# see https://selenium-python.readthedocs.io/locating-elements.html
# note it has "find_element" and "find_elements"


# switching to a different website because the example site has changed
browser = webdriver.Firefox(executable_path = '/usr/local/bin/geckodriver')
browser.get('https://professionaled.utexas.edu')

# locating the search field
search_elem = browser.find_element_by_class_name('nav-search-input')

# entering search input
search_elem.send_keys('Online Project Management Certificate Program')

# submitting search
search_elem.submit()

# back, forward, refresh, quit
browser.back()
browser.forward()
browser.refresh()
browser.quit()


#opening another window

browser = webdriver.Firefox(executable_path = '/usr/local/bin/geckodriver')
browser.get('https://automatetheboringstuff.com')

# find and print text from a single paragraph
elem = browser.find_element_by_css_selector('.main > div:nth-child(1) > p:nth-child(8)')
print(elem.text) #.text is a "member variable"

# find and print full text from page
elem = browser.find_element_by_css_selector('html')
print(elem.text) 

browser.quit()

