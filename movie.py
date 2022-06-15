from bs4 import BeautifulSoup as bs
import requests

r = requests.get("https://en.wikipedia.org/wiki/Toy_Story_3")

# convert to a beautiful soup object
soup = bs(r.content)

# print out the HTML
contents = soup.prettify()
#print(contents)

info_box = soup.find(class_="infobox vevent")
print(info_box)



