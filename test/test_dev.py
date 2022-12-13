import sys
sys.path.append("C:\Code\RPI4-BlinkLed")
import dataclasses
import datetime
import typing
import com 
import pytest
import buffer
import logging
import dev
from test_com import spidev_mock

# Rought SPI device module functionality 

# - 1 create spi device
# - 2 open connection to that device
# - 3 send message via sending message, when spi writes
#     it also reads messages from spidev so those needs to be but 
#     into to separate FIFO
# - 4 message should contain always current datetime with each data
# - 5 Read messages from FIFO and then fifo is empty for next purposes
# - 6 Close spi connection


#########################################################################
# Test plan for SPI device
#########################################################################

## --fixtures

# - create spi device with fixture
# - create spi device fixture which is connected


## --tests

# Raise
# - 1 check that all needed parameters are valid for connecting device
#     expecting valueerror if there is not correct parameters
# - 2 check that with connection there is no runtimeerror rised
# - 3 check if there is tryed to send empty object and rise valueError

# Functions
# - 1 send 100 bytes with fake data and read those and assert that data is correct
# - 2 send 1 byte and assert that we recive that when doing read
# - 3 read some certain ammount of bytes from spi and those corrensponds to first once which are send
# - 4 check that timestamps are correct in read message

# GLOBAL VARIABLES

BUS=0
DEV=0

# check which enviroment is used (linux -> rpi, windows -> dev machine)
if sys.platform.startswith('linux'):
    import spidev
    pytestmark = pytest.mark.parametrize("spi_device", [spidev_mock(bus=BUS, dev=DEV), spidev.SpiDev()])
elif sys.platform.startswith('win32'):
    pytestmark = pytest.mark.parametrize("spi_device", [spidev_mock(bus=BUS, dev=DEV)])
else:
    raise RuntimeError("Unknown OS used! please update this switch case to support your OS!")

@dataclasses.dataclass
class objectss:
    dev_obj : dev.dev
    spi_obj : com.Communication

@pytest.mark.parametrize("device",[dev.spi_dev])
@pytest.fixture
def dev_obj(device : dev.spi_dev, spi_device : com.SPICom):
    


def dev_setup(dev_obj : objectss):
    
    dev_obj.dev_obj.setup()








