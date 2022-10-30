# do not use this!! use setup.py or python tomal to install it as module in
# in future
import sys
sys.path.append("C:\Code\RPI4-BlinkLed")

import buffer

import logging

logger = logging.Logger("Debugger", logging.INFO)


class asd:
    test = 15

    def printTest(self):
        print(self.test)


def main():
    
    test = buffer.fifo()
    asdd = asd()
    asdd.printTest()


if __name__ == "__main__":
    main()