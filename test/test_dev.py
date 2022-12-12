import sys
sys.path.append("C:\Code\RPI4-BlinkLed")
import dataclasses
import datetime
from typing import List
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

REAL_SYSTEM_IN_USE : bool = False

# check which enviroment is used (linux -> rpi, windows -> dev machine)
if sys.platform.startswith('linux'):
    REAL_SYSTEM_IN_USE = True
elif sys.platform.startswith('win32'):
    REAL_SYSTEM_IN_USE = False
else:
    raise RuntimeError("Unknown OS used! please update this switch case to support your OS!")


# check if real system is used
if REAL_SYSTEM_IN_USE:
    # this is used when testing with real enviroment
    import spidev
    pytestmark = pytest.mark.parametrize("spi_device", [spidev_mock(bus=BUS, dev=DEV), spidev.SpiDev()])
else:
    # this is used when testing without real enviroment
    pytestmark = pytest.mark.parametrize("spi_device", [spidev_mock(bus=BUS, dev=DEV)])


@pytest.fixture(params=[])
def dev_obj(dev : dev.dev, spi_device : com.Communication):
    dev_obj = dev






