# 507/206 Homework 6 Part 1
import requests
from bs4 import BeautifulSoup
import sys

#### Part 1 ####
print('\n*********** PART 1 ***********')
print("Mark's page -- Alt tags\n")

### Your Part 1 solution goes here
www = sys.argv[1]
    
html = requests.get('http://newmantaylor.com/gallery.html').text
soup = BeautifulSoup(html, 'html.parser')
    
img_tag = soup.find_all("img")
for a in img_tag:
	if a.has_attr("alt"):
		print(a["alt"])
	else:
		print("No alternative text provided!")


