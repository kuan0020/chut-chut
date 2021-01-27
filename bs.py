from bs4 import BeautifulSoup
import requests 
from datetime import datetime 
import math 

def json_datetime_convert(json_dt):
    json_dt = str(json_dt)
    date, time = json_dt.split('T')
    time = time.rsplit(':',1) # remove seconds from time
    return str(time[0])

def get_info(bus_stop: str):
    actual = []
    dep_text = []
    # dep_time = []
    bus_num = []
    
    page = requests.get('https://svc.metrotransit.org/NexTrip/' + str(bus_stop))
    soup = BeautifulSoup(page.content, 'html.parser')
    nex_trips = soup.find_all('nextripdeparture')

    for i in range(len(nex_trips)):
        actual.append(nex_trips[i].actual.string)
        dep_text.append(nex_trips[i].departuretext.string)
        # dep_time.append(json_datetime_convert(nex_trips[i].departuretime.string))
        bus_num.append(nex_trips[i].find_all('route')[0].string)

    actual = actual[:math.ceil(len(actual)/4)]
    dep_text = dep_text[:math.ceil(len(dep_text)/4)]
    # dep_time = dep_time[:len(dep_time)//4]
    bus_num = bus_num[:math.ceil(len(bus_num)/4)]
    
    items = []
    for i in range(len(actual)):
        item = dict(bus_stop=str(bus_stop), actual=actual[i], dep_text=dep_text[i], bus_num=bus_num[i])
        items.append(item)

    if len(items) == 0:
        items.append(dict(bus_stop=str(bus_stop), actual='-', dep_text='-', bus_num='-'))
    return items
