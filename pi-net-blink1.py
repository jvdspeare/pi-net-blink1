# import
import time
import os
from blink1.blink1 import Blink1


hosts = {
    'edge router': ['192.168.20.1', 'red'],
    'secondary DNS': ['192.168.20.244', 'blue']
}


def blink(colour):
    b1 = Blink1()
    b1.fade_to_color(100, colour)
    b1.close()


def ping(host):
    response = os.system('ping -c 1 ' + host)
    time.sleep(0.3)
    return response


for x, y in hosts.items():
    print(x, y)
    if ping(y[0]) == 0:
        print('up')
        b2 = Blink1()
        b2.off()
        b2.close()
    else:
        print('down')
        blink(y[1])
