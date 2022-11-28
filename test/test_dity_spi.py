import sys
sys.path.append("C:\Code\RPI4-BlinkLed")
import os
import com
import pytest
import test.test_com
import logging


REAL_SYSTEM_IN_USE : bool = False

# Check are we running tests on rasberry pi as HIL or 
# in computer just as a unit test

if os.name == "posix":
    import spidev
    REAL_SYSTEM_IN_USE = True

DEV : int = 1
BUS : int = 1

TEST_DATA : list[bytes] = [12, 15, 15, 16, 00, 10]



@pytest.fixture
def spi_fixture() -> com.Communication:
    if REAL_SYSTEM_IN_USE:        
        logging.info("Real system in use")
        spid = com.SPICom(DEV, BUS, spidev=spidev.Spidev())
        spid.setup(max_speed_hz=50000, mode=0b01)
        return spid
    else:
        logging.info("Fake system in use")
        return com.SPICom(bus=BUS, dev=DEV,spidev=test.test_com.spidev_mock(bus=BUS, dev=DEV))
@pytest.fixture
def spi_dev_connected(spi_fixture : com.Communication)->com.Communication:
    spi_fixture.openConnection()
    return spi_fixture


def test_open_connection(spi_fixture : com.Communication)->None:
    spi_fixture.openConnection()
    spi_fixture.closeConnection()

def test_send_and_recive_data(spi_dev_connected : com.Communication)->None:
    spi_dev_connected.Write(TEST_DATA)
    data = spi_dev_connected.ReadBuffer()
    assert data == TEST_DATA, f"Data: {data=}\nTest_DATA:{TEST_DATA=}\n"
    spi_dev_connected.closeConnection()


