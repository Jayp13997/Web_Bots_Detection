from bs4 import BeautifulSoup
import requests
import random

#Web Network URL
Web_Network_URL = "http://localhost:50000/"
#Web_Network_URL = "https://people.cs.rutgers.edu/~jpk164/"

#var to capture all the different herf links for all the pages
all_links = []
visited_links = []

#get all the text from a page URL
def get_text(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    text = soup.get_text()
    return text

#get all the herf links from a page URL
def get_links(url):
    links = []
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    page_links = soup.find_all('a')
    for link in page_links:
        link_url = link["href"]
        links.append(link_url)
    return links

#add only the new links to all_links to have an overall global list of all the links
def append_all_links(url, all_links=[]):
    new_links = get_links(url)
    for new_link in new_links:
        if new_link not in all_links and new_link not in visited_links:
            print(new_link)
            all_links.append(new_link)
    return all_links

#get herf links from home page
all_links = append_all_links(Web_Network_URL, all_links)
#print(all_links)

#for each link in all_links, get additional new links and add them to all_links until we've gotten all possible links
while len(all_links) > 0:
    link = random.choice(all_links)
    append_all_links(Web_Network_URL + link, all_links)
    visited_links.append(link)
    all_links.remove(link)


#show page text for each link/page
page_text = get_text(Web_Network_URL)
for link in visited_links:
    print('text from: ' + str(Web_Network_URL + link))
    page_text = get_text(Web_Network_URL + link)
    print(page_text)



