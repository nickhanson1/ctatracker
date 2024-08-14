from configs import DISPLAY_WIDTH, DEST_SHORT_NAMES


def format(station, destination, time):
    tstring = str(time) + " min."
    if time == 0:
        tstring = "Now"
    if len(build_string(station, destination, tstring)) <= DISPLAY_WIDTH:
        return build_string(station, destination, tstring) 
    destination = DEST_SHORT_NAMES[destination]
    if len(build_string(station, destination, tstring)) <= DISPLAY_WIDTH:
        return build_string(station, destination, tstring)
    return build_string(station, destination, tstring, arrow = True)[0:DISPLAY_WIDTH]

def build_string(station, destination, time, arrow=False):
    if arrow:
        return f"{station}*{destination}:{time}"
    return f"{station} to {destination}:{time}"