# import
import time
import os
from blink1.blink1 import Blink1

hosts = {
    'edge router': ['192.168.20.1', 'red'],
    'secondary DNS': ['192.168.20.5', 'blue']
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
            status.append(True)
            print(x + 'up')
        else:
            status.append(False)
            print(x + 'down')
            blink(y[1])

    print(status)

    x = any(status) == 1
    if x is True:
        print('#########!!!!!!!!')
        time.sleep(5)
    else:
        b2 = Blink1()
        b2.off()
        b2.close()

    status.clear()
