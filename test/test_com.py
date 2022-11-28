import sys
sys.path.append("C:\Code\RPI4-BlinkLed")
import dataclasses
import datetime
from typing import List
import com 
import pytest
import buffer
import logging

# Global variables
REAL_SYSTEM_IN_USE : bool = False
DEV : int = 1
BUS : int = 2

@dataclasses.dataclass
class data_format:
    data : bytes
    timestamp : datetime.datetime


class spidev_mock():
    def __init__(self, dev:int, bus:int) -> None:
        pass
    def open(self, bus,dev)->None:
        pass
    def close(self)->None:
        pass
    def writebytes2(self, list)->None:
        pass

# check if real system is used
if REAL_SYSTEM_IN_USE:
    # this is used when testing with real enviroment
    import spidev
    pytestmark = pytest.mark.parametrize("spidevobj", [spidev_mock(bus=BUS, dev=DEV), spidev.SpiDev()])
else:
    # this is used when testing without real enviroment
    pytestmark = pytest.mark.parametrize("spidevobj", [spidev_mock(bus=BUS, dev=DEV)])



@pytest.fixture
def com_obj(spidevobj : com.Communication)-> com.Communication:
    return com.SPICom(dev=DEV, bus=BUS, spidev=spidevobj)
@pytest.fixture
def com_obj_empty(spidevobj : com.Communication)->com.Communication:
    return com.SPICom(dev=DEV, bus=None, spidev=spidevobj)

@pytest.fixture
def com_obj_open(com_obj : com.Communication)->com.Communication:
    return com_obj.openConnection()


@pytest.fixture
def create_test_data(self)->List[bytes]:
    lista = []
    return [lista.append(bytes(i)) for i in range(0, 500)]

def test_open_communication(com_obj : com.Communication)->None:
    if com_obj == None:
        logging.warning("Ei oo mitää")
    logging.warning(f"testiiiiiiiii{com_obj.state=}")
    com_obj.openConnection()
    assert com_obj.state == com.com_state.CONNECTED

def test_open_communication_error(com_obj_empty:com.Communication)-> None:
    with pytest.raises(ValueError):
        com_obj_empty.openConnection()

def test_close_communcation_error(com_obj : com.Communication)->None:
    with pytest.raises(RuntimeError):
        com_obj.closeConnection()

def test_write_error(com_obj_empty : com.Communication)->None:
    with pytest.raises(RuntimeError):
        com_obj_empty.Write([123, "moi"])

def test_read_error(com_obj_empty : com.Communication)->None:
    with pytest.raises(RuntimeError):
        com_obj_empty.ReadBuffer()











