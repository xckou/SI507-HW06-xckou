# 507/206 Homework 6 Part 2
import requests
from bs4 import BeautifulSoup


#### Part 2 ####
print('\n*********** PART 2 ***********')
print('Michigan Daily -- MOST READ\n')

### Your Part 2 solution goes here

html = requests.get('https://www.michigandaily.com/').text
soup = BeautifulSoup(html, 'html.parser')

# searching_div = soup.find('div', attrs = {"class":"panel-pane pane-mostread"})
searching_div= soup.find('div', attrs = {'class': "view view-most-read view-id-most_read view-display-id-panel_pane_1 view-dom-id-99658157999dd0ac5aa62c2b284dd266"})
# print(searching_div)

mr = searching_div.select("ol li")
for li in mr:
	print(li.text)
# print(mr)
# for a in mr:
# 	abstract = a.select("ol")
# 	print(abstract)
	# for li in abstract:
	# 	print(li)

