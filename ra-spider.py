import bs4 as bs
import urllib.request
from datetime import datetime



source = urllib.request.urlopen('https://www.residentadvisor.net/club.aspx?id=90981')
soup = bs.BeautifulSoup(source, 'lxml')
events = soup.find('ul', class_='list')
events_2step = events.find_all('a')[0:6]
for event in events_2step:
	print('\n')
	event_link_partial = event.attrs['href']
	event_id = event_link_partial.split('/')[2]
	print("event_id: " + event_id)
	event_link = "https://www.residentadvisor.net" + event_link_partial
	print("event_link: " + event_link)
	source_event = urllib.request.urlopen(event_link)
	soup_event = bs.BeautifulSoup(source_event, 'lxml')
	title = soup_event.find('h1').text
	print("event_title: " + title)
	date_start = soup_event.find('a', {"class": "cat-rev"}).text
	time = soup_event.find('aside', {"id": "detail"}).find('ul').find('li').contents[-1]
	time_start = time.split('-')[0]
	print(time)
	start_dateandtime = date_start + ' ' + time_start
	start_dateandtime = start_dateandtime.strip()
	print(start_dateandtime)
	start_datetime = datetime.strptime(start_dateandtime, '%d %b %Y %H:%M')
	print("START: "+ date_start)
	print(start_datetime)
	
	lineup = soup_event.find('p', {"class": "lineup"})
	print(lineup)
	description = soup_event.find('div', {"class": "left"}).find_all('p')[1]
	print("DESCRIPTION")
	print(description)

	try:
		flyer_link_partial = soup_event.find('div', {"class": "flyer"}).find('a').attrs['href']
		flyer_link = "https://www.residentadvisor.net" + flyer_link_partial
		print(flyer_link)
		print('\n')
	except:
		print("no flyer")
	
	if soup_event.find('li', {"id": "tickets"}) != None:
		print('*******************************selling tickets')
		ticket_uri = event_link
		print(ticket_uri)
	else:
		print("no ticket uri")

	




