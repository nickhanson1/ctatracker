import sys
import json
import requests
import xmltodict
from datetime import datetime, timezone, timedelta
from tzlocal import get_localzone
import time

from font import LETTERS


API_KEY = "8b506f5e981e451b8174228d287e0d57"


MAP_ID = 40320
STATION = "Division"
ROUTE_DEST = ["Forest Park", "UIC-Halsted"]
ROUTE_SHORT_NAMES = {"Forest Park" : "FP", "UIC-Halsted" : "UIC"}

DISPLAY_WIDTH = 30
DISPLAY_HEIGHT = 2

LETTER_WIDTH = 5
LETTER_HEIGHT = 7

"""
    Queries the CTA server with the given url; the url contains the mapid of the station,
    the key, and the maximum number of arrivals to return. The function returns the data 
    as a dictionary.    

    Args:
        url (String): The url to query the CTA server with.
    Returns:
        dict: The data returned from the CTA server.
    Raises:
        None
"""
def query(url):
    #while True:
    response = requests.post(url) 
    data = xmltodict.parse(response.content)
    return data

"""
    Returns the current time in the CST timezone.

    Args:
        None
    Returns:
        datetime: The current time in the CST timezone.
    Raises:
        None
"""
def now_in_cst():
    nowT = datetime.now()
    cst = timezone(timedelta(hours=-5))
    local_timezone = get_localzone()

    now_localized = nowT.replace(tzinfo=local_timezone)
    now_converted = now_localized.astimezone(cst)

    now_converted = now_converted.replace(tzinfo=None)
    return now_converted

"""
    Parses the data returned from the CTA server and returns a list of arrivals. 
    Also returns an error message if the data contains an error code.

    Args:
        data (dict): The data returned from the CTA server
    Returns:
        list: A list of arrivals in the format [station, destination, time_until_arrival]
        str: An error message if the data contains an error code
    Raises:
        None
"""
def get_arrivals(data):
    if(data['ctatt']['errCd'] != '0'):
        print("Error: " + data['ctatt']['errNm'])
        return None, data['ctatt']['errNm']
    
    data = data['ctatt']['eta']
    arrivals = []

    for train in data:
        if(train['destNm'] in ROUTE_DEST):
            arrT = train["arrT"]
            time_format = "%Y%m%d %H:%M:%S"
            arrT = datetime.strptime(arrT, time_format)
            #
            # TIME ZONE SHENANIGANS
            #
            nowT = now_in_cst()
            elapsed_time = arrT - now_in_cst()            

            arrivals.append([STATION, train['destNm'], elapsed_time.seconds // 60])
    
    return arrivals, None 

"""
    Returns a display of the given string list. The display is a 2D list of 0s and 1s.

    Args:
        str_list (list): A list of the strings to display
    Returns:
        list: A 2D list of 0s and 1s representing the display
    Raises:
        None
"""
def get_display(str_list):
    display = [[0] * (DISPLAY_WIDTH * LETTER_WIDTH)] * (DISPLAY_HEIGHT * LETTER_HEIGHT)
    for i, line in enumerate(str_list):
        for j, char in enumerate(line):
            letter = LETTERS[ord(char)]
            for k, row in enumerate(letter):
                display[i * LETTER_HEIGHT + k] = display[i * LETTER_HEIGHT + k][:j * LETTER_WIDTH] + row + display[i * LETTER_HEIGHT + k][j * LETTER_WIDTH + LETTER_WIDTH:]
    return display

def loop():
    display = [[0] * (DISPLAY_WIDTH * LETTER_WIDTH)] * (DISPLAY_HEIGHT * LETTER_HEIGHT)
    while True:
        data = query(f"http://lapi.transitchicago.com/api/1.0/ttarrivals.aspx?key={API_KEY}&mapid={MAP_ID}&max=10")
        arrivals, err = get_arrivals(data)

        if err != None:
            display = get_display([err])
        else:
            print
            timetable = []
            for entry in arrivals:
                if len(timetable) < 2:
                    time_until = "Now"
                    if entry[2] > 1:
                        time_until = str(entry[2]) + " min."
                    timetable.append(entry[0] + " to " + ROUTE_SHORT_NAMES[entry[1]] + ":" + time_until)

            display = get_display(timetable)
            for row in display:
                print(row)
            

            print(timetable)
            time.sleep(30)
    
loop()
