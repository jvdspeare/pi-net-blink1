# import
import time
import os
from blink1.blink1 import Blink1


hosts = {
    'edge router': ['192.168.20.1', 'red'],
    'secondary DNS': ['192.168.20.5', 'yellow'],
}


def blink(colour):
    b1 = Blink1()
    b1.fade_to_color(100, colour)


def ping(host):
    response = os.system('ping -c 1 ' + host)
    return response


for x, y in hosts:
    print(x, y)
    if ping('192.168.20.1') == 0:
        print('up')
        blink('blue')
    else:
        print('down')
        blink('yellow')
