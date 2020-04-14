# import
import time
import os
import math
from blink1.blink1 import Blink1

# define the hosts to monitor (name, ip/hostname, colour for blink)
hosts = {
    'google DNS': ['8.8.8.8', 'Red'],
    'telstra gateway max': ['192.168.20.1', 'Orange'],
    'ubiquiti edgerouter poe 5': ['192.168.20.1', 'Yellow'],
    'apple airport extreme': ['192.168.20.2', 'Blue'],
    'secondary DNS': ['192.168.20.5', 'Green']
}

# list to track status
status = list()

# define sleep time for loop, this affects the frequency at which hosts are monitored (adapted to the number of hosts)
sleep_time = len(hosts) * 3


# blink the blink
def blink(colour):
    b1 = Blink1()
    b1.play_pattern(colour)
    b1.close()


# ping the hosts
def ping(down_count=0):
    for x in hosts.values():
        response = os.system('ping -c 1 ' + x[0])
        if response == 0:
            status.append(1)
        else:
            status.append(0)
            down_count += 1
    if down_count == 0:
        down_count = 1
    return down_count


# ping hosts, blink the blink, wait before testing again
while True:
    blink_colours = str(math.ceil((sleep_time + len(hosts)) / ping()))

    for idx, item in enumerate(hosts.items()):
        if status[idx] == 0:
            blink_colours = blink_colours + ', ' + item[1][1] + ',0.5,0, Black,0.5,0'

    if 0 in status:
        blink(blink_colours)
        time.sleep(sleep_time)
    else:
        b2 = Blink1()
        b2.off()
        b2.close()
        time.sleep(sleep_time)

    status.clear()
