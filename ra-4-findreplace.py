import bs4 as bs
from urllib.request import Request, urlopen
from datetime import datetime




url='https://www.residentadvisor.net/club.aspx?id=90981'
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
web_byte = urlopen(req).read()
webpage = web_byte.decode('utf-8')
soup = bs.BeautifulSoup(webpage, 'lxml')
events = soup.find('ul', class_='list')
events_2step = events.find_all('a')
event = events_2step[0]
event_link_partial = event.attrs['href']
event_link = "https://www.residentadvisor.net" + event_link_partial
print(event_link)
req_event = Request(event_link, headers={'User-Agent': 'Mozilla/5.0'})
web_byte_event = urlopen(req_event).read()
webpage_event = web_byte_event.decode('utf-8')
soup_event = bs.BeautifulSoup(webpage_event, 'lxml')
title = soup_event.find('h1').text
lineup = str(soup_event.find('p', {"class": "lineup"}))
print(lineup)
description_html = soup_event.find('div', {"class": "left"}).find_all('p')[1]
description = str(description_html)
print("\n \n HTML description")
print(description)
lineup_updated = lineup.replace('<a href="', '<a href="https://www.residentadvisor.net/dj/monkeymaffia')
description_updated = description.replace('<a href="', '<a href="https://www.residentadvisor.net/dj/monkeymaffia')
print("\n \n LINE-UP UPDATED")
print(lineup_updated)

print("\n \n Description UPDATED")
print(description_updated)



        
        














