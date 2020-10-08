import bs4, requests

def get_cpe_tuition(product_url):

    response_object = requests.get(product_url)
    
    response_object.raise_for_status()

    #pass html.parser to avoid an ugly warning message
    soup = bs4.BeautifulSoup(response_object.text, 'html.parser') 

    # pass the css selector for what we are looking for - use chrome developer tools to inspect,
    # then click on the ellipsis in the elements pane for that item, then select copy selector
    elements = soup.select('#ut-page-content > div:nth-child(2) > div.middle_content.row > \
                            div.column.small-12.medium-4.large-3 > div.at-a-glance > \
                            div.field.field_scc_tuition > div.field-items > div')

    tuition = elements[0].text.strip()
    return tuition

tuition = get_cpe_tuition('https://professionaled.utexas.edu/online-project-management-certificate-program')

print('The tuition is: ' + tuition)
