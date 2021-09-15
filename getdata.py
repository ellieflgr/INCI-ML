import requests
#import pandas as pd
from bs4 import BeautifulSoup 

def match_ingredients(tag):
    return tag.name == "div" and tag["class"] == "text"

links_good = open('links_good.txt', 'r')
links = links_good.readlines()

url = requests.get(links[1].rstrip())

htmltext = url.text

#print(htmltext)

#create soup object of the html code
soup_html = BeautifulSoup(htmltext, features="html.parser")

#print(soup_html.title.text)

#product name equals page title
productname = soup_html.title.text

#parse out ingredient list

inci_id = 'inci'

ingredient_list = soup_html.find("div")

#print(ingredient_list)

#print(ingredient_list.text)

res = soup_html.find_all(match_ingredients)

print(res)

