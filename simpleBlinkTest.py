## this programs puprose is to test out that code is working as excpected

import time
from gpiozero import LED

LEDPINNUMBER = 17
WAITTIME = 5

def blinkerSimple(lednum : int, waitTime : int)->None:
    led = LED(lednum)
    asd : bool = True

    while asd:
        led.toggle()
        time.sleep(waitTime)
        asdasd = input("do we continue? y=yes, n = no")
        if asdasd == "n":
            asd = False
            
        



def main()->None:
    blinkerSimple(lednum=LEDPINNUMBER, waitTime=WAITTIME)

if __name__ == "__main__":
    pass
