# import
import time
import os
from blink1.blink1 import Blink1

hosts = {
    'google DNS': ['8.8.8.8', 'Red'],
    'telstra gateway max': ['192.168.20.1', 'Orange'],
    'ubiquiti edgerouter poe 5': ['192.168.20.1', 'Yellow'],
    'apple airport extreme': ['192.168.20.2', 'Blue'],
    'secondary DNS': ['192.168.20.5', 'Green'],
    'test device': ['192.168.22.21', 'Purple']
}

status = list()
blink_colours = list()


def blink(colour):
    b1 = Blink1()
    b1.play_pattern(colour)
    b1.close()


def ping():
    for x in hosts.values():
        response = os.system('ping -c 1 ' + x[0])
        if response == 0:
            status.append(1)
        else:
            status.append(0)


while True:
    ping()
    blink_colours.append(10)

    for idx, item in enumerate(hosts.items()):
        if status[idx] == 0:
            print(item[1][1])
            blink_colours.append(item[1][1] + ',3,0')

    blink(blink_colours)

    if 0 in status:
        time.sleep(30)
    else:
        b2 = Blink1()
        b2.off()
        b2.close()
        time.sleep(30)

    status.clear()
    blink_colours.clear()
