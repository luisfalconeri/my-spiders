import bs4 as bs
import urllib.request
from datetime import datetime



source = urllib.request.urlopen('https://www.residentadvisor.net/club.aspx?id=90981')
soup = bs.BeautifulSoup(source, 'lxml')
events = soup.find('ul', class_='list')
events_2step = events.find_all('a')
file = open("log.txt","w") 
counter = 0
for event in events_2step:
    counter += 1
    event_link_partial = event.attrs['href']
    event_link = "https://www.residentadvisor.net" + event_link_partial
    source_event = urllib.request.urlopen(event_link)
    soup_event = bs.BeautifulSoup(source_event, 'lxml')
    title = soup_event.find('h1').text
    date_start = soup_event.find('a', {"class": "cat-rev"}).text
    testetime = soup_event.find('aside', {"id": "detail"}).find('ul').find('li').contents
    print(testetime)
    time = soup_event.find('aside', {"id": "detail"}).find('ul').find('li').contents[-1]
    time_start = time.split('-')[0]
    start_dateandtime = date_start + ' ' + time_start
    start_dateandtime = start_dateandtime.strip()
    try:
        start_datetime = datetime.strptime(start_dateandtime, '%d %b %Y %H:%M')
    except: 
        start_datetime = "problem with the date" 
        
        
    file.write("\n")
    file.write("-----*********-------")
    file.write("\n")
    file.write("#: " + str(counter))
    file.write("event_link: " + event_link)
    file.write("\n")
    file.write("IMPORTANT -------!!!!!!")
    file.write(str(testetime))
    file.write("date_start: " + date_start)
    file.write("\n")
    file.write("time: " + time)
    file.write("\n")
    file.write("time_start: " + time_start)
    file.write("\n")
    file.write("start_dateandtime: " + start_dateandtime)
    file.write("\n")
    
    
file.close() 
	














