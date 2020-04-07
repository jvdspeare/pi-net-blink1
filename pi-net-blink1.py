# import
import time
import os
from blink1.blink1 import Blink1

hosts = {
    'google DNS': ['8.8.8.8', 'Red'],
    'telstra gateway max': ['192.168.20.1', 'Orange'],
    'ubiquiti edgerouter poe 5': ['192.168.20.1', 'Yellow'],
    'apple airport extreme': ['192.168.20.2', 'Blue'],
    'secondary DNS': ['192.168.20.5', 'Green']
}

status = list()


def blink(colour):
    b1 = Blink1()
    b1.fade_to_color(100, colour)
    b1.close()


def ping(host):
    response = os.system('ping -c 1 ' + host)
    time.sleep(0.3)
    return response


while True:
    for x, y in hosts.items():
        print(x, y)
        if ping(y[0]) == 0:
            status.append(1)
            print(x + 'up')
        else:
            status.append(0)
            print(x + 'down')
            blink(y[1])

    if 0 in status:
        print('#########!!!!!!!!')
    else:
        b2 = Blink1()
        b2.off()
        b2.close()

    time.sleep(10)

    status.clear()
