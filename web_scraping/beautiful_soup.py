# parsing html with beautiful soup

import bs4, requests # bs4 = beautiful soup


response_object = requests.get('http://www.professionaled.utexas.edu/ \
                                online-project-management-certificate-program')
response_object.raise_for_status()

#pass html.parser to avoid an ugly warning message
soup = bs4.BeautifulSoup(response_object.text, 'html.parser') 

# pass the css selector for what we are looking for - use chrome developer tools to inspect,
# then click on the ellipsis in the elements pane for that item, then select copy selector
# this returns a list of all elements that match
elements = soup.select('#ut-page-content > div:nth-child(2) > div.middle_content.row > \
                       div.column.small-12.medium-4.large-3 > div.at-a-glance > \
                       div.field.field_scc_tuition > div.field-items > div')

print(elements) # is a list with outer div tags included

# we only want the first element in the list & only the text value
print(elements[0].text) 

# you can use the strip method to remove whitespace from the text, e.g.:

print(tuition[0].text.strip())  

