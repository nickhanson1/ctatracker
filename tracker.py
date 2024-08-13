import sys
import json
import requests
import xmltodict
from datetime import datetime, timezone, timedelta
from tzlocal import get_localzone


API_KEY = "8b506f5e981e451b8174228d287e0d57"


MAP_ID = 40320
STATION = "Division"
ROUTE_DEST = "Forest Park"


def query(url):
    #while True:
    response = requests.post(url) 
    data = xmltodict.parse(response.content)
    return data

def now_in_cst():
    nowT = datetime.now()
    cst = timezone(timedelta(hours=-5))
    local_timezone = get_localzone()

    now_localized = nowT.replace(tzinfo=local_timezone)
    now_converted = now_localized.astimezone(cst)

    now_converted = now_converted.replace(tzinfo=None)
    return now_converted

def get_times(data):
    if(data['ctatt']['errCd'] != '0'):
        print("Error: " + data['ctatt']['errNm'])
        return None
    
    data = data['ctatt']['eta']
    arrivals = []

    for train in data:
        if(train['destNm'] == ROUTE_DEST):
            arrT = train["arrT"]
            time_format = "%Y%m%d %H:%M:%S"
            arrT = datetime.strptime(arrT, time_format)
            #
            # TIME ZONE SHENANIGANS
            #
            nowT = now_in_cst()
            elapsed_time = arrT - now_in_cst()            

            arrivals.append([STATION, ROUTE_DEST, elapsed_time.seconds // 60])
    
    return arrivals


def main():
    data = query(f"http://lapi.transitchicago.com/api/1.0/ttarrivals.aspx?key={API_KEY}&mapid={MAP_ID}&max=10")
    print(get_times(data))
    sys.exit(0)

main()
