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
file = open("log.txt","w") 
for event in events_2step:
	event_link_partial = event.attrs['href']
	event_id = event_link_partial.split('/')[2]
	event_link = "https://www.residentadvisor.net" + event_link_partial
	req_event = Request(event_link, headers={'User-Agent': 'Mozilla/5.0'})
	web_byte_event = urlopen(req_event).read()
	webpage_event = web_byte_event.decode('utf-8')
	soup_event = bs.BeautifulSoup(webpage_event, 'lxml')
	title = soup_event.find('h1').text
	date_start = soup_event.find('aside', {"id": "detail"}).find('ul').find('li').find('a').contents[0]
	time = soup_event.find('aside', {"id": "detail"}).find('ul').find('li').contents[-1]
	time_start = time.split('-')[0]
	start_dateandtime = date_start + ' ' + time_start
	start_dateandtime = start_dateandtime.strip()
	try:
		start_datetime = datetime.strptime(start_dateandtime, '%d %b %Y %H:%M')
	except: 
		start_datetime = "problem with the date" 

	lineup = soup_event.find('p', {"class": "lineup"})
	description = soup_event.find('div', {"class": "left"}).find_all('p')[1]

	try:
		flyer_link_partial = soup_event.find('div', {"class": "flyer"}).find('a').attrs['href']
		flyer_link = "https://www.residentadvisor.net" + flyer_link_partial
	except:
		flyer_link = "No flyer"
	
	if soup_event.find('li', {"id": "tickets"}) != None:
		ticket_uri = event_link
	else:
		ticket_uri = "None"
	file.write("\n")
	file.write("\n")
	file.write("-----*********-------")
	file.write("\n")
	file.write("event_id: " + event_id)
	file.write("\n")
	file.write("event_link: " + event_link)
	file.write("\n")
	file.write("title: " + title)
	file.write("\n")
	file.write("date_start: " + date_start)
	file.write("\n")
	file.write("time: " + time)
	file.write("\n")
	file.write("time_start: " + time_start)
	file.write("\n")
	file.write("start_dateandtime: " + start_dateandtime)
	file.write("\n")
	file.write("lineup: " + str(lineup))
	file.write("\n")
	file.write("description: " + str(description))
	file.write("\n")
	file.write("flyer_link: " + flyer_link)
	file.write("\n")


file.close() 
	


""" 





>>> from datetime import datetime
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> source = urllib.request.urlopen('https://www.residentadvisor.net/club.aspx?id=90981')
>>> soup = bs.BeautifulSoup(source, 'lxml')
>>> events = soup.find('ul', class_='list')
>>> events_2step = events.find_all('a')
>>> 
>>> 
>>> 
>>> event = events_2step[0]
>>> event
<a href="/events/1075688"><img height="76" src="/images/events/flyer/2018/6/de-0601-1075688-list.jpg" width="152"/></a>
>>> event_link_partial = event.attrs['href']
>>> event_link = "https://www.residentadvisor.net" + event_link_partial
>>> source_event = urllib.request.urlopen(event_link)
>>> soup_event = bs.BeautifulSoup(source_event, 'lxml')
>>>     title = soup_event.find('h1').text
  File "<stdin>", line 1
    title = soup_event.find('h1').text
    ^
IndentationError: unexpected indent
>>> title = soup_event.find('h1').text
>>> testetime = soup_event.find('aside', {"id": "detail"}).find('ul').find('li').contents
>>> testetime
[<div>Date /</div>, 'Friday', <br/>, <a class="cat-rev" href="/events/de/berlin/day/2018-06-01">1 Jun 2018</a>, <br/>, '20:00 - 12:00']
>>> testetime[0]
<div>Date /</div>
>>> testetime = soup_event.find('aside', {"id": "detail"}).find('ul').find('li').find('a')
>>> testetime
<a class="cat-rev" href="/events/de/berlin/day/2018-06-01">1 Jun 2018</a>
>>> testtime.contents
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'testtime' is not defined
>>> testetime.contents
['1 Jun 2018']
>>> testetime.contents[0]
'1 Jun 2018'
>>> 
 """











