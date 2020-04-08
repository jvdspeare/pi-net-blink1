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
    'st1': ['192.168.200.5', 'Green'],
    'st2': ['192.168.200.65', 'Red']
}

status = list()


def blink(colour):
    b1 = Blink1()
    b1.play_pattern(colour)
    b1.off()
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
    blink_colours = '10'

    for idx, item in enumerate(hosts.items()):
        if status[idx] == 0:
            print(item[1][1])
            blink_colours = blink_colours + ', ' + item[1][1] + ',0.3,0, Black,0.3,0'

    if 0 in status:
        print(blink_colours)
        blink(blink_colours)
        time.sleep(30)
    else:
        b2 = Blink1()
        b2.off()
        b2.close()
        time.sleep(30)

    status.clear()
